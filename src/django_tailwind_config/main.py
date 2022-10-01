"""Installable package to create working django app + project, django-tailwind config and virtual environment creation"""


import os
import platform
import shutil
from venv import create
import click


def create_initial_files(target_directory: str) -> None:
    """Copies the initial files that need to be at top level of project directory"""
    shutil.copy2('files/.gitignore', os.path.join(target_directory, '.gitignore'))
    shutil.copy2('files/README.md', os.path.join(target_directory, 'README.md'))
    shutil.copy2('files/requirements.txt', os.path.join(target_directory, 'requirements.txt'))
    pass


def create_virtual_env(target_directory: str) -> None:
    """Creates and activates the virtual env"""
    os.chdir(target_directory)
    os.system('cmd /c "python -m venv venv"')
    pass


def activate_virtual_env() -> None:
    """Activate venv"""
    os.system('cmd /c "venv\Scripts\activate"')
    pass


def install_requirements() -> None:
    """Install requirements
        Installing: django, django-tailwind
    """
    os.system('cmd /c "python pip install requirements.txt"')
    pass


def create_django_startproject_files(target_directory: str, django_project_name: str) -> str:
    """Runs django-startproject command"""
    os.chdir(target_directory)
    os.system(f'cmd /c "django-admin startproject {django_project_name}"')
    return django_project_name


def create_django_app(poject_directory_name: str, django_app_name: str) -> str:
    """Creates the django app folder inside of the django project directory"""
    os.system(f'cmd /c cd {poject_directory_name}')
    os.system(f'python manage.py startapp {django_app_name}')
    return django_app_name


def replace_django_settings_file(project_app_admin_path: str) -> None:
    """Configures the project -> project_folder -> settings.py file with tailwind and new created app name"""
    shutil.copy2('files/settings.py', os.path.join(project_app_admin_path, 'settings.py'))
    pass
    
    
def replace_urls_file(project_app_admin_path: str) -> None:
    """Configures the urls.py for django-tailwind"""
    shutil.copy2('files/urls.py', os.path.join(project_app_admin_path, 'urls.py'))
    pass


def configure_django_settings_file(project_app_admin_path: str, django_app_name: str) -> None:
    """Configures the provided app name in settings.py file in project folder"""
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

# @click.command()
# @click.option('--where', default=os.getcwd(), help='Name of the new project')

# INTIAL COMMAND LOOK

default = os.getcwd()
create_initial_files(default)
create_virtual_env(default)
activate_virtual_env()
install_requirements()
django_project_name = 'need to get this from initial command'
django_project = create_django_startproject_files(default, 'django_config_creator')
django_app_name = 'need to get this from initial command'
django_app = create_django_app(django_project_name, 'django_config_creator_app')
project_app_admin_path = os.getcwd()
replace_django_settings_file(project_app_admin_path)
replace_urls_file(project_app_admin_path)
# should be django_app_name for second argument
configure_django_settings_file(project_app_admin_path, 'django_config_creator_app')