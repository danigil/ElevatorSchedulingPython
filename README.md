# ElevatorSchdulingPython
This project is an offline-algorithm for elevator scheduling.
The algorithm works by allocating each call to an elevator that will serve it in the fastest time(The elevator that will arrive at the call's source floor first).

## Usage
The python file can produce results using a simulator. Click [here](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/libs/Ex1_checker_V1.2_obf.jar) to be redirected

To use the python file, use the following command in the command line: python Ex1.py arg1 arg2 arg3
      
arg1 is the path of a json file that represents a building(.json extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B1.json))<br />
      arg2 is the path of a csv file that represents a call list(.csv extension) (see [example](https://github.com/benmoshe/OOP_2021/blob/main/Assignments/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv))<br />
      arg3 is the desired name for the output file(.csv extension).(call list with elevator assignments).<br />
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

  

