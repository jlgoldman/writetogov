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

function IndexCtrl($scope, $repService, $location, $repResults, $repAutocompleteData) {
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
        $location.path('/district/' + response.data['house_rep']['district_code']);
      });
  };

  $scope.setSearchMode = function(searchMode) {
    $scope.state.searchMode = searchMode;
    $scope.state.searchBoxFocused = true;
  };

  $scope.$watch('form.selectedSearchItem', function(item, oldItem) {
    if (item !== oldItem) {
      $location.path('/compose/' + item.repId);
    };
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

function DistrictCtrl($scope, $repResults, $repService, $routeParams) {
  $scope.repResults = $repResults;
  $scope.state = {
    loading: false
  };

  this.init = function() {
    if (!$repResults.houseRep) {
      $scope.state.loading = true;
      $repResults.clear();
      $repService.lookupByDistrictCode($routeParams.districtCode)
        .then(function(response) {
          $scope.state.loading = false;
          $repResults.updateFromLookupResponse(response.data);
        });
    };
  };

  this.init();
}

function RepPageCtrl($scope, $repService, $routeParams) {
  $scope.state = {loading: false};
  $scope.rep = null;

  this.init = function() {
    $scope.state.loading = true;
    $repService.getByRepId($routeParams.repId)
      .then(function(response) {
        $scope.state.loading = false;
        $scope.rep = response.data['reps'][0]
      });
  };

  this.init();
}

function ReminderCtrl($scope) {
  $scope.form = {
    email: null
  };
  $scope.Frequency = Frequency;
}

function ComposeCtrl($scope, $repService, $routeParams) {
  $scope.state = {loading: false};
  $scope.form = {
    repId: $routeParams.repId,
    body: null,
    nameAndAddress: null
  };
  $scope.currentDate = new Date();
  $scope.rep = null;

  this.init = function() {
    $scope.state.loading = true;
    $repService.getByRepId($routeParams.repId)
      .then(function(response) {
        $scope.state.loading = false;
        $scope.rep = response.data['reps'][0]
      });
  };

  $scope.isFormComplete = function() {
    return $scope.form.body && $scope.form.body.trim()
      && $scope.form.nameAndAddress && $scope.form.nameAndAddress.trim();
  };

  this.init();
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

function routeConfig($routeProvider, $locationProvider) {
  $routeProvider
    .when('/district/:districtCode', {
      templateUrl: 'district-template'
    })
    .when('/state/:stateCode', {
      templateUrl: 'state-template'
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
    .controller('RepPageCtrl', RepPageCtrl)
    .controller('ReminderCtrl', ReminderCtrl)
    .controller('ComposeCtrl', ComposeCtrl)
    .service('$repService', RepService)
    .directive('repCard', repCard)
    .directive('googlePlaceAutocomplete', googlePlaceAutocomplete)
    .value('$repResults', new RepResults())
    .value('$repAutocompleteData', clientConfig['rep_autocomplete_data'])
    .config(routeConfig)
    .config(themeConfig)
    .config(function($mdGestureProvider) {
      // See https://github.com/angular/material/issues/1441
      // In this case, causes taps on Google Place Autocomplete
      // results on mobile to be ignored without this.
      $mdGestureProvider.skipClickHijack();
    });
}
