#!/usr/bin/make

export PYTHONPATH := $(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test-sqlite:
	rm -f sqless.db
	pythonenv/bin/python utils/build_test_db.py sqlite
	pythonenv/bin/robot --outputdir tests/reports/ tests

test-mysql:
	pythonenv/bin/python utils/build_test_db.py mysql
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests

test-postgres:
	pythonenv/bin/python utils/build_test_db.py postgres
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/* --verbose

clean:
	rm -rf python*
	rm -rf dist
	rm -rf build

PHONY: clean pythonenv test
