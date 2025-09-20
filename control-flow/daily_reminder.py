task = input('"Enter the task description:')
priority = input("Enter the task priority (high, medium, low):").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"{task} is a high priority task "
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"


if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)