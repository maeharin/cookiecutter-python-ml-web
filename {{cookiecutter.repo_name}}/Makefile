.PHONY: pyenv clean data requirements

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYENV_NAME = env_{{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = python3
PYTHON_VERSION = 3.6.5
PYTHON_PATH = .

# insall pyenv only if not exists. and activate
pyenv:
	@[ ! -e ~/.pyenv/versions/$(PYENV_NAME) ] && pyenv virtualenv $(PYTHON_VERSION) $(PYENV_NAME) || :
	pyenv local $(PYENV_NAME)

# Install Python Dependencies
requirements:
	pip install -U pip setuptools wheel
	pip install -r requirements.txt

app:
	PYTHONPATH=$(PYTHON_PATH) $(PYTHON_INTERPRETER) src/app/app.py

data:
	PYTHONPATH=$(PYTHON_PATH) $(PYTHON_INTERPRETER) src/data/make_dataset.py

feature:
	PYTHONPATH=$(PYTHON_PATH) $(PYTHON_INTERPRETER) src/features/build_features.py

train:
	PYTHONPATH=$(PYTHON_PATH) $(PYTHON_INTERPRETER) src/models/train_model.py

predict:
	PYTHONPATH=$(PYTHON_PATH) $(PYTHON_INTERPRETER) src/models/predict_model.py

# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

dockerbuild: clean
	docker build -t {{ cookiecutter.repo_name }} .

dockerrun:
	docker run --rm -p 80:8000 {{ cookiecutter.repo_name }}

