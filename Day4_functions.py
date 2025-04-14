# We import datetime so we can add timestamps to prompts
from datetime import datetime

# This function asks the user to type a prompt
def ask_prompt(index):
    return input(f"Enter prompt #{index + 1}:")

# This function checks if a prompt contains unsafe words
def is_prompt_safe(prompt):
    banned_words = ["hack", "kill", "steal", "kiwi"]
    for word in banned_words:
        if word in prompt.lower():
            return False  # Unsafe!
    return True  # Safe!

# This function attaches a timestamp to the prompt
def log_prompt(prompt):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (prompt, timestamp)  # Returns a tuple

# This function prints all prompts in a list with their timestamps
def show_prompts(title, prompt_list):
    print(f"\n{title} Prompts:")
    for p, t in prompt_list:
        print(f"- {p} (logged at {t})")

# This is the main controller of our program
def main():
    approved = []  # List of safe prompts
    blocked = []   # List of unsafe prompts

    # Ask how many prompts the user wants to enter
    num = int(input("How many prompts would you like to enter? "))

    # Loop through that many times
    for i in range(num):
        prompt = ask_prompt(i)

        # Check if the prompt is safe or not
        if is_prompt_safe(prompt):
            print("Prompt approved.")
            approved.append(log_prompt(prompt))
        else:
            print("Prompt blocked.")
            blocked.append(log_prompt(prompt))

    # Show both results at the end
    show_prompts("YES Approved", approved)
    show_prompts("NO Blocked", blocked)

# This line makes sure the program runs when you launch it
main()
