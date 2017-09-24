from onwrapper import OpenNotify

def test_astronauts():
	"""
	Tests the functionality of the astronauts API call.
	"""
	open_notify = OpenNotify()
	num_of_astronauts, astronauts = open_notify.astronauts()
	assert type(num_of_astronauts) == int
	#test