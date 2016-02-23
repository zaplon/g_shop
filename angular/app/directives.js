'use strict';

angular.module('app.directives', [])
.directive('gForm', function ($http) {
    return {
        templateUrl: 'templates/gform.html',
        scope: {class: '@class'},
        restrict: 'E',
        controller: function ($scope, $modal, Examinations) {

            $scope.form = $http.post('/utils/get-form/', {'class': $scope.class});

        }
    };
})