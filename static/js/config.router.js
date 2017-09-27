/**
 * Router configurations
 * Created by Vaibhav Jain on 22/10/16.
 * Website: https://www.kaizentechlabs.in
 * kaizentech cloud solutions private limited. All Rights Reserved.
 */

'use strict';

app.run(
  function ($rootScope, $state, $stateParams, $auth) {
    $rootScope.$state = $state;
    $rootScope.$stateParams = $stateParams;
    $rootScope.$on('$stateChangeStart',
      function (event, toState) {
        var loginRequired = false;
        var skipRequired = false;
        // if yes and if this user is logged in, redirect him to dashboard page
        // if (skipRequired && $auth.isAuthenticated()) {
        //   event.preventDefault();
        //   $state.go('access.selection');
        // }
      }
    );
  })
  .config(function ($httpProvider) {
      $httpProvider.interceptors.push('HTTP403Interceptor');
    }
  )
  .config(
    function ($stateProvider, $urlRouterProvider) {
      $stateProvider
        .state('home', {
            url: '',
            templateUrl: '/tpl/home.html'
          }
        )
        .state('analysis_data', {
            url: '/analyze-data',
            templateUrl: '/tpl/analysis.html',
          }
        )
          .state('cat-subcat', {
            url: '/cat-subcat',
            templateUrl: '/tpl/cat-subcat.html',
          }
        )
          .state('cat-brand', {
            url: '/cat-brand',
            templateUrl: '/tpl/cat-brand.html',
          }
        )
        .state('app', {
            abstract: true,
            url: '/app/',
            templateUrl: '/tpl/app.html',
            data: {loginRequired: false}
          }
        )
        .state('access', {
            url: '/access',
            template: '<div ui-view class="fade-in-right-big smooth"></div>'
          }
        )
        .state('access.login', {
            url: '/login/',
            templateUrl: '/tpl/auth_tpl/login.html',
            data: {skipRequired: true},
            resolve: {
              deps: ['uiLoad',
                function( uiLoad ){
                  return uiLoad.load([
                    // '/static/js/controllers/auth.Controllers.js'
                  ]);
                }
              ]
            }
          }
        )
		.state('access.signup', {
            url: '/signup/',
            templateUrl: '/tpl/auth_tpl/signup.html',
            data: {skipRequired: true, loginRequired:false},
            resolve: {
              deps: ['uiLoad',
                function( uiLoad ){
                  return uiLoad.load([
                    // '/static/js/controllers/auth.Controllers.js'
                  ]);
                }
              ]
            }
          }
        )
    }
  );