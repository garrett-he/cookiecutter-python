import os
from glob import glob

LICENSE_ID = '{{ cookiecutter.license_id }}'
WITH_CLI = '{{ cookiecutter.with_cli }}'
WITH_PYINSTALLER = '{{ cookiecutter.with_pyinstaller }}'

os.rename(f'LICENSE.{LICENSE_ID}', 'LICENSE')

if LICENSE_ID == 'Unlicense':
    os.rename('LICENSE', 'UNLICENSE')

if 'GPL' in LICENSE_ID:
    os.rename('LICENSE', 'COPYING')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if WITH_CLI == 'no':
    os.unlink('src/{{ cookiecutter.project_package }}/__cli__.py')
    os.unlink('src/{{ cookiecutter.project_package }}/__main__.py')
    os.unlink('tests/test_cli.py')

if WITH_PYINSTALLER == 'no':
    os.unlink('{{ cookiecutter.project_slug }}.spec')
