.PHONY: help build test lint docker deploy clean

IMAGE ?= example/app
TAG ?= $(shell git rev-parse --short HEAD)

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  %-12s %s\n", $$1, $$2}'

build: ## Build the application
	npm ci && npm run build

test: ## Run the test suite
	npm test

lint: ## Lint sources
	npm run lint

docker: ## Build the container image
	docker build -t $(IMAGE):$(TAG) .

deploy: docker ## Deploy the current commit
	./devops/scripts/deploy.sh $(TAG)

clean: ## Remove build artifacts
	rm -rf dist coverage
