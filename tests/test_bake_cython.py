from pytest_cookies.plugin import Cookies


def test_bake_cython(cookies: Cookies):
    result = cookies.bake(extra_context={'with_pyinstaller': 'yes', 'with_cli': 'yes', 'with_cython': 'yes'})
    assert not result.exception

    assert 'cython' in result.project_path.joinpath('pyproject.toml').read_text()
    assert 'poetry run python setup.py build_ext --build-lib build' in result.project_path.joinpath('Makefile').read_text()

    result = cookies.bake(extra_context={'with_cython': 'no'})
    assert not result.exception

    assert 'cython' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert 'poetry run python setup.py build_ext --build-lib build' not in result.project_path.joinpath('Makefile').read_text()
