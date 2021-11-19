import sys
import json
import csv


class Elevator:
    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time, calls):
        self._id = id
        self._speed = speed
        self._min_floor = min_floor
        self._max_floor = max_floor
        self._close_time = close_time
        self._open_time = open_time
        self._start_time = start_time
        self._stop_time = stop_time
        self._calls = calls

    def get_id(self):
        return self._id

    def get_speed(self):
        return self._speed

    def get_close_time(self):
        return self._close_time

    def get_open_time(self):
        return self._open_time

    def get_start_time(self):
        return self._start_time

    def get_stop_time(self):
        return self._stop_time

    def get_calls(self):
        return self._calls


class Building:
    def __init__(self, min_floor, max_floor, elevators):
        self._minFloor = min_floor
        self._maxFloor = max_floor
        self._elevators = []
        for elevDict in elevators:
            self._elevators.append(parse_elev_dict(elevDict))

    def get_elevators(self):
        return self._elevators


class Call:
    def __init__(self, time, source_floor, dest_floor, assigned_to):
        self._time = float(time)
        self._source_floor = int(source_floor)
        self._dest_floor = int(dest_floor)
        self._assigned_to = int(assigned_to)

    def get_time(self):
        return self._time

    def get_src(self):
        return self._source_floor

    def get_dest(self):
        return self._dest_floor

    def get_assigned_to(self):
        return self._assigned_to

    def set_assigned_to(self, chosen_elevator):
        self._assigned_to = chosen_elevator


def parse_elev_dict(elev_dict):
    elev_id = elev_dict["_id"]
    speed = elev_dict["_speed"]
    min_floor = elev_dict["_minFloor"]
    max_floor = elev_dict["_maxFloor"]
    close_time = elev_dict["_closeTime"]
    open_time = elev_dict["_openTime"]
    start_time = elev_dict["_startTime"]
    stop_time = elev_dict["_stopTime"]
    return Elevator(elev_id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time, [])


def parse_calls_file(file_name, calls):
    with open(file_name, 'r') as file:
        file = csv.reader(file)
        for line in file:
            calls.append(Call(line[1], line[2], line[3], line[5]))


def read_file(file_name):
    return open(file_name, "r").read()


def assign_calls(calls):
    for call in calls:
        assign_call(call)

    create_out_file(outName)


def assign_call(call):
    min_time = sys.maxsize
    elevators = building.get_elevators()
    chosen_elevator = 0
    for elevator in elevators:
        time_left = dist(call, elevator)
        if min_time > time_left:
            min_time = time_left
            chosen_elevator = elevator.get_id()

    call.set_assigned_to(chosen_elevator)

    for elevator in elevators:
        if chosen_elevator == elevator.get_id():
            elevator.get_calls().append(call)


def dist(call, elevator):
    elevator_calls = elevator.get_calls()
    time_left = 0
    distret = 0
    i = 0
    while i < len(elevator_calls):
        distret = abs(elevator_calls[i].get_dest() - elevator_calls[i].get_src()) / elevator.get_speed() + (
                    elevator.get_close_time() + elevator.get_open_time()) + elevator.get_start_time()+elevator.get_stop_time()

        if i > 0 and elevator_calls[i - 1].get_dest() != elevator_calls[i].get_src():
            distret += abs(elevator_calls[i - 1].get_dest() - elevator_calls[i].get_src()) / elevator.get_speed() + (
                        elevator.get_close_time() + elevator.get_open_time()) + elevator.get_start_time()+elevator.get_stop_time()

        if elevator_calls[i].get_time() + distret >= call.get_time():
            time_left += distret
        i += 1
        distret=0

    return time_left


def create_out_file(file_name):
    with open(file_name, 'w') as file:
        for elevator_call in calls:
            file.write(
                "Elevator call" + "," + str(elevator_call.get_time()) + "," + str(elevator_call.get_src()) + "," + str(
                    elevator_call.get_dest()) + "," + "0" + "," + str(elevator_call.get_assigned_to()))
            file.write("\n")


calls = []
jsonName = sys.argv[1]
callsName = sys.argv[2]
parse_calls_file(callsName, calls)
outName = sys.argv[3]
with open(jsonName, 'r') as file:
    readJson = json.loads(file.read())
building = Building(readJson["_minFloor"], readJson["_maxFloor"], readJson["_elevators"])
assign_calls(calls)
