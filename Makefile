# VENV Variable Name 
VENV := venv

# DEFAULT TARGET 
all: run

build:
	python3 -m venv $(VENV)
	pip install -r requriements.txt
	mkdir figures
	. ./$(VENV)/bin/activate

# Activating VENV - DOES NOT WORK 
activate: 
	. ./sourceVenv.sh 	

# Send an Email using GMAIL STMP
email:
	./$(VENV)/bin/python3 gmail.py 

# Running main.py script
run: 
	./$(VENV)/bin/python3 main.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean
