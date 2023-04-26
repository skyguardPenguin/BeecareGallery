from django.urls import path
from rest_framework import routers
from .api import beephotoViewSet


router = routers.DefaultRouter()
router.register('api/beephoto', beephotoViewSet, 'beephoto')



urlpatterns = router.urls +[
    path('api/beephoto/get_image/<int:pk>', beephotoViewSet.as_view({'get':'get_image'}), name='get_beephoto')
]

# urlpatterns = [
#     path('', views.test_image_view, name='test_image_view'),
# ]