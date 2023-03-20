from django.urls import path
from rest_framework import routers
from .api import loadViewSet
router =routers.DefaultRouter()
router.register('api/buzzfeed', loadViewSet,'load')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.test_image_view, name='test_image_view'),
# ]