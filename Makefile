.PHONY: test

test:
	py.test test --cov --cov-config=.coveragerc
