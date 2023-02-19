# cookiecutter-python

![license](https://img.shields.io/github/license/garrett-he/cookiecutter-python)
![version](https://img.shields.io/badge/version-1.0.0-blue)
![build](https://img.shields.io/github/actions/workflow/status/garrett-he/cookiecutter-python/ubuntu-jammy.yml)

A Cookiecutter template for Python packages.

## Features

The template is integrated with:

- [pytest][pytest]: Testing runner.
- [pylint][pylint]: Static code analyser.
- [pre-commit][pre-commit]: Git `pre-commit` hook manager.
- [tox][tox]: Setup multiple testing environments.
- [github-actions][github-actions]: GitHub Actions.
- [click][click]: Command-line interface framework (optional).
- [pyinstaller][pyinstaller]: Python application bundler (optional).

## Quickstart

1. Install the latest Cookiecutter via command:
   ```
   pip install --user --upgrade cookiecutter
   ```

2. Use command `cookiecutter` to generate a new project:
   ```
   cookiecutter gh:garrett-he/cookiecutter-python
   ```

## License

Copyright (C) 2023 Garrett HE <garrett.he@hotmail.com>

The BSD 3-Clause License, see [LICENSE](./LICENSE).


[pytest]: https://pytest.org

[pylint]: https://pypi.org/project/pylint/

[pre-commit]: https://pre-commit.com/

[tox]: https://tox.wiki

[github-actions]: https://docs.github.com/en/actions

[click]: https://click.palletsprojects.com

[pyinstaller]: https://pyinstaller.org
