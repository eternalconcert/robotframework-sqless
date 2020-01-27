#!/usr/bin/make

export PYTHONPATH := $(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test-sqlite:
	rm -f sqless.db
	cat tests/sqlite.yml > tests/schema.yml
	pythonenv/bin/python utils/build_test_db.py sqlite
	pythonenv/bin/robot --outputdir tests/reports/ tests
	rm -f tests/schema.yml

test-mysql:
	cat tests/mysql.yml > tests/schema.yml
	pythonenv/bin/python utils/build_test_db.py mysql
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests
	rm -f tests/schema.yml

test-postgres:
	cat tests/postgres.yml > tests/schema.yml
	pythonenv/bin/python utils/build_test_db.py postgres
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests
	rm -f tests/schema.yml

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/* --verbose

clean:
	rm -rf python*
	rm -rf dist
	rm -rf build

PHONY: clean pythonenv test
