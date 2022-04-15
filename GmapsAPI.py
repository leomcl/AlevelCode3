import requests

# API key
api_key = 'AIzaSyAgQIoMkAZx-C2N8dj04CjtKzT8guuqSos'


def estimatedTime(address1, address2):
    # base url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

    # get response
    r = requests.get(url + "origins=" + address1 + "&destinations=" + address2 + "&key=" + api_key)

    # return time as text and as seconds
    #time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    #print(time)
    print(seconds)

    return seconds
    # print the travel time
