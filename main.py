import json
import urllib.request
import turtle
import time

def find_iss():
  #url for astronauts in space
  url = 'http://api.open-notify.org/astros.json'
  #url for current location of iss
  iss_url = 'http://api.open-notify.org/iss-now.json'
  #url for overhead times in Chicago
  iss_ovh_url = 'http://api.open-notify.org/iss-pass.json?lat=41.878113&lon=-87.629799'

  #get list of astronauts in space
  iss_astros = json_results(url)
  astros = iss_astros['people']

  #prints out how many astros are currenlty in space
  print('People in space:', iss_astros['number'])
  #prints out each atsor name and what craft they are in
  for a in astros:
    print(a['name'], 'is in', a['craft'])

  #screen setup
  screen = turtle.Screen()
  screen.setup(720,360)
  screen.title('ISS-Locator')
  screen.setworldcoordinates(-180, -90, 180, 90)
  screen.bgpic('images/map.gif')

  #assigns current ISS lat and long to variables to be used later
  iss_pos = json_results(iss_url)
  iss_lat = float(iss_pos['iss_position']['latitude'])
  iss_long = float(iss_pos['iss_position']['longitude'])

  #sets a turtle at current ISS position
  screen.register_shape('images/iss.gif')
  iss = turtle.Turtle()
  iss.shape('images/iss.gif')
  iss.penup()
  iss.goto(iss_long, iss_lat)

  #makes a dot at city of choice, Chicago atm
  location = turtle.Turtle()
  location.penup()
  location.color('red')
  location.goto(-87.629799, 41.878113)
  location.dot(5)
  location.hideturtle()

  #prints out the next time the ISS will be over a city
  iss_ovh = json_results(iss_ovh_url)
  over_head_time = iss_ovh['response'][0]['risetime']
  location.write(time.ctime(over_head_time), font=6)


  screen.exitonclick()


def json_results(url):
  response = urllib.request.urlopen(url)
  results = json.loads(response.read())
  return results


find_iss()









