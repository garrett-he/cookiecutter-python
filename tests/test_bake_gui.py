from pytest_cookies.plugin import Cookies


def test_bake_with_gui(cookies: Cookies):
    result = cookies.bake(extra_context={'with_gui': 'yes'})
    assert not result.exception

    assert 'wxpython' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/__gui__.py').exists()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/__init__.py').exists()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/app.py').exists()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/frames/__init__.py').exists()
    assert result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/frames/main_frame.py').exists()

    result = cookies.bake(extra_context={'with_gui': 'no'})
    assert not result.exception

    assert 'wxpython' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/__gui__.py').exists()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/__init__.py').exists()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/app.py').exists()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/frames/__init__.py').exists()
    assert not result.project_path.joinpath(f'src/{result.context["project_package"]}/gui/frames/main_frame.py').exists()
