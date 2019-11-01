import sys
import numpy as np


# The overLap function will test to see if requested meeting times overlap with pre-existing meetings
def overLap(startTime, endTime):
    global room_1
    check = True
    startTime = startTime
    endTime = endTime
    for times in room_1:
        if startTime > times[0] and startTime < times[1]:
            check = False
            break
        elif endTime > times[0] and endTime < times[1]:
            check = False
            break
        elif startTime == times[0] and endTime > times[1]:
            check = False
            break
        elif startTime == times[0] and endTime == times[1]:
            check = False
            break
    return check

# Initializing room_1 as an empty array because no times have been reserved
room_1 = []

# The timeScheduler function will schedule the requested time if it is available. It works calling the overLap function
# and testing to see if it is true.
def timeScheduler(startTime, endTime):
    global room_1
    if len(room_1) == 0: # This is an initial condition to insert a time if all times are free. This will only be used 1x
        room_1.append([startTime, endTime])
        print(f'Great! Your scheduled reservation is from {startTime} to {endTime}')
    elif overLap(startTime, endTime) == True: # If this is true, the program will schedule the users time request
        room_1.append([startTime, endTime])
        print(f'Great! Your scheduled reservation is from {startTime} to {endTime}')
    else: # If no times are available, the user will be denied access to reserving that time
        print("Sorry, the time you selected is not available to reserve. The following times are not available: ")
        for i in room_1:
            if (float(i[0]) and float(i[1])) < 12:
                print(f'{i[0]}am to {i[1]}am')
            if (float(i[0]) < 12 and float(i[1])) >= 12:
                a = int(i[1]) - 12
                print(f'{i[0]}am to {a}pm')
            if (float(i[0]) and float(i[1])) > 12:
                b = int(i[0]) - 12
                c = int(i[1]) - 12
                print(f'{b}pm to {c}pm')
            if (float(i[0]) > 12 and float(i[1]) <= 12):
                d = int(i[0]) - 12
                print(f'{d}pm to {i[1]}am')

# The program will only exit once the user types exit. This allows for multiple meetings to be requested during a
# single session.
print('To exit, please type "exit" at any time.')
print('Please enter all times in 24-hr format.')
while True:
    startTime = input('Please pick a start time: ')
    if startTime == 'exit':
        sys.exit()
    endTime = input('Please pick an ending time: ')
    if endTime == 'exit':
        sys.exit()
    timeScheduler(startTime, endTime)


