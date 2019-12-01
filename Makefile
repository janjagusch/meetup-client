## downloading pylintrc
pylintrc_download:
	@echo "Downloading .pylintrc ..."
	@wget -O .pylintrc https://gitlab.com/InstaffoOpenSource/pylintrc/raw/master/.pylintrc

## deleting all Python garbage
clean:
	@echo "Cleaning up ..."
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +

## testing for missing __init__.py
test_missing_init: clean
	@echo "Testing for missing __init__.py ..."
	@poetry run python bin/test_missing_init

## tox testing
test_tox: test_missing_init
	@echo "Tox testing ..."
	@poetry run tox

## testing
test: test_tox

## black formatting
format_black: test_missing_init
	@echo "Black formatting ..."
	@poetry run black .

## prettier formatting
format_prettier:
	@echo "Prettier formatting ..."
	@npx prettier --write $$(find \( -name "*.yml" -o -name "*.yaml" -o -name "*.json" \) -not \( -path "./.venv/*" -o -path "./.tox/*" \))
	
## formatting
format: format_black format_prettier

## black linting
lint_black: test_missing_init
	@echo "Black linting ..."
	@poetry run black --check .

## prettier formatting
lint_prettier:
	@echo "Prettier linting ..."
	@npx prettier --check $$(find \( -name "*.yml" -o -name "*.yaml" -o -name "*.json" \) -not \( -path "./.venv/*" -o -path "./.tox/*" \))

## pylint linting
lint_pylint: test_missing_init
	@echo "Pylint linting ..."
	@poetry run pylint meetup_client
	@poetry run pylint $$(find tests/ -iname "*.py")

## linting
lint: lint_black lint_prettier lint_pylint

## installing Jupyter kernel
jupyter_install_kernel:
	@echo "Installing Jupyter kernel ..."
	@bin/install_kernel

# uninstalling Jupyter kernel
jupyter_uninstall_kernel:
	@echo "Uninstalling Jupyter kernel ..."
	@bin/uninstall_kernel
