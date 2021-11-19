set /p json= "enter json name: "
set /p calls= "enter calls name: "
python Ex1.py %json%.json %calls%.csv %json%_%calls%_out.csv
java -jar Ex1_checker_V1.2_obf.jar 325010288,325300820 %json%.json %json%_%calls%_out.csv %json%_%calls%.log  
pause