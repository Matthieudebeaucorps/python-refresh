# Importing required modules
from datetime import datetime  # For adding timestamps
import csv  # For saving and loading data in CSV format

# Ask the user to input a prompt with a counter
def ask_prompt(index):
    return input(f"Enter prompt #{index + 1}: ")

# Check if a prompt contains any blocked words
def is_prompt_safe(prompt):
    blocked = ["hack", "kill", "steal", "kiwi"]  # List of unsafe keywords
    return not any(word in prompt.lower() for word in blocked)

# Create a dictionary entry with the prompt, status, and current time
def log_prompt(prompt, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    return {
        "prompt": prompt,
        "status": status,
        "timestamp": timestamp
    }
# Create a main function to run the program
def main():
    prompt_history = []  # A list to store all prompt dictionaries

    num = int(input("How many prompts would you like to log? "))  # Ask user for number of prompts

    for i in range(num):  # Loop over the number of prompts
        prompt = ask_prompt(i)  # Get each prompt from the user

        if is_prompt_safe(prompt):  # Check if it's safe
            print("YES Prompt approved.")
            entry = log_prompt(prompt, "approved")  # Make a dictionary entry with status
        else:
            print("NO Prompt blocked.")
            entry = log_prompt(prompt, "blocked")
        prompt_history.append(entry)  # Save the prompt dictionary to the list

    # Print a readable summary at the end
    print("\n📜 Prompt History:")
    for p in prompt_history:
        print(f"- {p['status'].upper()}: {p['prompt']} (logged at {p['timestamp']})")

    return prompt_history  # Return the list of dictionaries so we can save it

# Write the list of prompt dictionaries to a CSV file
def save_to_csv(prompt_data, filename="prompt_log.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["prompt", "status", "timestamp"])  # Define columns
        writer.writeheader()  # Write column headers to the file
        writer.writerows(prompt_data)  # Write all rows from the list of dictionaries
    print(f"\n💾 Prompt log saved to {filename}")

# Load saved data back into a list of dictionaries
def load_from_csv(filename="prompt_log.csv"):
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Automatically reads headers
        return list(reader)  # Return list of dictionaries

# Example usage
loaded = load_from_csv()
print("\n Re-loaded from CSV:")
for p in loaded:
    print(f"{p['timestamp']} | {p['status'].upper()} | {p['prompt']}")
    
# Run the program and save the log to file
prompt_data = main()
save_to_csv(prompt_data)