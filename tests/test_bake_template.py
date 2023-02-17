import random
import toml
from glob import glob

from chance import chance
from pytest_cookies.plugin import Cookies

license_stubs = {
    'Apache-2.0': 'Apache License',
    'BSD-3-Clause': 'BSD 3-Clause License',
    'GPL-3.0': 'GNU General Public License',
    'LGPL-3.0': 'GNU Lesser General Public License',
    'MIT': 'MIT License',
    'MPL-2.0': 'Mozilla Public License'
}


def generate_context() -> dict:
    return {
        'project_name': f'{chance.word().capitalize()} {chance.word().capitalize()}',
        'project_slug': f'{chance.word().lower()}-{chance.word().lower()}',
        'project_package': f'{chance.word().lower()}_{chance.word().lower()}',
        'project_description': chance.sentence(),
        'project_version': f'{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}',
        'project_keywords': f'{chance.word()},{chance.word()},{chance.word()}',
        'author_name': chance.name(),
        'author_email': chance.email(),
        'license_id': chance.pickone([key for key in license_stubs.keys()]),
        'license_fullname': f'{chance.name()} <{chance.email()}>',
        'license_year': str(random.randint(2000, 2023)),
        'github_path': f'{chance.word()}/{chance.word()}-{chance.word()}'.lower(),
        'python_version': chance.pickone(['3.7', '3.8', '3.9', '3.10', '3.11'])
    }


def test_bake_license(cookies: Cookies):
    for license_id, license_stub in license_stubs.items():
        context = generate_context()
        context['license_id'] = license_id

        result = cookies.bake(extra_context=context)
        assert not result.exception

        license_text = result.project_path.joinpath('LICENSE').read_text(encoding='utf-8')
        assert license_stub in license_text

        assert len(glob('LICENSE.*')) == 0
        assert not result.project_path.joinpath('UNLICENSE').exists()

        if license_id in ['BSD-3-Clause', 'MIT']:
            assert context['license_fullname'] in license_text
            assert context['license_year'] in license_text

        readme = result.project_path.joinpath('README.md').read_text(encoding='utf-8')

        assert context['project_name'] in readme
        assert context['project_description'] in readme

        assert f'Copyright (C) {context["license_year"]} {context["license_fullname"]}' in readme
        assert license_stubs[context['license_id']] in readme
        assert 'see [LICENSE](./LICENSE)' in readme

    context = generate_context()
    context['license_id'] = 'Unlicense'
    result = cookies.bake(extra_context=context)
    assert not result.exception
    assert len(glob('LICENSE.*')) == 0
    assert not result.project_path.joinpath('LICENSE').exists()

    unlicense_text = result.project_path.joinpath('UNLICENSE').read_text(encoding='utf-8')
    assert 'This is free and unencumbered software released into the public domain' in unlicense_text
    assert context['license_fullname'] not in unlicense_text
    assert context['license_year'] not in unlicense_text

    readme = result.project_path.joinpath('README.md').read_text(encoding='utf-8')
    assert 'This is free and unencumbered software released into the public domain' in readme
    assert 'see [UNLICENSE](./UNLICENSE)' in readme


def test_bake_pyproject(cookies: Cookies):
    context = generate_context()
    result = cookies.bake(extra_context=context)
    assert not result.exception

    with result.project_path.joinpath('pyproject.toml').open('r', encoding='utf-8') as fp:
        pyproject = toml.load(fp)

    assert pyproject['tool']['poetry']['name'] == context['project_slug']
    assert pyproject['tool']['poetry']['version'] == context['project_version']
    assert pyproject['tool']['poetry']['description'] == context['project_description']
    assert pyproject['tool']['poetry']['authors'] == [f'{context["author_name"]} <{context["author_email"]}>']
    assert pyproject['tool']['poetry']['license'] == context['license_id']
    assert pyproject['tool']['poetry']['homepage'] == f'https://github.com/{context["github_path"]}'
    assert pyproject['tool']['poetry']['repository'] == f'https://github.com/{context["github_path"]}.git'
    assert pyproject['tool']['poetry']['keywords'] == context['project_keywords'].split(',')
    assert pyproject['tool']['poetry']['packages'] == [{'include': context['project_package'], 'from': 'src'}]
    assert pyproject['tool']['poetry']['dependencies']['python'] == context['python_version']


def test_bake_package(cookies: Cookies):
    result = cookies.bake()
    assert not result.exception

    package = result.project_path.joinpath(f'src/{result.context["project_package"]}')
    assert package.exists()


def test_bake_with_click(cookies: Cookies):
    result = cookies.bake(extra_context={'with_click': 'yes'})
    assert not result.exception

    assert 'click' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/__main__.py').exists()
    assert result.project_path.joinpath('tests/test_cli.py').exists()

    result = cookies.bake(extra_context={'with_click': 'no'})
    assert not result.exception

    assert 'click' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/__main__.py').exists()
    assert not result.project_path.joinpath('tests/test_cli.py').exists()


def test_bake_pyinstaller(cookies: Cookies):
    result = cookies.bake(extra_context={'with_pyinstaller': 'yes'})
    assert not result.exception

    assert 'pyinstaller' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'{result.context["project_slug"]}.spec').exists()

    result = cookies.bake(extra_context={'with_pyinstaller': 'no'})
    assert not result.exception

    assert 'pyinstaller' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'{result.context["project_slug"]}.spec').exists()
