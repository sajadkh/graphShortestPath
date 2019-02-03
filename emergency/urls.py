from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sensor', views.SensorView)

urlpatterns = [
    url('path', views.PathView.as_view()),
    url(r'^', include(router.urls)),
]

