from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryView)
router.register('products', views.ProductsView)

urlpatterns = [
    path('', include(router.urls))
]
