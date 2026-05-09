Local DataOps CLI

This is a command-line project that processes study and expense data. It takes raw files, cleans and validates the data, stores it locally in a structured format, and then generates simple reports and queries.

What the project does:
•	Imports study data from a CSV file
•	Imports expense data from a JSON file
•	Cleans and validates all incoming data
•	Stores clean data in local JSON files
•	Generates reports for study and expenses
•	Allows filtering and searching of stored data
•	Logs invalid records for debugging

How it works:
•	The system follows a simple data pipeline:
o	Input → Validate → Transform → Store → Analyze

Example output:
    Processing input/study.csv ...
    Rows processed	: 200
    Valid rows		: 185
    Invalid rows		: 15
    Saved to		: store/study.json
    Errors logged		: output/errors.log
    Time			: 0.042s

What I learned:
•	Building a simple data pipeline in Python
•	Working with CSV and JSON files
•	Data validation and cleaning techniques
•	Structuring a project into modules
•	Basic data analysis and reporting

Future improvements:
•	Add SQLite database instead of JSON storage
•	Integrate Pandas for analysis
•	Add data visualizations (with MatPlotLib)
•	Improve Smart Mode feature (Option 4 on the main Menu)

Author:
Koketso Spato
BSc Computer Science & Mathematics
University of Johannesburg
