from django.urls import include, path
from rest_framework import routers
from users import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r"", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]