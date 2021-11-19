# ElevatorSchdulingPython
This project is an offline-algorithm for elevator scheduling.
## Introduction
We've been presented with the issue of an elevator system that needs to decide which elevator will serve which floors (given there are more than one elevator).  
The main goal is to distribute a given group of calls to the elevators in a way that will ensure minimum waiting time per call.  
This project presents an algorithm that solves this issue.

## The algorithm
The algorithm works by allocating each call to an elevator that will serve it in the fastest time(The elevator that will arrive at the call's source floor first).

## Usage
To use the python file, use the following command in the command line: python Ex1.py arg1 arg2 arg3  
     
arg1 is the path of a json file that represents a building(.json extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B1.json))<br />
      arg2 is the path of a csv file that represents a call list(.csv extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv))<br />
      arg3 is the desired name for the output file(.csv extension).(call list with elevator assignments).<br />
      
The program outputs a csv file like the call file received in the input, only the last cell of every call is changed to the id of the elevator that was allocated to that call.
      
The output file can then be run through a simulator, to see how how the calls were treated with the allocations.  
Click [here](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/libs/Ex1_checker_V1.2_obf.jar) to be redirected to a simulator file  
We recommend you use the .bat file thats provided if you intend to use the python file with the simulator cited above.

## Bat File Usage
To use the bat file you need to have 4 different files in your directory:<br />
-Ex1_checker_V1.2_obf.jar<br />
-Ex1.py<br />
-Building json file<br />
-Call list csv file<br />

1)Run the .bat file.  
2)Enter the name of the json file(without extension) and press enter.  
3)Enter the name of the csv file(without extension) and press enter.
The program will run and output a log file(logs the simulator), and the output file from the python program.

  

