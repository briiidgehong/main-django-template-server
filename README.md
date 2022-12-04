# django-project

## - version
```
python 3.8
Django==3.2
djangorestframework==3.13.0
djangorestframework-simplejwt==5.2.2
drf-yasg==1.21.4
```

## - directory setting
```
project folder 안에 다음을 각각 위치시킨다.
이에 맞게 settings.py도 project prefix를 제거해주어야 한다.('toy_project.urls' -> 'urls')
- manage.py 
- requirements.py

.
├── README.md
├── db.sqlite3
└── toy_project
    ├── __init__.py
    ├── asgi.py
    ├── manage.py
    ├── requirements.txt
    ├── settings.py
    ├── urls.py
    ├── users
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── wsgi.py

```

## - start project
```
git clone https://github.com/briiidgehong/django-project.git
cd django-project
conda create --name django-project python=3.8
conda activate django-project
pip install django==3.2
django-admin startproject toy_project
pip freeze > requirements.txt
python manage.py runserver
```

## - add rest-framework
```
pip install djangorestframework==3.14.0
INSTALLED_APPS = [
    ...
    'rest_framework',
]
urlpatterns = [
    ...
    path('admin/', admin.site.urls), # default setting
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # add
]

admin/
api-auth/ login/ [name='login']
api-auth/ logout/ [name='logout']

```

## - add swagger
```
drf-yasg==1.21.4

# settings.py
INSTALLED_APPS = [
   ...
   # required for serving swagger ui's css/js files
   'django.contrib.staticfiles', 
   'drf_yasg',
   ...
]

# urls.py
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# settings.py
# connect swagger login and rest-framework login url
# 위에서 추가한 rest login url의 namespace를 사용하여 접근
# path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
LOGIN_URL = "rest_framework:login"
LOGOUT_URL = "rest_framework:logout"
```


## - add users app (user-model-custom / using AbstractUser model)
```
python manage.py startapp users 
# settings.py
INSTALLED_APPS = [
    'users',
]
AUTH_USER_MODEL = "users.Users"

# add models.py sourcecode
# add views.py sourcecode
# add users.urls.py sourcecode
# add urls.py sourcecode

python manage.py makemigrations
python manage.py migrate
```
<img width="1618" alt="스크린샷 2022-12-04 오후 8 58 27" src="https://user-images.githubusercontent.com/73451727/205489116-012d394f-f351-4003-ac66-5349d95223bf.png">

## - auth setting
```
1. BASIC TOKEN AUTH # django built-in func
from rest_framework.authentication import BasicAuthentication
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
```
```
2. SESSION - COOKIE AUTH # django built-in func
from rest_framework.authentication import SessionAuthentication
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
```
```
3. JWT TOEKN AUTH
pip install djangorestframework-simplejwt==5.2.2
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
from rest_framework_simplejwt.authentication import JWTAuthentication
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
```


## - dockerize

## - nginx setting
