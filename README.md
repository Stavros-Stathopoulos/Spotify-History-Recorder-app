# Spotify History Recorder app
 Its an app that creates a CSV file with the songs you listen in a single spotify session. It requires internet connection and online Spotify streaming. Its been tested and working perfectly with Spotify Premium

Requires:

	PYTHON 3.10.0  		 	 https://www.python.org/downloads/release/python-3100/
	spotipy module V. 2.22.1 https://pypi.org/project/spotipy/
	xlwt module V. 1.3.0	 https://pypi.org/project/xlwt/
	tqdm  module V. 4.65.0
	datetime module
	time module
	decimal module
	
	IMPORTAND NOTE: Downlad from Command Prompt for Windows using Administrative lunch, using pip install MODULE_NAME

To lunch:  

	1) Register in spotify for developers  https://developer.spotify.com/
	2) Create an app
	3) After creating an app go to settings  
	4) Copy your Cient ID and REPLACE_YOUR_CLIENT_ID in the python script named credentials.py
	5) Copy your Cient secret and REPLACE_YOUR_CLIENT_SECRET in the python script named credentials.py
	6) In the dashboard replace Redirect URIs with http://localhost:9000 Or a URI of your preference in the script named credentials.py
	7) Save settings
	8) Make sure that the files convert_bitrate_to_size.py, credentials.py and time_converters.py are in the same directory
	9) Lunch the python script

	IMPORTAND NOTE: You may need to manualy give access to your aplication.
			1) Go to settings -> User Managment
			2) Enter user using your Name and Email, as you used them in your spotify account

#Contact
Stavros Stathopoulos mail: astatho97@gmail.com  Discord: 𝕌𝕜𝕟𝕠𝕨𝕟.𝕖𝕩𝕖#0203
Project Link: https://github.com/Stavros-Stathopoulos/Spotify-History-Recorder-app
All copyrights reserved
