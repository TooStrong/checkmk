#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Sequence

import pytest


def pytest_addoption(parser):
    parser.addoption("--python_files", nargs="*", default=[], help="python files to check")


@pytest.fixture
def python_files(request) -> Sequence[str]:
    files = request.config.getoption("--python_files")
    if files is None:
        pytest.skip()
    return files
