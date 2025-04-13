# Python Refresh

A Python project template with development tools setup.

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source .venv/bin/activate
```
- On Windows:
```bash
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development Tools

- **Black**: Code formatter
  - Format code: `black .`
  
- **pytest**: Testing framework
  - Run tests: `pytest`

## Project Structure

- **Day1_basics.py**: Introduction to Python basics
- **Day2_logic.py**: Logic and control flow
- **Day3_loops_ranges.py**: Loops, ranges, and input handling with a prompt logging system

## Day 3: Loops and Ranges

The Day3_loops_ranges.py script demonstrates:
- Working with loops and ranges
- User input handling
- String manipulation
- Conditional logic
- Timestamp logging
- List management

To run the Day 3 script:
```bash
python Day3_loops_ranges.py
```

The script will prompt you to enter multiple prompts, which it will categorize as approved or blocked based on content.
