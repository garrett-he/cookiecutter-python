import os
import shutil
from glob import glob

license_id = '{{ cookiecutter.license_id }}'
with_cli = '{{ cookiecutter.with_cli }}'

os.rename(f'LICENSE.{license_id}', 'LICENSE')

if license_id == 'Unlicense':
    os.rename('LICENSE', 'UNLICENSE')

if 'GPL' in license_id:
    os.rename('LICENSE', 'COPYING')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if with_cli == 'no':
    os.unlink('src/{{ cookiecutter.project_package }}/__cli__.py')
    shutil.rmtree('src/{{ cookiecutter.project_package }}/cli')
    os.unlink('tests/test_cli.py')
