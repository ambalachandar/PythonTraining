import re

with open("C:\\Python\\718134_963258_Log\\718134_963258_Log.txt", "r") as f:
    log_contents = f.read()

# Use a regular expression to find all occurrences of [USER_ACTION]
pattern = re.compile(r"\[USER_ACTION\]")
matches = pattern.findall(log_contents)

# Print the number of matches found

print(f"Number of [USER_ACTION] occurrences: {len(matches)}")
