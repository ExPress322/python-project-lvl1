install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl
re:
	pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall
lint:
	poetry run flake8 brain_games