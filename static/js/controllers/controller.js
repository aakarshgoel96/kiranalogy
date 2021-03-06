'use strict';

app.controller('DataAnalysisController',
  function ($scope, AnalysisService, $state) {
    $scope.data = 'HAIR';
    $scope.categories = ['PACKED FOOD', 'HAIR', 'BISCUITS','ICE CREAM','OIL','BEVERAGES','TEA','PFW','HOUSEHOLD','HHC',
    'CPD','CLEANERS','ORAL','SKIN','BABY PRODUCTS','SOAP','Skin','Hair','PPW','DETERGENTS','Tea','PACKED RICE / ATTA',
    'CHOCOLATE','Unknown','Oral','SAUCE','MPW','PPW Liquids','DEODORANT','MFW','FEMCARE','Coffee','DMT','DIPS','TOILETRY',
    'COFFEE','ENERGY & HEALTH DRINKS','DAIRY PRODUCTS','Others','HUL 3','FACE','READY TO EAT & COOK','NOODLES','CIGARETTES',
    'ORGANIC STAPLES','DRY FRUITS','FRUIT DRINKS & JUICES','MEDICINE','PASTA & VERMICELLI','VEG SNACKS','BODY','KCLL','BOOKS & PERIODICALS',
    'JAMS & SPREADS','SAUCES & KETCHUP','BREAKFAST CEREALS','WATER','MUKHWAS & MOUTH FRESHENER','CHOCOLATES & CONFECTIONARY',
    'HOUSE NEEDS','MASALA','TEA & COFFEE','ORGANIC FOODS','BREAD & BAKERY','SHAMPOO','FLOURS & SOOJI','SKIN FACE CARE','FLOOR',
    'RICE & RICE PRODUCTS','BAKING & DESSERT ITEMS','MASALAS & SPICES','ORAL CARE','TOILET FLOOR & OTHER CLEANERS','PAPER & DISPOSABLE',
    'OTC', 'SKIN BODY CARE', 'OTHERS']

	$scope.Submit = function () {
		console.log($scope.data)
		AnalysisService.one('').customPOST({"category": $scope.data}).then(function (success) {
			$state.go('analysis_data')
		})

	}
  }
);
