from click.testing import CliRunner
from {{ cookiecutter.project_package }} import __version__
from {{ cookiecutter.project_package }}.__cli__ import main


def test_cli_version(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ['--version'])

    assert not result.exception
    assert result.output.strip() == __version__
