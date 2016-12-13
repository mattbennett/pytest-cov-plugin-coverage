pytest-cov doesn't cover the import of other plugins installed via setuptools entrypoints.

# steps to reproduce

1. git clone git@github.com:mattbennett/pytest-cov-plugin-coverage.git
2. cd pytest-cov-plugin-coverage
3. pip install -e .[dev]
4. make test

# plugin
```
# plugin.py
import pytest


@pytest.fixture
def one():
    return 1


@pytest.fixture
def zero():
    return 0
```

# test
```
from demo.app import foo

def test_true(one):
    assert foo(one) is True


def test_false(zero):
    assert foo(zero) is False
```

# output
```
$ make test
py.test test --cov --cov-config=.coveragerc
========================================================= test session starts =========================================================
platform darwin -- Python 2.7.10, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
rootdir: /Users/mattbennett/Code/proj, inifile:
plugins: demo-0.0.1, cov-2.4.0
collected 3 items

test/test_app.py ...

---------- coverage: platform darwin, python 2.7.10-final-0 ----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
demo/__init__.py       0      0   100%
demo/app.py            4      0   100%
demo/plugin.py         5      3    40%   1-4, 9
------------------------------------------------
TOTAL                  9      3    67%

FAIL Required test coverage of 100% not reached. Total coverage: 66.67%
```
