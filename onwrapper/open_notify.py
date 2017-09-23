import requests
#to do: have exceptions if return code not 200 or message not success
class OpenNotify(object):
	"""
	A Python wrapper for the Open Notify API.
	http://http://open-notify.org/
	"""

	def astronauts(self):
		"""
		Returns the number of people currently in spcace.
		Returns a list of all the astronauts and their spacecraft.
		"""
		endpoint = "http://api.open-notify.org/astros.json"
		response = requests.get(endpoint)

		return (response.json()["number"],
			    response.json()["people"])

	def location(self):
		"""
		Returns the current longitude and latitude of the ISS.
		"""
		endpoint = "http://api.open-notify.org/iss-now.json"
		response = requests.get(endpoint)
		print(response.json())

		return (response.json()["iss_position"]["longitude"],
			    response.json()["iss_position"]["latitude"])

	def pass_prediction(self, latitude, longitude, n):
		"""
		Returns the pass times/dates for given coordinates.
		"""
		endpoint = "http://api.open-notify.org/iss-pass.json?lat={}&lon={}&alt=20&n={}".format(latitude, longitude, n)
		response = requests.get(endpoint)

		return response.json()

print "poodle test"