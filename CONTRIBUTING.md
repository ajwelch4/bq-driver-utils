# Contributing

## Requirements

- [Poetry][poetry] (analyze, test)
- [npm][npm] (analyze)
- [addlicense][addlicense] (analyze)

## Install

```shell
poetry install
```

## Analyze (format, lint, type check)

```shell
poetry shell
nox -t analyze
```

## Test

### Unit

```shell
poetry shell
nox -s tests -- unit
```

### Integration

```shell
poetry shell
nox -s tests -- integration
```

### Unit and Integration

```shell
poetry shell
nox -s tests
```

### Logs

To view all logs while running tests:

```shell
poetry shell
nox -s tests --verbose -- unit pytest_verbose
```

## Docs

Be sure to update the [README](./README.md) if necessary.

<!-- markdownlint-disable line-length -->

[poetry]: https://python-poetry.org/docs/#installation
[npm]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
[addlicense]: https://github.com/google/addlicense
