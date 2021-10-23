autopush integration tests
============================

Automated tests for the autopush server.

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla-services/autopush-integration-tests/tree/master#license)


Summary
---------

A variety of tests are used to verify the integrity of [Mozilla's autopush service](https://autopush.readthedocs.io/).
This repository contains integration tests used largely for deployment verification.

Setup
---------

Create a python virtual env.

`python -m venv venv`

Activate the virtual environment

`source venv/bin/activate`

Install requirements

`pip install -r requirements.txt`


Run Tests
---------

To run the current set of tests, please use the following command:

`pytest -v --variables environments.json --env=<ENV> --api-version=<API_VERSION> tests/`

* `<ENV>` is `stage`, `production`, or `dev` depending on what
environment you are testing.

To check the rust API add the following option to the command

`--rs-api-version<RS_API_VERSION>`

Run Tests with Docker
---------------------

Pull the docker image

`docker pull mozilla-services/autopush-integration-tests:latest`

Run the test suite

`docker run autopush-integration-tests pytest -v --variables environments.json --env=<ENV> --api-version=<API_VERSION> tests/`

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/