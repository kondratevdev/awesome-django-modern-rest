.PHONY: help
help: ## Show the help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: lint
lint: ## Run linting checks
	awesome-lint README.md
	awesome_bot README.md

.PHONY: toc
toc: ## Run ToC generation
	doctoc README.md

.PHONY: test
test: toc lint  ## Run all tests
