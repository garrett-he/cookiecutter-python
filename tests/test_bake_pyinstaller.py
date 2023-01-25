from pytest_cookies.plugin import Cookies


def test_bake_pyinstaller(cookies: Cookies):
    result = cookies.bake(extra_context={'with_pyinstaller': 'yes', 'with_cli': 'yes'})
    assert not result.exception

    assert 'pyinstaller' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'{result.context["project_slug"]}.spec').exists()

    result = cookies.bake(extra_context={'with_pyinstaller': 'no'})
    assert not result.exception

    assert 'pyinstaller' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'{result.context["project_slug"]}.spec').exists()
