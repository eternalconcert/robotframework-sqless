#!/usr/bin/make

export PYTHONPATH := "$(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test:
	rm -f sqless.db
	pythonenv/bin/python utils/build_test_db.py
	pythonenv/bin/robot --outputdir reports/ tests

clean:
	rm -rf python*
	rm -rf dist
	rm -rf build

PHONY: clean pythonenv test
