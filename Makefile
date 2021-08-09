lint: ## Lint code
	flake8 app/ src/ tests/ --count


format: ## Format code
	black app/ src/ tests/


pytest: ## pytest
	python -m pytest tests


pytest-coverage: ##
	python -m pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=src --cov-report=xml --cov-report=html
	open htmlcov/index.html
