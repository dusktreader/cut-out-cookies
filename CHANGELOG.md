# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## v0.3.0 - 2023-08-14
- Added support for Jinja 3
- Added noxfile for matrix testing across multiple versions of python and jinja2.

## v0.2.0 - 2021-05-06
- Removed `null` filter
- Adjusted `stencil_path` to render with a special prefix instead of resolving to `None`
- Updated unit tests

## v0.1.3 - 2021-04-19
- Updated documentation

## v0.1.2 - 2021-04-16
- Added tool for cleanup in post-build hook
- See this issue for motive: https://github.com/cookiecutter/cookiecutter/issues/1518

## v0.1.1 - 2021-04-16
- Added more metadata to pyproject.toml

## v0.1.0 - 2021-04-16
- Initial release of cut-out-cookies
- Added jinja filtes `stencil`, `null`, and `stencil_path`
- Added a README.md file
- Included unit tests
- Configured black code formatting
- Configured isort import ordering
- Created pre-commit hook for black and isort
- Added a README and this CHANGELOG
