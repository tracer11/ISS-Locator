import json
import urllib.request
import turtle
import time

def find_iss():
  url = 'http://api.open-notify.org/astros.json'
  response = urllib.request.urlopen(url)
  results = json.loads(response.read())

  astros = results['people']

  print('People in space:', results['number'])

  for a in astros:
    print(a['name'], 'is in', a['craft'])

  iss_url = 'http://api.open-notify.org/iss-now.json'
  iss_response = urllib.request.urlopen(iss_url)
  iss_results = json.loads(iss_response.read())

  iss_lat = float(iss_results['iss_position']['latitude'])
  iss_long = float(iss_results['iss_position']['longitude'])

  screen = turtle.Screen()
  screen.setup(720,360)
  screen.title('ISS-Locator')
  screen.setworldcoordinates(-180, -90, 180, 90)
  screen.bgpic('images/map.gif')

  screen.register_shape('images/iss.gif')
  iss = turtle.Turtle()
  iss.shape('images/iss.gif')
  iss.penup()
  iss.goto(iss_long, iss_lat)

  location = turtle.Turtle()
  location.penup()
  location.color('red')
  location.goto(-87.629799, 41.878113)
  location.dot(5)
  location.hideturtle()

  url = 'http://api.open-notify.org/iss-pass.json?lat=41.881832&lon=-87.623177'
  loc_response = urllib.request.urlopen(url)
  loc_results = json.loads(loc_response.read())

  over_head_time = loc_results['response'][0]['risetime']
  location.write(time.ctime(over_head_time), font=6)


  screen.exitonclick()

find_iss()
