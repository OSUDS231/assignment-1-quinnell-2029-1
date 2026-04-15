secs = int(input("Please enter a number of seconds to convert into hours, minutes, seconds:"))
hours = secs // 3600
minutes = (secs % 3600) // 60
seconds = secs % 60

print(f"{secs} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
