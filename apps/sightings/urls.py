from django.urls import path
from rest_framework import routers
from .api import speciesViewSet,sightingsViewSet,beephotoViewSet


router = routers.DefaultRouter()
router.register('api/species', speciesViewSet,'species')
router.register('api/sightings', sightingsViewSet,'sightings')
router.register('api/beephoto', beephotoViewSet, 'beephoto')



urlpatterns = router.urls

# urlpatterns = [
#     path('', views.test_image_view, name='test_image_view'),
# ]