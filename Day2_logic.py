# 🚀 AI Prompt Score Checker
age = int(input("How old are you? "))
if age >= 18:
    print("You’re an adult. Congrats big boy")
else:
    print("You’re not allowed here (yet) little baby.")

prompt = input("Enter your AI prompt: ")

if "hack" in prompt.lower() or "kill" in prompt.lower() or "steal" in prompt.lower():
    print("Prompt blocked for safety.")
else:
    print("All good my G, Prompt approved. Sending to Claude...")

