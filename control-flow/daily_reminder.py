# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a HIGH priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a MEDIUM priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a LOW priority task.")
    case _:
        if time_bound == "yes":
            print(f"Reminder: '{task}' has an unspecified priority. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' has an unspecified priority.")
