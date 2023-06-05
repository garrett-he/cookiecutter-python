from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='{{ cookiecutter.project_slug }}',
    ext_modules=cythonize([
        './src/{{ cookiecutter.project_package }}/__init__.py',
    ], language_level='3str'),
    requires=['Cython']
)
