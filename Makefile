# VENV Variable Name 
VENV := venv

# DEFAULT TARGET 
all: run

create:
	python3 -m venv $(VENV)
	pip install -r requriements.txt
	. ./$(VENV)/bin/activate

# Activating VENV 
activate: 
	. ./$(VENV)/bin/activate

# Running main.py script
run: 
	./$(VENV)/bin/python3 main.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean
