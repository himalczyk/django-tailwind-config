from statistics import multimode
import click
import os

default = os.getcwd()

@click.command()
@click.option("--params", '-m', help="Provide the django project name and app name. Example of full command: python django-tailwind-config -m example_project_name -m example_app_name", multiple=True)
def start(params):
    print(params[0], params[1])
    
if __name__ == '__main__':
    start()