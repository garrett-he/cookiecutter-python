from pytest_cookies.plugin import Cookies


def test_bake_with_cli(cookies: Cookies):
    result = cookies.bake(extra_context={'with_cli': 'yes'})
    assert not result.exception

    assert 'click' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/__cli__.py').exists()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/__main__.py').exists()
    assert result.project_path.joinpath('tests/test_cli.py').exists()

    result = cookies.bake(extra_context={'with_cli': 'no'})
    assert not result.exception

    assert 'click' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/__cli__.py').exists()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/__main__.py').exists()
    assert not result.project_path.joinpath('tests/test_cli.py').exists()
