import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        dest="env",
        default="stage",
        help="Environment tests are running in: dev | stage | prod",
    )
    parser.addoption(
        "--api-version",
        dest="apiversion",
        default="0.0.0",
        help="Version of the autopush service API we are testing against",
    )
    parser.addoption(
        "--rs-api-version",
        dest="rsapiversion",
        default="0.0.0",
        help="Version of the autopush-rs API we are testing against",
    )


@pytest.fixture()
def env(request):
    return request.config.getoption("--env")


@pytest.fixture()
def api_version(request):
    return request.config.getoption("--api-version")


@pytest.fixture()
def rs_api_version(request):
    return request.config.getoption("--rs-api-version")