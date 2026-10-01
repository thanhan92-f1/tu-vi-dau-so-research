.PHONY: validate test package

validate:
	python3 scripts/validate_skill.py .
	python3 scripts/validate_case.py examples/sample-case.json

test: validate
	python3 -m unittest discover -s tests -v

package: test
	cd .. && zip -r tu-vi-dau-so-research.zip tu-vi-dau-so-research \
		-x '*/__pycache__/*' '*.pyc' '*/.git/*' '*/.DS_Store'
