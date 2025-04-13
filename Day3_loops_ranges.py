from datetime import datetime

prompt_list = []
num_prompts = int(input("How many prompts would you like to log?"))

approved = []
blocked =[]

for i in range(num_prompts):
    prompt = input(f"Enter prompt #{i+1}: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if any(word in prompt.lower() for word in ["hack", "kill", "steal"]):
        print("Prompt blocked.")
        blocked.append((prompt, timestamp))
    else:
        print("Prompt approved.")
        approved.append((prompt, timestamp))

print("\nApproved Prompts:")
for p, t in approved:
    print(f"- {p} (logged at {t})")

print("\nBlocked Prompts:")
for p, t in blocked:
    print(f"- {p}(logged at {t})")
    

