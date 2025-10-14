import time
hours = 0
minutes = 0
seconds = 0

for hours in range(12):
    for minutes in range (60):
        for seconds in range (60):
            print(f"{hours}:{minutes}:{seconds}")
            time.sleep(1)

    