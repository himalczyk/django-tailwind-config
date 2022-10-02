# django-tailwind installation docs

https://django-tailwind.readthedocs.io/en/latest/installation.html


# configuring setuptools using pyproject.toml files

https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

# entry points

https://packaging.python.org/en/latest/specifications/entry-points/

# good readme creation for documentation

https://readme.so/

# Article helping to publish package

https://realpython.com/pypi-publish-python-package/#create-a-small-python-package


# Versioning notes

Semantic versioning is a good default scheme to use, although it’s not perfect. You specify the version as three numerical components, for instance 1.2.3. The components are called MAJOR, MINOR, and PATCH, respectively. The following are recommendations about when to increment each component:

Increment the MAJOR version when you make incompatible API changes.
Increment the MINOR version when you add functionality in a backwards compatible manner.
Increment the PATCH version when you make backwards compatible bug fixes. (Source)
You should reset PATCH to 0 when you increment MINOR, and reset both PATCH and MINOR to 0 when you increment MAJOR.