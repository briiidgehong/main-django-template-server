from django.urls import include, path
from rest_framework import routers
from users import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r"", views.UserViewSet)

urlpatterns = [
    url(r"^register", views.RegisterView.as_view()),
    url(r"^session-login", views.SessionLoginView.as_view()),
    url(r"^session-logout", views.SessionLogoutView.as_view()),
    
    # get jwt token
    # refresh jwt token
]
urlpatterns += router.urls