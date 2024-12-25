# Run test for code style.
lint:
	poetry run pylint user_management_py/ tests/

# Run test and and generate coverage report in xml format.
test:
	poetry run pytest --cov --cov-report=xml -v

# Build docs.
docs:
	poetry run mkdocs build

# Build and run it locally over http://127.0.0.1:8000/.
docs-online:
	poetry run mkdocs serve