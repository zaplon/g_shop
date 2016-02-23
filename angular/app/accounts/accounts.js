'use strict';

angular.module('app.accounts', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: 'accounts/login',
    controller: 'AccountsCtrl'
  });
}])

.controller('AccountsCtrl', function($scope, $http) {
    $scope.doLogin = function(){
        var promise = $http.post('/rest-auth/login/', {'username': $scope.username, 'password': $scope.password});
        promise.then(function(){
            //key
        });
    }
});