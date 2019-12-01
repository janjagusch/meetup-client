# meetup-client

[![Build Status](https://travis-ci.org/janjagusch/meetup-client.svg?branch=master)](https://travis-ci.org/janjagusch/meetup-client) [![codecov](https://codecov.io/gh/janjagusch/meetup-client/branch/master/graph/badge.svg)](https://codecov.io/gh/janjagusch/meetup-client)

A Python client for the [Meetup API](https://www.meetup.com/meetup_api/) that supports [OAuth 2](https://www.meetup.com/meetup_api/auth/#oauth2) authentification.

## Installation

### Dependencies

For more information, please take a look at the `tool.poetry.dependencies` section in `pyproject.toml`.

### User Installation

#### PIP

```
pip install meetup-client
```

#### Poetry

```
poetry add meetup-client
```

## Getting Started

**Note**: meetup-client only supports OAuth 2 authentification with server flow without user credentials. To create an access token, follow the instructions [here](https://www.meetup.com/meetup_api/auth/#oauth2).

Next, you can create a `MeetupClient` instance as follows:

```python
from meetup_api.client import MeetupClient

meetup_client = MeetupClient(
    access_token=<YOUR ACCESS TOKEN>,
)
```

## Examples

Please take a look at the [examples](notebooks/examples.py). You can convert this into a Jupyter notebook, using [jupytext](https://github.com/mwouts/jupytext).

## Changelog

Please take a look at the [CHANGELOG.md](CHANGELOG.md) for notable changes to meetup-client.

## License

See the [LICENSE](LICENSE) for details.

## Development

We welcome new contributions to this project!

### Source Code

You can check the latest source code with the command:

```
git clone git@github.com:janjagusch/meetup-client.git
```

### Dependencies

Please take a look at `tool.poetry.dev-dependencies` in `pyproject.toml`.

### Linting

After cloning and installing the dependencies, you can lint the project by executing:

```
make lint
```

### Testing

After cloning and installing the dependencies, you can test the project by executing:

```
make test
```

## Help and Support

### Authors

- Jan-Benedikt Jagusch <jan.jagusch@gmail.com>
