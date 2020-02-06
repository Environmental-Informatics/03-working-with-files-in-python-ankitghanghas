README FILE FOR RACCOON EXPERIMENT
Version 1.0
Created By Ankit Ghanghas 
Thu Feb  6 15:04:37 EST 2020
--------------------------------------------------------------------------------

The entire processing is done using a python script named  Evaluate_Raccoon_Life.py
--------------------------------------------------------------------------------

Processing

The script reads the ouput from a Raccoon behavior model as an input file and stores the different type of data provided in the comma separated file in a dictionary.
Based on the X and Y coordinates specified in the input file, it  calculates and stores the distance travelled by the raccoon in the last hour starting with zero as it is taken as reference position.
It also computes the average energy level, mean X and Y coordinates and total distance moved by the raccoon during the entire experiment.

The script writes the Raccoon name, average location, distance travelled, average energy level and final state of the raccoon at the end of the experiment as the header of a new output text file named Georges_life.txt

The script also writes the date, time, X and Y coordinate, the asleep flag, the behaviour mode and the distance travelled for each hour of the raccoon life to the output file as tab separated data.

--------------------------------------------------------------------------------

Files

Input File: 2008Male00006.txt
Output File: Georges_life.txt


Column header for the data in the output file

'Day' : Day of measurement
'Time': Time of measurement
' X' : X coordinate of the raccoon
' Y' : Y coordinate of the raccon
' Asleep': the asleep flag
'Behavior Mode' : Behavior of the raccoon for the last observed hour
'Distance' : Distance travelled by the raccoon since last measurement.


For additional information please send an e-mail to aghangha@purdue.edu
