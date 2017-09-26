from django.conf.urls import include, url
from rest_auth import views as rest_auth_views
from rest_framework.routers import DefaultRouter
from apps.api.views.accounts import SignUPView

from apps.api.views import stores as stores_viewset


router = DefaultRouter()

router.register('stores', stores_viewset.StoreViewSet, base_name='stores')
router.register('products', stores_viewset.ProductViewSet, base_name='products')
router.register('vendors', stores_viewset.VendorViewSet, base_name='vendors')
router.register('purchasebills', stores_viewset.PurchaseBillViewSet, base_name='purchasebills')
router.register('purchasedetails', stores_viewset.PurchaseDetailViewSet, base_name='purchasedetails')
router.register('sellbills', stores_viewset.SellBillViewSet, base_name='sellbills')
router.register('selldetails', stores_viewset.SellDetailViewSet, base_name='selldetails')

urlpatterns = [
    url('^', include(router.urls)),
    url('analyze_data/$', stores_viewset.AnalysisView.as_view())
]

urlpatterns += [
    url(r'^login/$', rest_auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', rest_auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignUPView.as_view(), name='signup'),
    # Using default view but using custom serializer PasswordResetSerializer
    url(r'^password/reset/$', rest_auth_views.PasswordResetView.as_view(), name='password_reset'),
    # Using default view and serializer
    url(r'^password/reset/confirm/$', rest_auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

