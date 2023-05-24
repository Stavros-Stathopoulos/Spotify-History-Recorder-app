'''
this script converts bitrate to size in megabytes
and it is used in the spotify_track.py script
it contains the following functions:
    Convert_bits_to_bytes(bits) - Converts bits to bytes
    Convert_bytes_to_kilobytes(bytes) - Converts bytes to kilobytes
    Convert_kilobytes_to_megabytes(kilobytes) - Converts kilobytes to megabytes
    convert_bitrate_to_size(time_in_seconds, bitrate) - Calculates the size in megabytes using the bitrate and the time in seconds

in order to use this script you need to import it in the script you want to use it
and call the function you want to use
for example:
    import convert_bitrate_to_size
    size_in_megabytes = convert_bitrate_to_size.convert_bitrate_to_size(time_in_seconds, bitrate)

Every function has a default value for the parameters
if you want to use the default value you don't need to pass any parameter
for example:
    import convert_bitrate_to_size
    size_in_megabytes = convert_bitrate_to_size.convert_bitrate_to_size()

if you want to use your own values you need to pass the parameters
for example:
    import convert_bitrate_to_size
    size_in_megabytes = convert_bitrate_to_size.convert_bitrate_to_size(180, 160)

Every function returns a value that is type decimal so you need to convert it to float or int 
(Its better to convert to float with type casting for example: float(size_in_megabytes)) 
    or import decimal in the script you want to use it

Created on 05/04/2023
Created by: Stavros Stathopoulos

'''
import decimal #This is a module that allows us to work with decimal numbers Very important to use decimal instead of float

#This is a function that sets the precision of the decimal numbers
decimal.getcontext().prec =4

#This is a function that converts bits to bytes
def Convert_bits_to_bytes(bits = 1):
    bytes = decimal.Decimal(bits) / decimal.Decimal(8)
    return bytes

#This is a function that converts bytes to kilobytes
def Convert_bytes_to_kilobytes(bytes = 1):
    kilobytes = decimal.Decimal(bytes) / decimal.Decimal(1024)
    return kilobytes

#This is a function that converts kilobytes to megabytes
def Convert_kilobytes_to_megabytes(kilobytes = 0):
    megabytes = decimal.Decimal(kilobytes) / decimal.Decimal(1024)
    return megabytes

#This is a function that calculates the size in megabytes using the bitrate and the time in seconds
def convert_bitrate_to_size(time_in_seconds = 180, bitrate_in_bps = 160):

    #Bitrate = sample rate * bits per sample * channels
    #size_in_bits = time_in_seconds * bitrate

    size_in_bits = decimal.Decimal(bitrate_in_bps) * decimal.Decimal(time_in_seconds)
    size_in_bytes = Convert_bits_to_bytes(size_in_bits)
    size_in_kilobytes = Convert_bytes_to_kilobytes(size_in_bytes)
    size_in_megabytes = Convert_kilobytes_to_megabytes(size_in_kilobytes)
    return size_in_megabytes

#This is the main function of the script used for testing
if __name__ == '__main__':
    time_in_seconds = 155.4
    bitrate = 160000
    size_in_kilobytes = convert_bitrate_to_size(time_in_seconds, bitrate)
    print(size_in_kilobytes)
