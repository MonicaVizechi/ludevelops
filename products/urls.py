from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductViewSet.as_view(), name="product-list"),
    path('<int:pk>/', views.ProductDetailViewSet.as_view(), name="product-detail"),
    path('sellers/', views.SellerViewSet.as_view(), name="seller-list"),
    path('sellers/<int:pk>/',
         views.SellerDetailViewSet.as_view(), name="seller-detail")
]