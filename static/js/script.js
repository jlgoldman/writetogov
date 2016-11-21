var SearchMode = {
  ADDRESS: 1,
  TEXT: 2
};

var Chamber = {
  HOUSE: 'HOUSE',
  SENATE: 'SENATE'
};

var RepStatus = {
  ACTIVE: 'ACTIVE',
  LEFT_CONGRESS: 'LEFT_CONGRESS',
  DEFEATED_IN_GENERAL: 'DEFEATED_IN_GENERAL',
  DEFEATED_IN_PRIMARY: 'DEFEATED_IN_PRIMARY',
  RETIRING: 'RETIRING',
  SEEKING_OTHER_OFFICE: 'SEEKING_OTHER_OFFICE',
  PENDING_RESULT: 'PENDING_RESULT'
};

var Frequency = {
  WEEKLY: 'WEEKLY',
  MONTHLY: 'MONTHLY'
};

function IndexCtrl($scope, $repService, $location,
    $pageTransitioner, $repResults, $repAutocompleteData, $document) {
  $scope.form = {
    address: null,

    searchText: null,
    selectedSearchItem: null
  };
  $scope.state = {
    loading: false,
    searchMode: SearchMode.ADDRESS,
    searchBoxFocused: false
  };
  $scope.SearchMode = SearchMode;

  $scope.placeSelected = function(place) {
    $scope.state.loading = true;
    var location = place.geometry.location;
    $repResults.clear();
    $repService.lookupByLatLng(location.lat(), location.lng())
      .then(function(response) {
        $scope.state.loading = false;
        $repResults.updateFromLookupResponse(response.data);
        $pageTransitioner.goToDistrictPage(response.data['house_rep']['district_code']);
      });
  };

  $scope.setSearchMode = function(searchMode) {
    $scope.state.searchMode = searchMode;
    $scope.state.searchBoxFocused = true;
  };

  $scope.$watch('form.selectedSearchItem', function(item, oldItem) {
    if (item !== oldItem) {
      $pageTransitioner.goToComposePage(item.repId);
    };
  });

  $scope.$watch(function() {return $location.path();}, function(path, oldPath) {
    if (path == '/') {
      $document[0].title = 'Write to the Government - Write Your Elected Representatives';
    }
  });

  $scope.textSearch = function(query) {
    if (!query) {
      return [];
    }

    function queryPartMatches(queryPart, row) {
      return _.some(row, function(rowPart) {
        return rowPart && rowPart.indexOf && rowPart.toLowerCase().indexOf(queryPart) == 0;
      });
    }

    var parts = _.map(query.split(/\s+/), function(s) {
      return s.toLowerCase();
    });
    var matchingRows = _.filter($repAutocompleteData, function(row) {
      var isMatch = true;
      _.each(parts, function(queryPart) {
        if (queryPart && !queryPartMatches(queryPart, row)) {
          isMatch = false;
        }
      });
      return isMatch;
    });
    var items = _.map(matchingRows, function(row) {
      return {
        repId: row[0],
        name: row[1] ? row[1] + ' ' + row[2] : '(vacant)',
        stateName: row[4],
        districtOrdinal: row[7],
        title: row[8]
      }
    });
    return items;
  };
}

function DistrictCtrl($scope, $repResults, $repService, $preloadData, $routeParams, $document) {
  if ($preloadData.lookupResp && $preloadData.lookupResp['house_rep']) {
    $repResults.updateFromLookupResponse($preloadData.lookupResp);
  }
  $scope.repResults = $repResults;

  if ($repResults.houseRep) {
    var template = _.template('<%= stateName %>\'s <%= ordinal %> District - Write to the Government');
    $document[0].title = template({
      stateName: $repResults.houseRep['state_name'],
      ordinal: $repResults.houseRep['district_ordinal']
    });
  }

  // HACK: After doing an address search, make sure we're back to the
  // top of the page.
  $document[0].body.scrollTop = 0;
}

function ReminderCtrl($scope, $reminderService) {
  $scope.form = {
    email: null,
    frequency: Frequency.WEEKLY
  };
  $scope.Frequency = Frequency;
  $scope.submitting = false;
  $scope.success = false;
  $scope.error = false;

  $scope.formValid = function() {
    return $scope.form.email && $scope.form.email.indexOf('@') != -1;
  };

  $scope.submit = function() {
    $scope.error = false;
    $scope.success = false;
    $scope.submitting = true;
    $reminderService.create($scope.form.email, $scope.form.frequency)
      .then(function(response) {
        $scope.submitting = false;
        $scope.success = true;
      }, function(response) {
        $scope.submitting = false;
        $scope.error = true;
      });
  };
}

function ComposeCtrl($scope, $repService, $routeParams, $preloadData, $document) {
  $scope.state = {
    loading: false,
    mailFormOpen: false,
    composeComplete: false
  };
  $scope.form = {
    repId: $routeParams.repId,
    body: null,
    nameAndAddress: null
  };
  $scope.currentDate = new Date();
  $scope.rep = $preloadData.rep || null;

  this.init = function() {
    if ($scope.rep) {
      return;
    }
    $scope.state.loading = true;
    $repService.getByRepId($routeParams.repId)
      .then(function(response) {
        $scope.state.loading = false;
        $scope.rep = response.data['reps'][0];

        if ($scope.rep) {
          var template = _.template('Write to <%= title %> <%= first %> <%= last %> - Write to the Government');
          $document[0].title = template({
            title: $scope.rep['title'],
            first: $scope.rep['first_name'],
            last: $scope.rep['last_name']
          });
        }
      });
  };

  $scope.isFormComplete = function() {
    return $scope.form.body && $scope.form.body.trim()
      && $scope.form.nameAndAddress && $scope.form.nameAndAddress.trim();
  };

  $scope.openMailForm = function() {
    $scope.state.mailFormOpen = true;
    // HACK: Make sure we scroll to the top of the page so the form is properly visble;
    $document[0].body.scrollTop = 0;
  };

  this.init();
}

function RepStripeFormCtrl($scope, $StripeCheckout, $stripePublishableKey, $letterService) {
  $scope.submitting = false;
  $scope.errors = [];

  var stripeHandler = $StripeCheckout.configure({
    key: $stripePublishableKey,
    image: 'https://www.writetogov.com/static/img/logo-bluegrey-1024.png',
    locale: 'auto',
    token: function(tokenData) {
      $scope.$apply(function() {
        $scope.submitting = true;
        $scope.errors = [];
        $letterService.generateAndMail(tokenData['id'], $scope.rep['rep_id'], $scope.body, $scope.nameAndAddress)
          .then(function(response) {
            $scope.submitting = false;
          }, function(response) {
            $scope.submitting = false;
            console.log(response);
            $scope.errors = response.data['errors'];
          })
      });
    }
  });

  $scope.openStripeCheckout = function() {
    var descTemplate =  _.template('Mail a letter to <%= title %> <%= first %> <%= last %>');
    var description = descTemplate({
      title: $scope.rep['title'],
      first: $scope.rep['first_name'],
      last: $scope.rep['last_name']
    });
    stripeHandler.open({
      name: 'Write to the Government',
      description: description,
      amount: 150,
      allowRememberMe: false
    });
  };
}

function repStripeForm() {
  return {
    scope: {
      rep: '=',
      body: '=',
      nameAndAddress: '=',
      buttonText: '@',
    },
    templateUrl: 'rep-stripe-form-template',
    controller: RepStripeFormCtrl
  };
}

function RepResults(houseRep, senators, houseSpeaker, senateMajorityLeader) {
  this.houseRep = houseRep;
  this.senators = senators || [];
  this.houseSpeaker = houseSpeaker;
  this.senateMajorityLeader = senateMajorityLeader;

  this.updateFromLookupResponse = function(data) {
    this.clear();

    this.houseRep = data['house_rep'];
    this.senators = data['senators'] || [];

    var houseSpeaker = _.find(data['leadership'], function(rep) {
      return rep['chamber'] == Chamber.HOUSE;
    });
    if (!houseSpeaker || !this.houseRep || houseSpeaker['rep_id'] != this.houseRep['rep_id']) {
      this.houseSpeaker = houseSpeaker;
    }

    var senMaj = _.find(data['leadership'], function(rep) {
      return rep['chamber'] == Chamber.SENATE;
    });
    if (!senMaj || _.isEmpty(this.senators)
      || (senMaj['rep_id'] != this.senators[0]['rep_id']
        && senMaj['rep_id'] != this.senators[1]['rep_id'])) {
      this.senateMajorityLeader = senMaj;
    }
  };

  this.clear = function() {
    this.houseRep = null;
    this.senators = [];
    this.houseSpeaker = null;
    this.senateMajorityLeader = null;
  };
}

function PreloadData(rep, lookupResp) {
  this.rep = rep;
  this.lookupResp = lookupResp;

  this.clear = function() {
    this.rep = null;
    this.lookupResp = null;
  }
}

function repCard() {
  var repStatusToMessage = {
    'RETIRING': 'Retiring',
    'DEFEATED_IN_GENERAL': 'Defeated - term ends January 3',
    'DEFEATED_IN_PRIMARY': 'Defeated in primary - term ends January 3',
    'SEEKING_OTHER_OFFICE': 'Seeking other office',
    'PENDING_RESULT': 'Re-election pending result'
  };

  return {
    scope: {
      rep: '=',
      extraTitle: '@',
      hideActions: '='
    },
    templateUrl: 'rep-card-template',
    controller: function($scope) {
      $scope.RepStatus = RepStatus;

      if ($scope.rep['status'] == RepStatus.LEFT_CONGRESS) {
        $scope.statusMessage = $scope.rep['status_note'];
      } else {
        $scope.statusMessage = repStatusToMessage[$scope.rep['status']];
      }
    }
  };
}

function googlePlaceAutocomplete($parse) {
  return {
    require: 'ngModel',
    link: function(scope, element, attrs, model) {
      var options = {
        types: [],
        componentRestrictions: {}
      };
      scope.gPlace = new google.maps.places.Autocomplete(element[0], options);
      var selectFn = attrs.onSelect ? $parse(attrs.onSelect) : null;

      google.maps.event.addListener(scope.gPlace, 'place_changed', function() {
        scope.$apply(function() {
          model.$setViewValue(element.val());
          selectFn && selectFn(scope, {$place: scope.gPlace.getPlace()});
        });
      });
    }
  };
}

function RepService($http) {
  this.getByRepId = function(repId) {
    var req = {
      'rep_ids': [parseInt(repId)]
    };
    return $http.post('/rep_service/get', req);
  };

  this.lookupByLatLng = function(lat, lng) {
    var req = {
      'latlng': {
        'lat': lat,
        'lng': lng
      }
    };
    return $http.post('/rep_service/lookup', req);
  };

  this.lookupByDistrictCode = function(code) {
    var req = {
      'district_code': code
    };
    return $http.post('/rep_service/lookup', req);
  };
}

function ReminderService($http) {
  this.create = function(email, frequency) {
    var req = {
      'email': email,
      'frequency': frequency
    };
    return $http.post('/reminder_service/create', req);
  };
}

function LetterService($http) {
  this.generateAndMail = function(stripeToken, repId, body, nameAndAddress) {
    var req = {
      'stripe_token': stripeToken,
      'rep_id': repId,
      'body': body,
      'name_and_address': nameAndAddress
    };
    return $http.post('/letter_service/generate_and_mail', req);
  };
}

function PageTransitioner($document, $location, $preloadData) {
  this.goToComposePage = function(repId) {
    $preloadData.clear();
    $location.path('/compose/' + repId);
  };

  this.goToDistrictPage = function(districtCode) {
    $preloadData.clear();
    $location.path('/district/' + districtCode);
  };
}

function routeConfig($routeProvider, $locationProvider) {
  $routeProvider
    .when('/district/:districtCode', {
      templateUrl: 'district-template'
    })
    .when('/compose/:repId', {
      templateUrl: 'compose-template'
    })
    .otherwise({
      templateUrl: 'index-template'
    });
  $locationProvider.html5Mode(true);
}

function themeConfig($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue-grey')
    .accentPalette('orange')
    .warnPalette('red');
}

var BRACKET_INTERPOLATOR = function ($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}

function initMain(clientConfig) {
  angular.module('mainApp', ['ngMaterial', 'ngRoute'], BRACKET_INTERPOLATOR)
    .controller('IndexCtrl', IndexCtrl)
    .controller('DistrictCtrl', DistrictCtrl)
    .controller('ReminderCtrl', ReminderCtrl)
    .controller('ComposeCtrl', ComposeCtrl)
    .service('$repService', RepService)
    .service('$reminderService', ReminderService)
    .service('$letterService', LetterService)
    .service('$pageTransitioner', PageTransitioner)
    .directive('repCard', repCard)
    .directive('googlePlaceAutocomplete', googlePlaceAutocomplete)
    .directive('repStripeForm', repStripeForm)
    .value('$repResults', new RepResults())
    .value('$repAutocompleteData', clientConfig['rep_autocomplete_data'])
    .value('$preloadData', new PreloadData(clientConfig['rep'], clientConfig['lookup_response']))
    .value('$StripeCheckout', window['StripeCheckout'])
    .value('$stripePublishableKey', clientConfig['stripe_publishable_key'])
    .config(routeConfig)
    .config(themeConfig)
    .config(function($mdGestureProvider) {
      // See https://github.com/angular/material/issues/1441
      // In this case, causes taps on Google Place Autocomplete
      // results on mobile to be ignored without this.
      $mdGestureProvider.skipClickHijack();
    });
}
