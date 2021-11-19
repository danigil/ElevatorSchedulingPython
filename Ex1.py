import sys
import json
import csv


# Elevator Scheduling Offline-Algorithm
# This algorithm works by looking for the elevator that will arrive at a call's source floor the fastest
# taking into account the calls that are already assigned to the elevator.
# This python file contains 3 classes:
# Building which contains a list of elevators, and min_floor,max_floor variables
# Elevator which contains information about the elevator, speed, id, etc.
# Call which contains the time,source floor, destination floor of a call.
# The algorithm works by going over the list of calls, assigning each call an elevator.
# After all calls have been assigned an elevator, the algorithm creates a new output file, with all the call data.

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

    def get_min_floor(self):
        return self._min_floor

    def get_max_floor(self):
        return self._max_floor

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


# This function is called for all the list items in the json file
# It extracts the data from a dictionary that represents an elevator, and instantiates an Elevator object with the data,
# the object is returned.
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


# This function reads the calls file and fills a list with Call objects which
# contain the data from each call in the call file.
def parse_calls_file(file_name, calls):
    with open(file_name, 'r') as call_file:
        call_file = csv.reader(call_file)
        for line in call_file:
            calls.append(Call(line[1], line[2], line[3], line[5]))


# This function loops through all the calls in the calls list and calls the assign_call method on them one by one.
def assign_calls(calls):
    for call in calls:
        assign_call(call)

    create_out_file(out_name)


# This function is essentialy the main algorithm, it loops through all the elevators,
# calculates which elevator will arrive at the source floor first(using the dist method)
# and assigns the best elevator to the call.
def assign_call(call):
    min_time = sys.maxsize  # big number for comparisons, var used for storing the best found result so far.
    elevators = building.get_elevators()
    if len(elevators) > 0:
        chosen_elevator = elevators[0]  # sets the default elevator to the first one.
    else:
        chosen_elevator = -1
    for elevator in elevators:
        # this if checks whether the elevator can service the floors the call wants to go to,
        # if not it skips this elevator.
        if not (
                elevator.get_min_floor() <= call.get_src() <= elevator.get_max_floor() and elevator.get_max_floor() >= call.get_dest() >= elevator.get_min_floor()):
            continue

        time_till_arrival = dist(call, elevator)  # calculates how much time will it take
        # for the elevator to service the call.
        if min_time > time_till_arrival:  # if a better time was found, set it as the new best time,
            # and store the elevator's id.
            min_time = time_till_arrival
            chosen_elevator = elevator.get_id()

    call.set_assigned_to(chosen_elevator)

    for elevator in elevators:  # look for the chosen elevator objects using the id we kept,
        # add the call to the elevator's call list.
        if chosen_elevator == elevator.get_id():
            elevator.get_calls().append(call)


# This functions calculates the time it takes a certain elevator to get to a call, given its current tasks.
def dist(call, elevator):
    elevator_calls = elevator.get_calls()  # stores the elevators call list for iteration
    time_till_arrive = 0
    dist_calc = 0
    i = 0
    while i < len(elevator_calls):  # loops through all the elevator's calls
        # stores all the current elevator call's variables for better readability
        dest = elevator_calls[i].get_dest()
        src = elevator_calls[i].get_src()
        speed = elevator.get_speed()
        close = elevator.get_close_time()
        open = elevator.get_open_time()
        start = elevator.get_start_time()
        stop = elevator.get_stop_time()

        dist_calc = abs(dest - src) / speed + close + open + start + stop

        # if we're not looking at the first call, add the time it takes to move the elevator from the
        # the destination floor of the previous call to the current call's source floor.
        if i > 0 and elevator_calls[i - 1].get_dest() != src:
            dist_calc += abs(elevator_calls[i - 1].get_dest() - src) / speed + close + open + start + stop

        # if the call from the list finishes(arrives at its destination) before the time of
        # the target call we don't need to count it.
        if elevator_calls[i].get_time() + dist_calc >= call.get_time():
            time_till_arrive += dist_calc
        i += 1

    return time_till_arrive


# This function creates an output csv file from the calls list after they were all assigned.
def create_out_file(file_name):
    with open(file_name, 'w') as created_file:
        for elevator_call in calls:
            created_file.write(
                "Elevator call" + "," + str(elevator_call.get_time()) + "," + str(elevator_call.get_src()) + "," + str(
                    elevator_call.get_dest()) + "," + "0" + "," + str(elevator_call.get_assigned_to()))
            created_file.write("\n")


calls = []  # initialize the calls list.

# store the input arguments
json_name = sys.argv[1]
calls_name = sys.argv[2]
out_name = sys.argv[3]

# read the building json file
with open(json_name, 'r') as file:
    readJson = json.loads(file.read())

parse_calls_file(calls_name, calls)

# instantiate a building object from the json file.
building = Building(readJson["_minFloor"], readJson["_maxFloor"], readJson["_elevators"])

assign_calls(calls)
