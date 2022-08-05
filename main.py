"""Installable package to create working django app + project, django-tailwind config and virtual environment creation"""


import os
import shutil
import click

def create_initial_files(target_directory: str) -> None:
    """Copies the initial files that need to be at top level of project directory"""
    
    shutil.copy2('files/.gitignore', os.path.join(target_directory, '.gitignore'))
    shutil.copy2('files/README.md', os.path.join(target_directory, 'README.md'))
    pass

def create_django_startproject_files(target_directory: str, django_project_name: str) -> None:
    os.chdir(target_directory)
    os.system(f'cmd /c "django-admin startproject {django_project_name}"')
    
# @click.command()
# @click.option('--where', default=os.getcwd(), help='Location of the new project')

default = os.getcwd()
create_django_startproject_files(default, 'django_config_creator')