# django-project
django-project

## version
```
python 3.8
Django==3.2
djangorestframework==3.14.0
drf-yasg==1.21.4
```

## start project
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

## add rest-framework
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

## add swagger
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


## add users app
```
mkdir ./toy_project/users
python manage.py startapp users ./toy_project/users
```
