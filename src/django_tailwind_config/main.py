"""Installable package to create working django app + project, django-tailwind config and virtual environment creation"""


import os
import platform
import shutil
from venv import create
import click
import sys


class djangoTailwindConfig():
    
    def __init__(self, target_directory):
        self.target_directory = target_directory
    

    def create_initial_files(self, target_directory: str) -> None:
        """Copies the initial files that need to be at top level of project directory"""
        shutil.copy2('files/.gitignore', os.path.join(target_directory, '.gitignore'))
        shutil.copy2('files/README.md', os.path.join(target_directory, 'README.md'))
        shutil.copy2('files/requirements.txt', os.path.join(target_directory, 'requirements.txt'))
        pass
    
    
    def is_venv(self):
        return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


    # def create_virtual_env(self, target_directory: str) -> str:
    #     """Creates and activates the virtual env"""
    #     os.chdir(target_directory)
    #     os.system('cmd /c "python -m venv venv_test"')
    #     return target_directory


    # def activate_virtual_env(self, target_directory: str) -> None:
    #     """Activate venv"""
    #     os.system('cmd /c python --version')
    #     os.system('cmd /c virtualenv --version')
    #     os.system('cmd /c cd')
    #     os.system('cmd /c dir')
    #     os.chdir("venv_test\Scripts")
    #     os.system('cmd /c dir')
    #     os.system(f'cmd /c activate && pip -V && cd {target_directory} && pip install -r requirements.txt')
    #     os.system('cmd /c pip -V')
    #     os.chdir(target_directory)
    #     subprocess.run('pip install -r requirements.txt')
    #     pass


    def install_requirements(self) -> None:
        """Install requirements
            Installing: django, django-tailwind
        """
        os.system('cmd /c "pip install -r requirements.txt"')
        pass


    def create_django_startproject_files(self, target_directory: str, django_project_name: str) -> str:
        """Runs django-startproject command"""
        os.chdir(target_directory)
        os.system(f'cmd /c "django-admin startproject {django_project_name}"')
        return django_project_name


    def create_django_app(self, project_directory_name: str, django_app_name: str, root_path: str) -> str:
        """Creates the django app folder inside of the django project directory"""
        os.chdir(f"{root_path}\{project_directory_name}")
        os.system('cmd /c dir')
        os.system(f'python manage.py startapp {django_app_name}')
        return django_app_name


    def replace_django_settings_file(self, project_app_admin_path: str, root_path: str, django_project_name: str) -> None:
        """Configures the project -> project_folder -> settings.py file with tailwind and new created app name"""
        shutil.copy2(f"{root_path}\\files\settings.py", os.path.join(f"{project_app_admin_path}\{django_project_name}", 'settings.py'))
        pass
        
        
    def replace_urls_file(self, project_app_admin_path: str, root_path:str, django_project_name: str) -> None:
        """Configures the urls.py for django-tailwind"""
        shutil.copy2(f"{root_path}\\files\\urls.py", os.path.join(f"{project_app_admin_path}\{django_project_name}", 'urls.py'))
        pass


    def configure_django_settings_file(self, project_app_admin_path: str, django_app_name: str, django_project_name: str) -> None:
        """Configures the provided app name in settings.py file in project folder"""
        os.chdir(f"{project_app_admin_path}\{django_project_name}")
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
@click.command()
@click.option("--params", '-m', help="Provide the django project name and app name. Example of full command: python django-tailwind-config -m example_project_name -m example_app_name", multiple=True)
def start(params):
    root_path = os.getcwd()
    configure = djangoTailwindConfig(root_path)
    configure.create_initial_files(root_path)
    # root_directory = configure.create_virtual_env(root_path)
    # configure.activate_virtual_env(root_directory)
    if configure.is_venv():
        configure.install_requirements()
        django_project_name = params[0]
        django_project = configure.create_django_startproject_files(root_path, django_project_name)
        django_app_name = params[1]
        django_app = configure.create_django_app(django_project, django_app_name, root_path)
        project_app_admin_path = os.getcwd()
        configure.replace_django_settings_file(project_app_admin_path, root_path, django_project)
        configure.replace_urls_file(project_app_admin_path, root_path,  django_project)
        # should be django_app_name for second argument
        configure.configure_django_settings_file(project_app_admin_path, 'django_config_creator_app', django_project)
    else:
        print("You have not created a virtual environment. Please create and activate it to install this package inside.\n\n More info on: https://docs.python.org/3/library/venv.html\n\n Virtual environments allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation.")
        
if __name__ == '__main__':
    start()