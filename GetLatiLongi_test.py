import GetLatiLongi
def test_GetLatiLongi():
	assert GetLatiLongi.GetLatiLongi().__str__() in "{'ww': [-180, -90, 180, 90], 'us': [-120, 30, -75, 50]}"
	
def test_GetLatiLongi1():
	assert GetLatiLongi.GetLatiLongi1('latitude_longitude').__str__() in "{'ww': [-180, -90, 180, 90], 'us': [-120, 30, -75, 50]}"
	assert GetLatiLongi.GetLatiLongi1('latitude_longitude2').__str__() in "{'Svalbard': [78, 55, 11, 56], 'Greenland': [71, 18, 156, 46], 'Alaska': [70, 12, 148, 31], 'Nunavut': [79, 59, 85, 56]}"
	

