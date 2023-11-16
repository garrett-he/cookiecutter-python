from pytest_cookies.plugin import Cookies


def test_bake_pyinstaller(cookies: Cookies):
    result = cookies.bake(extra_context={'with_pyinstaller': 'yes', 'with_cli': 'yes', 'with_gui': 'yes'})
    assert not result.exception

    assert 'pyinstaller' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'{result.context["project_slug"]}-cli.spec').exists()
    assert result.project_path.joinpath(f'{result.context["project_slug"]}-gui.spec').exists()
    assert f'poetry run pyinstaller {result.context["project_slug"]}-cli.spec' in result.project_path.joinpath('Makefile').read_text()
    assert f'poetry run pyinstaller {result.context["project_slug"]}-gui.spec' in result.project_path.joinpath('Makefile').read_text()

    result = cookies.bake(extra_context={'with_pyinstaller': 'no'})
    assert not result.exception

    assert 'pyinstaller' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'{result.context["project_slug"]}-cli.spec').exists()
    assert not result.project_path.joinpath(f'{result.context["project_slug"]}-gui.spec').exists()
    assert f'poetry run pyinstaller {result.context["project_slug"]}-cli.spec' not in result.project_path.joinpath('Makefile').read_text()
    assert f'poetry run pyinstaller {result.context["project_slug"]}-gui.spec' not in result.project_path.joinpath('Makefile').read_text()
