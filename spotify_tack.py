"""
This program gets the song you are currently listening to on Spotify and saves it in an excel file.
   It also saves the artist, the duration, the preview link, the country and the type of the song.
   The program waits 200 seconds to get the next song.
   If you want to change the country you can change the country code in the line 100.
   In order to run the program you need to create a Spotify app and get the client id and the client secret.    https://developer.spotify.com/dashboard/applications
   You also need to change the client id and the client secret arguments given in lines 91-93 .
   In the app you need to add the redirect uri http://localhost:9000 and the scope user-read-recently-played, user-read-playback-state.
   The program is written in Python 3.10.0.
   The program uses the following libraries:
   - spotipy in version 2.22.1  https://pypi.org/project/spotipy/ 
   - xlwt in version 1.3.0      https://pypi.org/project/xlwt/
   - datetime in version 4.3    https://pypi.org/project/DateTime/
   - time in version 3.10.0     https://pypi.org/project/time/
   - tqdm in version 4.62.3     https://pypi.org/project/tqdm/
   The program uses the following classes:
   - SpotifyTrack
   The program uses the following methods:
   - Authentification(): To access authorised Spotify data
   - get_data(): To get the data from the api
   - create_data_list(): To create an excel file
   - save_data(): To write data in the right position
   - driver_func(): To run the program
   - main(): To run the program

   The program uses the following API:
   - Spotify API
   The program uses the following API endpoints:
   - GET https://api.spotify.com/v1/me/player/currently-playing
   The program uses the following API scopes:
   - user-read-recently-played
   - user-read-playback-state

   The program uses the following API parameters:
   - country

   The program uses the following API response:
   - name
   - artist
   - duration
   - preview_link
   - country
   - type
   - date

   The program uses the following API errors:
   - 401 Unauthorized
   - 404 Not Found
   - 429 Too Many Requests

   The program uses the following API error messages:
   - The access token expired

   Created by: Stavros Stathopoulos
   Created on: 2023-04-02
   """

from tqdm import tqdm #To show the progress bar
import spotipy  #To access the Spotify API
from spotipy.oauth2 import SpotifyOAuth #To access authorised Spotify data
from xlwt import Workbook #To create an excel file
import datetime #To get the date
import time #To make the program wait
import sys #To get the client id and the client secret from another file
sys.path.insert(0,"Scripts\tools") #To get the client id and the client secret from another file
import credentialsprof #To get the client id and the client secret from another file
import time_converters #To convert the duration from milliseconds to minutes
import convert_bitrate_to_size #To convert the bitrate to size

def convert(time_in_miliseconds):
    time_in_seconds = time_converters.Convert_from_milisec_to_sec(time_in_miliseconds)
    time_in_minutes = time_converters.Convert_from_sec_to_min(time_in_seconds)
    return time_in_minutes

class SpotifyTrack:
    
    def __init__(self):
        self.i = 1
        print("Welcome to Spotify Track")
        self.driver_func()

#we try authentification 
    def Authentification(self):
        #we try authentification
        
        for i in tqdm (range (101),
            desc="Authentification...",
            ascii=False, ncols=75):
            time.sleep(0.01)
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentialsprof.client_id,
                                                client_secret=credentialsprof.client_secret,
                                                redirect_uri=credentialsprof.redirect_uri,
                                                scope="user-read-recently-played, user-read-playback-state"))
        print("Authentification successful")

#we get the data from the api       
    def get_data(self):
        bitrate = 160000
        #we try to get the data from the api and we print the error if we can't
        self.results = self.sp.currently_playing('GR')
        #we get the song name
        song_name = self.results['item']['name']
        #we get the artist name
        artist_name = self.results['item']['artists']
        #we get the preview link of the song
        preview_link = self.results['item']['preview_url']
        #we get the duration in milliseconds
        self.duration = self.results['item']['duration_ms']
        #we convert the duration from milliseconds to minutes
        self.duration =(convert(self.duration))
        #we create a list of dictionaries
        data = []
        #we append the data in the list
        data.append({"name":song_name})
        data.append({"artist":artist_name[0]['name']})
        data.append({"duration":self.duration})
        data.append({"preview_link":preview_link})
        data.append({"country":"Greece"})
        data.append({"type":"spotify"}) 
        data.append({"date":datetime.datetime.now()})
        data.append({"bitrate":str(bitrate/1000)+"kbps"})
        data.append({"file_format":"AAC"})
        data.append({"file_size":convert_bitrate_to_size.convert_bitrate_to_size(bitrate, time_converters.Convert_min_to_sec(self.duration))})
        #we call the write_data function
        self.save_data(data)
#
#we create the excel file
    def create_data_list(self):
        #we get the data from the api
        
        # Workbook is created
        self.wb = Workbook()
        # add_sheet is used to create sheet.
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        #we write the name in the first row
        self.sheet1.write(0, 0, 'name')
        #we write the artist in the second row
        self.sheet1.write(0, 1, 'artist')
        #we write the duration in the third row
        self.sheet1.write(0, 2, 'duration')
        #we write the preview link in the fourth row
        self.sheet1.write(0, 3, 'preview_link')
        #we write the country in the fifth row
        self.sheet1.write(0, 4, 'country')
        #we write the type in the sixth row
        self.sheet1.write(0, 5, 'type')
        #we write the date in the seventh row
        self.sheet1.write(0, 6, 'date')
        #we write the bitrate in the eighth row
        self.sheet1.write(0, 7, 'bitrate')
        #we write the file format in the ninth row
        self.sheet1.write(0, 8, 'file_format')
        #we write the file size in the tenth row
        self.sheet1.write(0, 9, 'file_size')

#we call the save_data function to write the data in the right position
    def save_data(self, data):
        #we print the data we get from the api to check if we get the right data
        print(data)
        #we write data in the right position
        self.sheet1.write(self.i, 1, data[1]['artist'])
        self.sheet1.write(self.i, 0, data[0]['name'])
        self.sheet1.write(self.i, 2, data[2]['duration'])
        self.sheet1.write(self.i, 3, data[3]['preview_link'])
        self.sheet1.write(self.i, 4, data[4]['country'])
        self.sheet1.write(self.i, 5, data[5]['type'])
        self.sheet1.write(self.i, 6, data[6]['date'])
        self.sheet1.write(self.i, 7, data[7]['bitrate'])
        self.sheet1.write(self.i, 8, data[8]['file_format'])
        self.sheet1.write(self.i, 9, data[9]['file_size'])
        #we increase the row number
        self.i += 1
#we create the driver function  to call the other functions
    def driver_func(self):

        self.create_data_list()
        self.Authentification()
        #we create the excel file name
        date = datetime.datetime.now()
        file = str("spotify_track_"+date.strftime("%Y_%m_%d_%H_%M")+".xls")
                
        while True:
            try:
                self.get_data()

                #we save the file
                self.wb.save(file)
                #we make the program wait 3 minutes
                print("\n")
                for i in tqdm (range (101),
                    desc="Waiting for next song...",
                    ascii=False, ncols=75):
                    time.sleep(float(self.duration)-1.5)
                print("\n")
            except Exception as e:
                print("EXCEPTION: ",e)
                print("No song is currently playing")
                break



#main function
if __name__ == '__main__':
    SpotifyTrack()