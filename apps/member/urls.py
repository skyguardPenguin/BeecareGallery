from django.urls import path
from rest_framework import routers
from .api import memberphotoViewSet

router = routers.DefaultRouter()
router.register('api/memberphoto',memberphotoViewSet, 'memberphoto')
urlpatterns = router.urls +[
    path('api/memberphoto/get_image/<int:pk>', memberphotoViewSet.as_view({'get':'get_image'}), name='get_memberphoto')
]