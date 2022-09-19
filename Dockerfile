FROM python:3.10-slim
copy requirements.txt requirements.txt
copy *.py .
copy *.csv .
run pip install -r requirements.txt
cmd ["python", "test.py"]
