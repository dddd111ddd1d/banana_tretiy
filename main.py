import requests

class City:
  def __init__(self, city):
    r = requests.get("http://geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset=0&namePrefix=" + city)
    res = r.json()
    self.name = res["data"][0]["name"]
    self.lat = res[""]
    self.lon = res[""]

c = input("vedit misto:")

city = City(c)

print(city.name)