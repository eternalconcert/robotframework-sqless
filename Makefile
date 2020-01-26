#!/usr/bin/make

export PYTHONPATH := $(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test-sqlite:
	rm -f sqless.db
	cat sqlite.yml > schema.yml
	pythonenv/bin/python utils/build_test_db.py sqlite
	pythonenv/bin/robot --outputdir reports/ tests

test-mysql:
	cat mysql.yml > schema.yml
	pythonenv/bin/python utils/build_test_db.py mysql
	pythonenv/bin/robot --outputdir reports/ tests

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/* --verbose

clean:
	rm -rf python*
	rm -rf dist
	rm -rf build

PHONY: clean pythonenv test
