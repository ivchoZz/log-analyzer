# Log Analyzer

A simple command-line tool that analyzes log files and generates a report with error/warning counts, the most common message, and level percentages.

## Features

- Counts ERROR and WARNING occurrences
- Finds the most frequently repeated log message
- Calculates percentage breakdown by log level (ERROR/WARNING/INFO)
- Optionally saves the report to a file
- Handles missing or empty log files gracefully

## Requirements

- Python 3
- pytest (for running tests)

Install dependencies:

    pip install -r requirements.txt

## Usage

Analyze a log file and print the report to the console:

    python analyzer.py server.log

Analyze a log file and save the report to a file:

    python analyzer.py server.log -o report.txt

## Example

## Given a log file with entries like:
    2026-08-19 10:19:15 INFO User logged in
    2026-08-19 10:20:02 ERROR Database connection failed
    2026-08-19 10:20:45 WARNING High memory usage
    2026-08-19 10:21:10 ERROR Timeout on request
    2026-08-19 10:22:00 INFO Server started
    2026-08-19 11:20:02 ERROR Database connection failed

The tool outputs:
    === Log Analysis Report ===
    Total lines: 6
    Errors: 3
    Warnings: 1
    Most common message: Database connection failed
    INFO: 33.33%
    ERROR: 50.00%
    WARNING: 16.67%
    
## Running Tests

    pytest test_analyzer.py

## Project Structure

    log-analyzer/
    ├── analyzer.py          # Main script
    ├── test_analyzer.py     # Unit tests
    ├── requirements.txt     # Dependencies
    ├── server.log           # Sample log file
    └── README.md

