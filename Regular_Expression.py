import re

# Open the log file
with open("C:\\Python\\718134_963258_Log\\718134_963258_Log.txt", "r") as f:
    log_data = f.read()

# Find all occurrences of [USER_ACTION] using regular expressions
pattern = r"\[USER_ACTION\]"
user_actions = re.findall(pattern, log_data)

# Print the results
print(user_actions)
