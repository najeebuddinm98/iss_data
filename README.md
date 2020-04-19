# International Space Station Data

This script uses the opensource [**Open-Notify API**](http://open-notify.org/Open-Notify-API/) in order to get the data from the **International Space Station** regarding its current location, the names of the astronauts in it and when it will pass a given location along with duration of passage. 

The script asks for the *name of any city* as input from the user. We use the [Geocode API](https://geocode.xyz/api) to get the coordinates of the entered city name. These are used for third information printed i.e. the duration and date of passage over a given location.

*Further changes* can be made to the code: like taking latitude and longitude values directly from the user; getting input from the clipboard; storing the data in a text file/document or calling the ```retrieval``` function from the ``getweather.py`` script.