import sys
import json
from datetime import date


# The getTime functions will check to make sure the users input times are acceptable
def getStartTime():
    startTimeCheck = False
    global startTime
    while startTimeCheck == False:
        startTime = input("Please choose a starting time: ")
        if startTime == "exit" or startTime == "Exit":
            with open('roomFile_1', 'w') as outfile:
                json.dump(room_1, outfile, indent=4)
            with open('roomFile_2', 'w') as outfile:
                json.dump(room_2, outfile, indent=4)
            with open('roomFile_3', 'w') as outfile:
                json.dump(room_3, outfile, indent=4)
            with open('roomFile_4', 'w') as outfile:
                json.dump(room_4, outfile, indent=4)
            with open('roomFile_5', 'w') as outfile:
                json.dump(room_5, outfile, indent=4)
            sys.exit()
        elif startTime == "":
            print("You did not input a time!")
        elif int(startTime) < 0 or int(startTime) > 24:
            print("Please choose a time greater than 0 and less than 24.")
        else:
            startTimeCheck = True
    return startTime


def getEndTime():
    endTimeCheck = False
    while endTimeCheck == False:
        endTime = input("Please choose an ending time: ")
        if endTime == "exit" or endTime == "Exit":
            with open('roomFile_1', 'w') as outfile:
                json.dump(room_1, outfile, indent=4)
            with open('roomFile_2', 'w') as outfile:
                json.dump(room_2, outfile, indent=4)
            with open('roomFile_3', 'w') as outfile:
                json.dump(room_3, outfile, indent=4)
            with open('roomFile_4', 'w') as outfile:
                json.dump(room_4, outfile, indent=4)
            with open('roomFile_5', 'w') as outfile:
                json.dump(room_5, outfile, indent=4)
            sys.exit()
        elif endTime == startTime:
            print("You cannot choose the same time for start and end times.")
        elif endTime == "":
            print("You did not input a time!")
        elif int(endTime) < 0 or int(endTime) > 24 or endTime == "":
            print("Please choose a time greater than 0 and less than 24.")
        else:
            endTimeCheck = True
    return endTime


def getScheduleDate(scheduleDate):
    dateToday = date.today()
    dateToday = int(str(dateToday).replace("-", ""))
    dateScheduleCheck = False
    while dateScheduleCheck == False:
        if scheduleDate == "exit" or scheduleDate == "Exit":
            with open('roomFile_1', 'w') as outfile:
                json.dump(room_1, outfile, indent=4)
            with open('roomFile_2', 'w') as outfile:
                json.dump(room_2, outfile, indent=4)
            with open('roomFile_3', 'w') as outfile:
                json.dump(room_3, outfile, indent=4)
            with open('roomFile_4', 'w') as outfile:
                json.dump(room_4, outfile, indent=4)
            with open('roomFile_5', 'w') as outfile:
                json.dump(room_5, outfile, indent=4)
            sys.exit()
        elif scheduleDate == "":
            print("You did not enter a date.")
        elif int(scheduleDate) < dateToday:
            print("Sorry, you entered an past date. Please enter a future date.")
        else:
            dateScheduleCheck = True
    return dateScheduleCheck


# The overLap function will test to see if requested meeting times overlap with pre-existing meetings
def overLap(startTime, endTime, room):
    check = True
    for times in room:
        if int(startTime) > int(times["Start Time"]) and int(startTime) < int(times["End Time"]):
            check = False
            break
        elif int(endTime) > int(times["Start Time"]) and int(endTime) < int(times["End Time"]):
            check = False
            break
        elif int(startTime) == int(times["Start Time"]) and int(endTime) > int(times["End Time"]):
            check = False
            break
        elif int(startTime) == int(times["Start Time"]) and int(endTime) == int(times["End Time"]):
            check = False
            break
    return check


# The timeScheduler function will schedule the requested time if it is available. It works calling the overLap function
# and testing to see if it is true.
def timeScheduler(startTime, endTime, date):
    check = False
    # for room in rooms:
    if overLap(startTime, endTime, room_1) == True: # If this is true, the program will schedule the users time request
        data = {
            "Name": name,
            "Date": date,
            "Start Time": startTime,
            "End Time": endTime
        }
        room_1.append(data)
        print(f'Great! Your scheduled reservation is from {startTime} to {endTime}, in room 1')
    else:
        if overLap(startTime, endTime, room_2) == True:  # If this is true, the program will schedule the users time request
            data = {
                "Name": name,
                "Date": date,
                "Start Time": startTime,
                "End Time": endTime
            }
            room_2.append(data)
            print(f'Great! Your scheduled reservation is from {startTime} to {endTime}, in room 2')
        else:
            if overLap(startTime, endTime, room_3) == True:  # If this is true, the program will schedule the users time request
                data = {
                    "Name": name,
                    "Date": date,
                    "Start Time": startTime,
                    "End Time": endTime
                }
                room_3.append(data)
                print(f'Great! Your scheduled reservation is from {startTime} to {endTime}, in room 3')
            else:
                if overLap(startTime, endTime, room_4) == True:  # If this is true, the program will schedule the users time request
                    data = {
                        "Name": name,
                        "Date": date,
                        "Start Time": startTime,
                        "End Time": endTime
                    }
                    room_4.append(data)
                    print(f'Great! Your scheduled reservation is from {startTime} to {endTime}, in room 4')
                else:
                    if overLap(startTime, endTime, room_5) == True:  # If this is true, the program will schedule the users time request
                        data = {
                            "Name": name,
                            "Date": date,
                            "Start Time": startTime,
                            "End Time": endTime
                        }
                        room_5.append(data)
                        print(f'Great! Your scheduled reservation is from {startTime} to {endTime}, in room 5')
                        check = True
                    else: # If no times are available, the user will be denied access to reserving that time
                        print("Sorry, the time you selected is not available to reserve. The following times are not available: ")
                        for times in room_1:
                            print(times["Start Time"] + " to " + times["End Time"] + " in room 1")
                        for times in room_2:
                            print(times["Start Time"] + " to " + times["End Time"] + " in room 2")
                        for times in room_3:
                            print(times["Start Time"] + " to " + times["End Time"] + " in room 3")
                        for times in room_4:
                            print(times["Start Time"] + " to " + times["End Time"] + " in room 4")
                        for times in room_5:
                            print(times["Start Time"] + " to " + times["End Time"] + " in room 5")
                    return check


# Load the json files into their respective rooms
def loadJSON(file, room):
    with open(file, 'r') as infile:
        data = json.loads(infile.read())
        for i in data:
            if i in room:
                continue
            else:
                room.append(i)
        return room


# Initializing room_1 as an empty array because no times have been reserved
room_1 = []
room_2 = []
room_3 = []
room_4 = []
room_5 = []


# The program will only exit once the user types exit. This allows for multiple meetings to be requested during a
# single session.
print('To exit, please type "exit" at any time.')
print('Please enter all times in 24-hr format.')


loadJSON('roomFile_1', room_1)
loadJSON('roomFile_2', room_2)
loadJSON('roomFile_3', room_3)
loadJSON('roomFile_4', room_4)
loadJSON('roomFile_5', room_5)
finalCheck = True
while finalCheck == True:
    global name
    name = input("Please input your name: ")
    scheduleDate = input("Please choose a date for your meeting, in the format of 'Year-Month-Day: XXXX-XX-XX': ")
    scheduleDate = scheduleDate.replace("-", "")
    if getScheduleDate(scheduleDate) == True:
        timeScheduler(getStartTime(), getEndTime(), scheduleDate)
        continueInput = input("Would you like to schedule another meeting (yes or no)? ")
        if continueInput == "no":
            with open('roomFile_1', 'w') as outfile:
                json.dump(room_1, outfile, indent=4)
            with open('roomFile_2', 'w') as outfile:
                json.dump(room_2, outfile, indent=4)
            with open('roomFile_3', 'w') as outfile:
                json.dump(room_3, outfile, indent=4)
            with open('roomFile_4', 'w') as outfile:
                json.dump(room_4, outfile, indent=4)
            with open('roomFile_5', 'w') as outfile:
                json.dump(room_5, outfile, indent=4)
            sys.exit()
