# Local DataOps CLI

## About this project
This is a simple CLI tool I built in Python style logic (data pipeline concept) to practice working with real-world data handling. The project reads raw data (CSV + JSON), validates it, cleans it, and then stores a processed version while logging any errors along the way.
The main idea was to simulate a small data processing pipeline like you would find in real data engineering systems.

## What the system does
- The project basically:
- Reads raw input files (study.csv and expenses.json)
- Validates each record (checks for missing or wrong data)
- Cleans and transforms valid data
- Saves clean data into a store/ folder
- Logs errors into output/errors.log
- Shows a CLI summary report (processed, valid, invalid rows, time taken)

## Project structure
- design        : UML Design
- input/        : raw data files
- store/        : cleaned JSON output
- output/       : logs (errors)
- main.py       : CLI entry point
- ingest.py     : reads and processes data
- validate.py   : data validation rules
- transform.py  : data cleaning logic
- storage.py    : saving/loading system
- report.py     : gives a report from a clean data
- query.py      : filters/search clean data
- smart.py      : it must give an insights from clean data

## How it works (simple flow)
1. User selects dataset from CLI
2. System reads file
3. Each row is validated
4. Invalid rows go to error log
5. Valid rows are transformed
6. Clean data is saved to store/
7. Summary report is displayed


## How to run it
1. Make sure Python is installed
2. Open terminal in project folder
Run: python source/main.py

## What I learned from this project
- How to structure a real project (not just scripts)
- Working with file I/O (CSV, JSON)
- Data validation logic
- Separation of concerns (ingest, validate, transform, storage)
- Building a CLI app in a clean flow
- Debugging real data errors

## Future improvements
- Add SQLite database instead of JSON storage
- Integrate Pandas for analysis
- Add data visualizations with Matplotlib
- Improve Smart Mode feature (Option 4 on the main menu)

## Notes
This project is still evolving — I mainly used it to understand how real data pipelines are structured, not just coding functions in isolation.
