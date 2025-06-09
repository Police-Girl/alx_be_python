task = input ("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time = input ("Is it time-bound? (yes/no): ")
match priority:
	case "high":
		print(f"{task}, is a high priority task that requires immediate attention today!")
	case "medium":
		print(f"{task}, is a medium priority task keep it in mind.")
	case "low":
		print(f"{task}, is a  low priority task. Consider completing it when you have free time.")
if time == "yes":
	print(f"The task is time-bound.")
if time == "no":
	print (f"The task is not time-bound")
