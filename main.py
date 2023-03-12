import requests

class city:
  def __init__(self, city):
    r = requests.get("http://geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset=0&namePrefix=")
    res = r.json()
    self.name = res['data'][0]['name']


c = input("vedit misto")