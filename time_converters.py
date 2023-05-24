'''
This is a script that converts time from miliseconds to seconds and from seconds to minutes and from minutes to seconds
This script is used in the script Scripts\convert_bitrate_to_size.py
It contains the following functions:
    Convert_from_milisec_to_sec(time_in_miliseconds) - Converts time from miliseconds to seconds
    Convert_from_sec_to_min(time_in_seconds) - Converts time from seconds to minutes
    Convert_min_to_sec(time_in_minutes) - Converts time from minutes to seconds

In order to use this script you need to import it in the script you want to use it
and call the function you want to use
for example:
    import time_converters
    time_in_seconds = time_converters.Convert_from_milisec_to_sec(time_in_miliseconds)

Every function takes one parameter which is the time in miliseconds, seconds or minutes as a float and returns the time in seconds, minutes or miliseconds as a decimal
we use decimal instead of float because it is more accurate
Every function returns a value that is type decimal so you need to convert it to float or int 
(It's better due to higher acuracy to convert to float with type casting for example: float(time_in_seconds)) 



Created on 05/04/2023
Created by: Stavros Stathopoulos
'''
import decimal# This is a module that allows us to work with decimal numbers
#This is a function that sets the precision of the decimal numbers for better accuracy try bigger numbers like 10 or 100
decimal.getcontext().prec = 4

#This is a function that converts time from miliseconds to seconds
def Convert_from_milisec_to_sec(time_in_miliseconds):
    time_in_seconds = decimal.Decimal(time_in_miliseconds) / decimal.Decimal(1000)
    return time_in_seconds

#This is a function that converts time from seconds to minutes
def Convert_from_sec_to_min(time_in_seconds):
    time_in_minutes = decimal.Decimal(time_in_seconds) / decimal.Decimal(60)
    return time_in_minutes

#This is a function that converts time from minutes to seconds
def Convert_min_to_sec(time_in_minutes):
    time_in_seconds = decimal.Decimal(time_in_minutes) * decimal.Decimal(60)
    return time_in_seconds

#This is the main function that is used for testing the functions
if __name__ == '__main__':
    time_in_miliseconds = 187200
    time_in_seconds = Convert_from_milisec_to_sec(time_in_miliseconds)
    time_in_minutes = Convert_from_sec_to_min(time_in_seconds)
    print(time_in_minutes)
    time_in_seconds = Convert_min_to_sec(time_in_minutes)
    print(time_in_seconds)

