'use strict';

// Personal Assistant API
app.factory('AnalysisAPI',
  function (Restangular) {
    return Restangular.service('analyze_data')
  }
);