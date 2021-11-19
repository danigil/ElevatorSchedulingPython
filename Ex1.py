import sys
import json
import re
import csv


class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime, calls):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self._calls = calls

    def get_id(self):
        return self._id

    def get_calls(self):
        return self._calls

    def get_speed(self):
        return self._speed

    def get_closeTime(self):
        return self._closeTime

    def get_openTime(self):
        return self._openTime

    def get_startTime(self):
        return self._startTime

    def get_stopTime(self):
        return self._stopTime


class Building:
    def __init__(self, minFloor, maxFloor, elevators):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevators = []
        for elevDict in elevators:
            self._elevators.append(parse(elevDict))

    def get_elevators(self):
        return self._elevators


class Call:
    def __init__(self, time, sourceFloor, destFloor, assignedTo):
        self._time = float(time)
        self._sourceFloor = int(sourceFloor)
        self._destFloor = int(destFloor)
        self._assignedTo = int(assignedTo)

    def get_src(self):
        return self._sourceFloor

    def get_time(self):
        return self._time

    def get_dest(self):
        return self._destFloor

    def set_assignedTo(self, chosenElevator):
        self._assignedTo = chosenElevator

    def get_assignedTo(self):
        return self._assignedTo


def parse(elevDict):
    elev_id = elevDict["_id"]
    speed = elevDict["_speed"]
    min_floor = elevDict["_minFloor"]
    max_floor = elevDict["_maxFloor"]
    close_time = elevDict["_closeTime"]
    open_time = elevDict["_openTime"]
    start_time = elevDict["_startTime"]
    stop_time = elevDict["_stopTime"]
    return Elevator(elev_id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time, [])


def parse_calls_file(file_name, calls):
    with open(file_name, 'r') as file:
        file = csv.reader(file)
        for line in file:
            calls.append(Call(line[1], line[2], line[3], line[5]))


def read_file(file_name):
    return open(file_name, "r").read()


def assignCalls(calls):
    for call in calls:
        assignCall(call)

    createFile(outName)

def assignCall(call):
    min_time = sys.maxsize
    elevators = building.get_elevators()
    chosen_elevator = elevators[0]
    for elevator in elevators:
        time_left=dist(call,elevator)
        if min_time>time_left:
            min_time=time_left
            chosen_elevator = elevator.get_id()

    call.set_assignedTo(chosen_elevator)

    for elevator in elevators:
        if chosen_elevator== elevator.get_id():
            elevator.get_calls().append(call)

def dist(call, elevator):
    elevator_calls = elevator.get_calls()
    time_left=0

    i=0
    while(i<len(elevator_calls)):
        distret= abs(elevator_calls[i].get_dest()-elevator_calls[i].get_src())*elevator.get_speed()+(elevator.get_closeTime() + elevator.get_openTime())


        if i>0 and elevator_calls[i-1].get_dest()!=elevator_calls[i].get_src():
            distret+= abs(elevator_calls[i-1].get_dest()-elevator_calls[i].get_src())*elevator.get_speed()+(elevator.get_closeTime() + elevator.get_openTime())
        else:
            distret+=0

        if (elevator_calls[i].get_time() + distret >= call.get_time()):
            time_left += distret
        i+=1

    return time_left

def createFile(fileName):
    with open(fileName, 'w') as file:
        for elevator_call in calls:
            file.write("Elevator call" +","+ str(elevator_call.get_time()) + "," + str(elevator_call.get_src()) +"," + str(elevator_call.get_dest()) +"," + "0" +"," + str(elevator_call.get_assignedTo()))
            file.write("\n")


calls = []
jsonName = sys.argv[1]
callsName = sys.argv[2]
parse_calls_file(callsName, calls)
outName= sys.argv[3]
readJson = json.loads(read_file(jsonName))
building = Building(readJson["_minFloor"], readJson["_maxFloor"], readJson["_elevators"])
assignCalls(calls)



