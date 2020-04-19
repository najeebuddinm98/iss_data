#get information from the International Space Station

import requests, json, datetime, os

#DO: function that takes url and returns json data as a dictionary
def retrieval(url):
    response=requests.get(url)
    response.raise_for_status()
    data=json.loads(response.text)
    return data

#DO: function that returns the latitude and longitude using Geocode API
def get_coordinates(cityname):
    loc=cityname.lower().replace(' ','+')
    urlGC='https://geocode.xyz/%s?json=1' %(loc)
    coord=retrieval(urlGC)
    #DEBUG: print(coord)
    return coord

#DO: get the response using requests
if __name__=="__main__":
    cn=input('Enter city name: ')
    coordinates=get_coordinates(cn)

    urlAstro='http://api.open-notify.org/astros.json'
    urlPass='http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' %(coordinates['latt'],coordinates['longt'])
    urlLoc='http://api.open-notify.org/iss-now.json'

    dataAstro=retrieval(urlAstro)
    dataPass=retrieval(urlPass)
    dataLoc=retrieval(urlLoc)
    #DEBUG: print(dataAstro, dataPass, dataLoc)

    #DO: print it in proper format using datetime module
    stamp=datetime.datetime.now()

    print('The ISS is at lat&long= ',dataLoc['iss_position']['latitude'],' ',dataLoc['iss_position']['longitude'],' at ',stamp)
    print('\nThe name of the astronauts are:')
    for i in dataAstro['people']:
        print(i['name'])
    print('\nThe ISS will pass above %s on:' %(cn.title()))
    for j in dataPass['response']:
        print(datetime.datetime.fromtimestamp(j['risetime']),' for ',j['duration'],' seconds')

    os.system('cmd /k "pause"') #useful when running from terminal




