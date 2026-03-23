
# DLT Log Parser

Python tool for parsing DLT logs and generating reports.

## Features
- Parse DLT log files
- Summarize logs per module
- Export reports:
  - HTML (colored table)
  - CSV (Excel-compatible)

## Usage
python src/main.py

## Example Output
Display: {'INFO': 1, 'WARNING': 1, 'ERROR': 1}

## Technologies
- Python
- pathlib
- dataclasses

## Setup

Create virtual environment:

python -m venv venv

Activate it:

venv\Scripts\activate