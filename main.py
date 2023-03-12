import requests

class city:
  def __init__(self, city):
    r = requests/get("geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset=0&namePrefix=")
    res = r.json()
    