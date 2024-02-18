VIRTUALENV_DIR ?= ./.env
PYTHON ?= python3
PIP=$(VIRTUALENV_DIR)/bin/pip
VIRTUAL_PYTHON=$(VIRTUALENV_DIR)/bin/python
VIRTUALENV_BIN=$(PYTHON) -m venv
PYPROJECT ?= pyproject.toml

all: help

.PHONY: build
build: pip  ## generate 1ma2 site
	$(VIRTUAL_PYTHON) -m 1ma2 public

.PHONY: pip
pip: $(PYPROJECT) $(PIP) ## install dependencies
	$(PIP) install -e . | tee $(VIRTUALENV_DIR)/.pip.log

.PHONY: bootstrap
bootstrap: $(VIRTUALENV_DIR)  ## set up virtual env

.PHONY: clean
clean:  ## reset checkout, clear virtual environment
	rm -rf $(VIRTUALENV_DIR)
	touch $(PYPROJECT)

$(PIP): $(VIRTUALENV_DIR)
$(VIRTUAL_PYTHON): $(VIRTUALENV_DIR)

$(VIRTUALENV_DIR):
	$(VIRTUALENV_BIN) $(VIRTUALENV_DIR)

# via https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## List tasks with documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
