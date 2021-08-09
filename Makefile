lint: ## Lint code
	flake8 app/ src/ tests/ --count


format: ## Format code
	black app/ src/ tests/


pytest: ## pytest
	python -m pytest tests


pytest-coverage: ##
	python -m pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=src --cov-report=xml --cov-report=html
	open htmlcov/index.html

tag=test
build-push: ## Build Image locally, Tag, and push to Docker Hub
	docker build -t addition-model-api-test:$(tag) .
	docker tag addition-model-api-test:$(tag) shumingpeh/addition-model-api-test:$(tag)
	docker push shumingpeh/addition-model-api-test:$(tag)
