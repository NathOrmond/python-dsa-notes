# DSA Learning Project Makefile

# Load environment variables if .env exists
ifneq (,$(wildcard .env))
    include .env
    export
endif

.PHONY: help install test test-all check-status benchmark clean setup

# Default target
help:
	@echo "DSA Learning Project - Available Commands:"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install     - Install dependencies"
	@echo "  make setup       - Complete project setup"
	@echo ""
	@echo "Testing:"
	@echo "  make test        - Run all tests"
	@echo "  make test-easy   - Run easy problem tests"
	@echo "  make test-medium - Run medium problem tests"
	@echo "  make test-hard   - Run hard problem tests"
	@echo "  make test-two-sum - Run two_sum specific tests"
	@echo ""
	@echo "Status & Progress:"
	@echo "  make status      - Check solution implementation status"
	@echo "  make status-all  - Check all problems with details"
	@echo ""
	@echo "Performance:"
	@echo "  make benchmark   - Benchmark all problems"
	@echo "  make benchmark-two-sum - Benchmark two_sum specifically"
	@echo ""
	@echo "Development:"
	@echo "  make create-problem DIFFICULTY=easy NAME=problem_name - Create new problem"
	@echo "  make clean        - Clean up cache and temporary files"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Run linting checks"

# Installation
install:
	pip install -r requirements.txt

setup: install
	@echo "✅ Project setup complete!"
	@echo "Run 'make status' to check your progress"

# Testing
test:
	python -m pytest tests/ -v

test-easy:
	python -m pytest tests/problems/easy/ -v

test-medium:
	python -m pytest tests/problems/medium/ -v

test-hard:
	python -m pytest tests/problems/hard/ -v

test-two-sum:
	python -m pytest tests/problems/easy/test_two_sum.py -v

# Status checking
status:
	python scripts/check_solutions.py

status-all:
	python scripts/check_solutions.py --all

# Performance benchmarking
benchmark:
	python scripts/benchmark.py --all

benchmark-two-sum:
	python scripts/benchmark.py --problem easy/two_sum

# Development tools
create-problem:
	@if [ -z "$(DIFFICULTY)" ] || [ -z "$(NAME)" ]; then \
		echo "❌ Usage: make create-problem DIFFICULTY=easy NAME=problem_name"; \
		exit 1; \
	fi
	python scripts/create_problem.py $(DIFFICULTY) $(NAME)

# Code quality
format:
	black src/ tests/ scripts/

lint:
	python -m flake8 src/ tests/ scripts/

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

clean-cache:
	@echo "🗑️  Removing Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cache cleanup complete"

setup-cache:
	@echo "📁 Setting up centralized cache directory..."
	@mkdir -p .cache/python
	@echo "✅ Cache directory created at .cache/python"
	@echo "💡 To use centralized cache, run: export PYTHONPYCACHEPREFIX=.cache/python"

setup-env:
	@echo "⚙️  Setting up environment configuration..."
	@if [ ! -f .env ]; then \
		cp env.example .env; \
		echo "✅ Created .env from env.example"; \
		echo "💡 Edit .env to customize your settings"; \
	else \
		echo "⚠️  .env already exists, skipping..."; \
	fi

setup-grind75:
	@echo "🚀 Setting up Grind 75 problems..."
	@python scripts/generate_grind75.py

# Learning workflow shortcuts
learn-two-sum: status
	@echo "📚 Learning Two Sum Problem:"
	@echo "1. Read: cat src/problems/easy/two_sum/two_sum.md"
	@echo "2. Implement: Edit src/problems/easy/two_sum/solutions/solution_1.py"
	@echo "3. Test: make test-two-sum"
	@echo "4. Check: make status"

progress:
	@echo "📊 Your Learning Progress:"
	@python scripts/check_solutions.py
	@echo ""
	@echo "🎯 Next Steps:"
	@echo "- Implement solutions marked as 'Not Implemented'"
	@echo "- Run tests after each implementation"
	@echo "- Use 'make benchmark' to compare performance"
