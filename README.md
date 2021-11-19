# ElevatorSchdulingPython
This project is an offline-algorithm for elevator scheduling.  

## Introduction
We've been presented with the issue of an elevator system that needs to decide which elevator will serve which floors (given there are more than one elevator).  
The main goal is to distribute a given group of calls to the elevators in a way that will ensure minimum waiting time per call.  
This project presents an algorithm that solves this issue.

## Literature
This project was made after reading the following articles for understanding of the concept.  
[On-line Algorithms versus Off-line Algorithms for the Elevator](https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele) by Sasikanth Avancha,  Dipanjan Chakraborty, Vasundhara Puttagunta.  
[Online optimization: Elevator and vehicle scheduling](http://co-at-work.zib.de/berlin2009/downloads/2009-10-01/2009-10-01-1100-BH-Online-Optimization.pdf) by Benjamin Hiller

## Algorithm
The algorithm works by allocating each call to an elevator that will serve it in the fastest time(The elevator that will arrive at the call's source floor first).  
At first, the program parses the data from the input files and creates Building,Elevator,Call objects from the data.  
Each Elevator object holds its own list that contains Call objects, additionally, there is a global call list that contains all the calls.  
The algorithm loops through all the calls, and for each call it calls a method that takes the call object as an input and in turn decides which elevator is best suited for that call.  
The best elevator is the elevator that given its current assigned calls, will arrive at the source floor of the call we want to assign the fastest.  
The algorithm calculates this variable for each elevator, and takes the one with the lowest time(the elevator that will serve the call fastest).  
Once an elevator is chosen the algorithm adds the call to the elevator's call list(for future usage).  
After all the calls have been assigned the algorithm creates an output file identical to the input csv file, except the last cell which is changed to the assigned elevator's id.  

## Usage
To use the python file, use the following command in the command line: python Ex1.py arg1 arg2 arg3  
     
arg1 is the path of a json file that represents a building(.json extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B1.json))  
      arg2 is the path of a csv file that represents a call list(.csv extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv))  
      arg3 is the desired name for the output file. a .csv extension (call list with elevator assignments).  
      
The program outputs a csv file like the call file received in the input, only the last cell of every call is changed to the id of the elevator that was allocated to that call.
      
The output file can then be run through a simulator, to see how how the calls were treated with the allocations.  
Click [here](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/libs/Ex1_checker_V1.2_obf.jar) to be redirected to a simulator file  
We recommend you use the .bat file thats provided if you intend to use the python file with the simulator cited above.

## Bat File Usage
To use the bat file you need to have 4 different files in your directory:  
-Ex1_checker_V1.2_obf.jar  
-Ex1.py  
-Building json file  
-Call list csv file  

1)Run the .bat file.  
2)Enter the name of the json file(without extension) and press enter.  
3)Enter the name of the csv file(without extension) and press enter.  
The program will run and output a log file(logs the simulator), and the output file from the python program.

  

