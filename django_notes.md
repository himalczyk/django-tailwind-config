# Start new project

```
django-admin startproject <project_name>
```

## Running a server

```
python manage.py runserver
```

## Running on different port

```
python manage.py runserver 5050
python manage.py runserver <port_number>
```

## Creating an App

```
python manage.py startapp <app_name>
```

## Views

- Views are HTTP requests
- urls are connected to specific views

### Display object from models in views

Look for a certain id in our path and pass that to the views.index

## URLs

## Linking apps with the project, the main guy

Set the url to the app in the urls project file and set pathing there
The path from there, we use a include method built in django to include pathing, specify the app name and look for its urls, the app urls. Then the urls we look for the views for the specified app that we have created.

# SQLite3 Database setup

## Models

Each model represent basically a database table

Working with a database, needs to modify the settings file in the project folder and add the application to the installed apps

## Changes migrations

Make any changes to the project it needed to do

```
python manage.py migrate
```

## Tell django we have made some changes to our project, makemigrations

```
python manage.py makemigrations home
python manage.py makemigrations <app_name>
```

This needs to be applied with the below or above migrate command

### Apply migrations with python migrate

## Add stuff to the database from the command line

Objects added to the database table are getting an id to .get() them automatically

Get into the shell interactive session

```
python manage.py shell
```

import classes from app.models
instantiate an object for the wanted class
save the instantiated object

```
from home.models import Item, ToDoList
t = ToDoList(name="Dawid\'s List")
t.save()
ToDoList.objects.all
```

Creating items:

```
t.item_set.create(attribute="value", attribute=value)
```

# Admin django dashboard

```
from home.models import Item, ToDoList
t = ToDoList.objects
t.all()
t.filter(name__startswith="Dawid")
```

## Give access (register) in the dashboard to the database table model created

its done in the admin app admin py file

# Templates

Dynamic html changing basing upon whatever we passsed to, connecting the backend to the frontend

## Base templates

A template for every other page, like the top navigation bar, banner and the footer.

### Inherit from base template to other templates

```
{%extends 'home/base.html'%}
```

#### Passing variables to templates from views

Inside the dictionary its a key of the dict in return that we can relate to in a template html view and using it get the value inside a "<p>" tag

```
def index(response, id):
    # get the database object that is being called in the url
    todo_list = ToDoList.objects.get(id=id)
    item = todo_list.item_set.get(id=id)
    # print the name of the todo list
    return render(response, "home/base.html", {"name":todo_list.name})
```

#### Block contents

In base html we can define placeholder blocks:

```
    {% block <block_name> %}
    {% endblock%}
```

Which basically is a placeholder for anyuthing we want, we can relate to any of the blocks by using the exact same naming convention we set those object in. The same block name needs to be used.

# Forms

Login form, create new account form, create new todo list

# Tailwind-django

python manage.py tailwind start

# Heroku notes

## Get tailed logs

heroku logs -t -a himalczyk

## Procfile

https://vibhurishi.blogspot.com/2013/02/heroku-error-h14-with-django.html

## Set secret key on heroku server

heroku config:set SECRET_KEY="YOUR_SECRET_KEY_VALUE"

## Deploy a build

git push heroku main

## Run console bash on heroku server

heroku run bash

## Check running web apps on heroku

heroku ps:scale web=1

## Run migrations on heroku

heroku run python portfolio_blog/manage.py migrate