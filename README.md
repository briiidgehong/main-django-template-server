# django-project
django-project

## version
```
python 3.8
django 3.2
rest-framework
drf-yasg
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

pip install djangorestframework==3.14.0
INSTALLED_APPS = [
    ...
    'rest_framework',
]
urlpatterns = [
    ...
    path('admin/', admin.site.urls), # default setting
    path('api-auth/', include('rest_framework.urls')) # add
]

admin/
api-auth/ login/ [name='login']
api-auth/ logout/ [name='logout']

```

## add users app
```
mkdir ./toy_project/users
python manage.py startapp users ./toy_project/users
```

## add swagger
```

```
