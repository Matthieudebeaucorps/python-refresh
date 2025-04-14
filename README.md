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

---

### Day 4 – Functions & Clean Architecture

**What I learned:**
- How to create reusable functions in Python
- How to break down a program into clean, modular parts
- How to use tuples and timestamps in a real-world tool
- Prepped a clean Claude-safe prompt logger for future upgrades

**Functions created:**
- `ask_prompt(index)` – gets user input
- `is_prompt_safe(prompt)` – blocks unsafe prompts
- `log_prompt(prompt)` – adds timestamp to a prompt
- `show_prompts(title, list)` – prints prompts with a title

### Day 5 – Dictionaries, Lists & CSV Logging
**What I learned:**

Used dictionaries to structure prompt entries (prompt, status, timestamp)

Stored all entries in a list for tracking multiple prompts
Used Python’s csv module to save data to prompt_log.csv
Learned to re-load prompt data from a CSV and display it cleanly
Built a fully functioning Claude-safe prompt history logger

**Features added:**

List of prompt entries as dictionaries
CSV export with csv.DictWriter
Reload function with csv.DictReader
Optional blocked words like "hack", "kill", "steal", "kiwi"
