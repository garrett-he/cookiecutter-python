rmdir /s /q build
rmdir /s /q dist

{% if cookiecutter.with_cython == 'yes' %}
poetry run python setup.py build_ext --build-lib build
copy .\src\audiofoundry_duration\__main__.py .\build\audiofoundry_duration\
{% endif %}

poetry run pyinstaller audiofoundry-duration.spec
copy .\CHANGELOG.md .\dist\CHANGELOG.md
copy .\COPYING .\dist\COPYING
copy .\README.md .\dist\README.md
