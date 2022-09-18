FROM python:3.8-slim-buster
copy requirements.txt requirements.txt
copy *.py .
copy *.csv .
run pip install -r requirements.txt
cmd ["python", "test.py"]
