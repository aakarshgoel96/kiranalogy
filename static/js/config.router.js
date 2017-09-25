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
        if (toState.data.redirectOn && $auth.isAuthenticated()){
          event.preventDefault();
          $state.go(toState.data.redirectOn);
        }
        // check if this state need login
        if (toState.data && toState.data.loginRequired) {
          loginRequired = true;
        }
        // if yes and if this user is not logged in, redirect him to login page
        if (loginRequired && !$auth.isAuthenticated()) {
          event.preventDefault();
          $state.go('access.login');
        }
        // check if this state need skipping
        if (toState.data && toState.data.skipRequired) {
          skipRequired = true;
        }
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
            templateUrl: '/tpl/home.html',
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
        .state('access.logout', {
            url: '/logout/',
            template: null,
            data: {loginRequired: true},
            controller: 'LogoutController',

          }
        )
        .state(
          'access.reset-password', {
            url: '/reset/password/',
            templateUrl: '/tpl/auth_tpl/resetPassword.html',
            data: {skipRequired: true},

          }
        )
        .state(
          'access.selection', {
            url: '/selection/',
            template: null,
            data: {loginRequired: true},
            controller: 'SelectionController',

          }
        )
        .state('access.404', {
          url: '/404/',
          templateUrl: '/tpl/404.html',
          data: {skipRequired: true}
        });
    }
  );