"""Installable package to create working django app + project, django-tailwind config and virtual environment creation"""


import os
import shutil
from venv import create
import click
    

def create_initial_files(target_directory: str) -> None:
    """Copies the initial files that need to be at top level of project directory"""
    
    shutil.copy2('files/.gitignore', os.path.join(target_directory, '.gitignore'))
    shutil.copy2('files/README.md', os.path.join(target_directory, 'README.md'))
    pass

def get_project_admin_path(target_directory: str, django_app_name: str) -> str:
    """Creates the main project app folder PATH with settings.py and urls.py for the whole project"""
    path = os.path.join(target_directory, django_app_name)
    next_path = os.path.join(path, django_app_name)
    os.chdir(next_path)
    project_app_admin_path = os.getcwd()
    return project_app_admin_path

def replace_django_settings_file(project_app_admin_path: str):
    """Configures the project -> project_folder -> settings.py file with tailwind and new created app name"""
    shutil.copy2('files/settings.py', os.path.join(project_app_admin_path, 'settings.py'))
    pass
    
def replace_urls_file(project_app_admin_path: str):
    """Configures the urls.py for django-tailwind"""
    shutil.copy2('files/urls.py', os.path.join(project_app_admin_path, 'urls.py'))
    pass

def configure_django_settings_file(project_app_admin_path: str, django_app_name: str):
    os.chdir(project_app_admin_path)
    with open('settings.py', 'r') as read_settings_py:
        lines = read_settings_py.readlines()
        print(lines)
    with open('settings.py', 'w') as settings_py_file:
        for idx, line in enumerate(lines):
            if "'app_name'" in line:
                # replace the line with the current index, which is the current line to the django app name string
                lines[idx] = f"\t'{django_app_name}',\n"
                settings_py_file.writelines(lines)
    pass
    
def configure_django_urls_file(project_app_admin_path: str):
    pass

def create_django_startproject_files(target_directory: str, django_project_name: str) -> None:
    os.chdir(target_directory)
    os.system(f'cmd /c "django-admin startproject {django_project_name}"')
    return django_project_name
    
    
def create_django_app(poject_directory_name: str, django_app_name: str) -> str:
    """Creates the django app folder inside of the django project directory"""
    os.system(f'cmd /c cd {poject_directory_name}')
    os.system(f'python manage.py startapp {django_app_name}')
    return django_app_name

    
    
    
# @click.command()
# @click.option('--where', default=os.getcwd(), help='Name of the new project')

default = os.getcwd()
create_initial_files(default)
# django_project_name = create_django_startproject_files(default, 'django_config_creator')
# django_app_name = create_django_app(django_project_name, 'django_config')
# configure_django_app_settings(django_project_name, 'django_app_name')