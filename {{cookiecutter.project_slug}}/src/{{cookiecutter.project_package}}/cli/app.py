import click

from {{cookiecutter.project_package}} import __version__
from {{cookiecutter.project_package}}.cli.commands import command_group

def print_version(ctx: click.Context, _, value: str):
    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()


@click.group(commands=command_group)
@click.option('--version', help='Show version information.', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def main():
    """{{ cookiecutter.project_description }}"""


if __name__ == '__main__':
    main()
