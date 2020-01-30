#!/usr/bin/make

export PYTHONPATH := $(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test-sqlite:
	rm -f sqless.db
	cat tests/config/sqlite.yml > tests/config/db_config.yml
	pythonenv/bin/python utils/build_test_db.py sqlite
	pythonenv/bin/robot --outputdir tests/reports/ tests
	rm -f tests/config/db_config.yml

test-mysql:
	cat tests/config/mysql.yml > tests/config/db_config.yml
	pythonenv/bin/python utils/build_test_db.py mysql
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests
	rm -f tests/config/db_config.yml

test-postgres:
	cat tests/config/postgres.yml > tests/config/db_config.yml
	pythonenv/bin/python utils/build_test_db.py postgres
	pythonenv/bin/robot -i all_dbms --outputdir tests/reports/ tests
	rm -f tests/config/db_config.yml

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/* --verbose

clean:
	rm -rf python*
	rm -rf dist
	rm -rf build

PHONY: clean pythonenv test
