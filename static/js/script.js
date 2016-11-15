var SearchMode = {
  ADDRESS: 1,
  TEXT: 2
};

function IndexCtrl($scope, $repService, $location, $repResults, $repAutocompleteData) {
  $scope.form = {
    address: null,

    searchText: null,
    selectedSearchItem: null
  };
  $scope.state = {
    loading: false,
    searchMode: SearchMode.ADDRESS
  };
  $scope.SearchMode = SearchMode;

  $scope.placeSelected = function(place) {
    $scope.state.loading = true;
    var location = place.geometry.location;
    $repService.lookupByLatLng(location.lat(), location.lng())
      .then(function(response) {
        $scope.state.loading = false;
        $repResults.fromLookupResponse(response.data);
        $location.path('/district/' + response.data['house_rep']['district_code']);
      });
  };

  $scope.$watch('form.selectedSearchItem', function(item, oldItem) {
    if (item !== oldItem) {
      $location.path('/rep/' + item.repId);
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
        name: row[1] + ' ' + row[2],
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
      $repService.lookupByDistrictCode($routeParams.districtCode)
        .then(function(response) {
          $scope.state.loading = false;
          $repResults.fromLookupResponse(response.data);
        });
    };
  };

  this.init();
}

function RepPageCtrl($scope, $repService, $routeParams) {
  $scope.state = {loading: false};

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

function RepResults(houseRep, senators, leadership) {
  this.houseRep = houseRep;
  this.senators = senators || [];
  this.leadership = leadership || [];

  this.fromLookupResponse = function(data) {
    this.houseRep = data['house_rep'];
    this.senators = data['senators'] || [];
    this.leadership = data['leadership'] || [];
  };

  this.clear = function() {
    this.houseRep = null;
    this.senators = [];
    this.leadership = [];
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
    .when('/rep/:repId', {
      templateUrl: 'rep-page-template'
    })
    .when('/district/:districtCode', {
      templateUrl: 'district-template'
    })
    .when('/state/:stateCode', {
      templateUrl: 'state-template'
    })
    .otherwise({
      templateUrl: 'index-template'
    });
  $locationProvider.html5Mode(true);
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
    .service('$repService', RepService)
    .directive('googlePlaceAutocomplete', googlePlaceAutocomplete)
    .value('$repResults', new RepResults())
    .value('$repAutocompleteData', clientConfig['rep_autocomplete_data'])
    .config(routeConfig);
}
