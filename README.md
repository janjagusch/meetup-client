# meetup-client

[![Build Status](https://travis-ci.org/janjagusch/meetup-client.svg?branch=master)](https://travis-ci.org/janjagusch/meetup-client)

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

**Note**: meetup-client curently only supports OAuth 2 authentification with server flow without user credentials.

Before you can use the client, you need to either [register](https://secure.meetup.com/meetup_api/oauth_consumers/create/) a new OAuth consumer or add a redirect_uri to your existing consumer by clicking the edit link next to you consumer's [listing](https://secure.meetup.com/meetup_api/oauth_consumers/) ([more information](https://www.meetup.com/meetup_api/auth/#oauth2)).

Next, you can create a `MeetupClient` instance as follows:

```python
from meetup_api.client import MeetupClient

meetup_client = MeetupClient(
    consumer_key=<YOUR CONSUMER KEY>,
    consumer_secret=<YOUR CONSUMER SECRET>,
    redirect_uri=<YOUR CONSUMER REDIRECT URI>,
)
```

The program will then prompt instructions in the console:

1. Navigate to a specified url in a browser.
1. Copy the value of the `code` parameter in the redirected url.
1. Paste the code into the console.

**Note**: If you call the `MeetupClient` constructor with the `code` or `access_token` argument, the previous step will be omitted.

You can also define the client scope, using the `scopes` argument. Valid scopes are defined [here](https://www.meetup.com/meetup_api/auth/#oauth2) under the section "Permission Scopes".

**Advice**: Use the 'ageless' scope to create an access token valid for two weeks. Then persist the token and pass it to the `MeetupClient` constructor as `access_token` argument. This way, you do not have to manually paste the code value into the console for every constructor call.

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
