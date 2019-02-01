from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'path', views.PathView)

urlpatterns = [
    url('source', views.SourceView.as_view()),
    url(r'^', include(router.urls)),
]

