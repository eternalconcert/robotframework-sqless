#!/usr/bin/make

export PYTHONPATH := "$(PYTHONPATH):./src/

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test:
	rm -f sqless.db
	pythonenv/bin/python utils/build_test_db.py
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
