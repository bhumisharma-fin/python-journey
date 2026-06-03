# Virtual Environment Guide

## Why?
Har project ke apne libraries = no conflicts!

## Commands (Mac/Linux)
```bash
python -m venv venv
source venv/bin/activate
pip install pandas numpy
pip freeze > requirements.txt
deactivate
```

## Commands (Windows)
```bash
python -m venv venv
venv\Scripts\activate
pip install pandas numpy
```

## For This Project
```bash
git clone https://github.com/bhumisharma-fin/python-journey
cd python-journey
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
