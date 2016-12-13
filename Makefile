.PHONY: test

test:
	py.test test --cov --cov-config=.coveragerc

test_fix:
	COV_CORE_SOURCE=demo COV_CORE_DATAFILE=.coverage.plugin py.test test --cov --cov-config=.coveragerc
