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
python manage.py runserver
```
<img width="1618" alt="스크린샷 2022-12-04 오후 8 58 27" src="https://user-images.githubusercontent.com/73451727/205489116-012d394f-f351-4003-ac66-5349d95223bf.png">

## - dockerize
```
pip install gunicorn==20.1.0
pip install psycopg2-binary==2.9.5
pip freeze > requirements.txt
```

```
# db setting
1. local-db
2. rds
```

### add ./toy_project/Dockerfile
### add ./toy_project/entrypoint.sh

### add ./docker-compose-local-db.yml
### add ./docker-compose-rds.yml
### add ./.env_local

```
# urls.py - static file 처리
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
```

```
# settings.py

import os
ENV_WHOAMI = os.environ.get("WHOAMI")
ENV_SECRET_KEY = os.environ.get("SECRET_KEY")

> local-db setting
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
        "TEST": {"NAME": "test_database"},
    }
}

> rdb setting

```

```
docker-compose -f docker-compose-local-db.yml up
0.0.0.0:8080/swagger
```
<img width="1175" alt="스크린샷 2022-12-24 오전 11 59 58" src="https://user-images.githubusercontent.com/73451727/209419033-4060711f-1f15-4657-98d6-93ee435ce61b.png">


## - nginx setting
```
- 
```


## - auth setting
```
1. BASIC TOKEN AUTH # django built-in func
from rest_framework.authentication import BasicAuthentication
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
```
<img width="514" alt="스크린샷 2022-12-05 오후 5 19 29" src="https://user-images.githubusercontent.com/73451727/205588260-186b68df-df07-4fd7-8a37-4bc41500f744.png">
<img width="901" alt="스크린샷 2022-12-05 오후 5 17 49" src="https://user-images.githubusercontent.com/73451727/205588229-8bb41297-68a0-43e5-bfe9-9dc0b204a785.png">


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
