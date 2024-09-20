import os
from glob import glob

license_id = '{{ cookiecutter.license_id }}'
with_click = '{{ cookiecutter.with_click }}'
with_pyinstaller = '{{ cookiecutter.with_pyinstaller }}'

if license_id != 'Unlicense':
    os.rename('LICENSE.{{ cookiecutter.license_id }}', 'LICENSE')
    os.unlink('UNLICENSE')

if license_id == 'GPL-3.0':
    os.rename('LICENSE', 'COPYING')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if with_click == 'no':
    os.unlink('src/{{ cookiecutter.project_package }}/__main__.py')
    os.unlink('tests/test_cli.py')

if with_pyinstaller == 'no':
    os.unlink('{{ cookiecutter.project_slug }}.spec')
