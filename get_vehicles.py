import json
import urllib.parse
import urllib.request
import datetime

#
# Vehicle Class utility class uses edmunds Vehicle API to get a list of vehicles made for a given year
# 
class Vehicles:
    # Configure Vehicle API URL and request parameters
	base_url = "https://api.edmunds.com/api/vehicle/v2/makes?"
	api_key = "UNIQUEAPIKEY"
	current_year = datetime.datetime.now().year
	next_year = current_year + 1
	years = {current_year, next_year}	


	def __init__(self):
		pass

    # 
    # get_data()
    # Returns an array of vehicles
    #
	def get_data(self):
		vehicles = []
		try:
            # get vehicle data for each year 
			for year in self.years:
                
                # create a request to the API and get a response
				url_vars = {"year": year, "view": "basic", "fmt": "json", "api_key": self.api_key}
				data_url = self.base_url + urllib.parse.urlencode(url_vars)
				response = urllib.request.urlopen(data_url)
                
                # convert bytes to utf-8 encoded string
				str_response = response.readall().decode("utf-8")  
                
                # create vehicle data object fromm JSON string 
				jsonData = json.loads(str_response)
                
                # Retrive all vehicle makes Acura, Audi, BMW, etc.  
				vehicleMakes = jsonData.get("makes") 
                
                # Iterate over each make
				for item in vehicleMakes: 
                    # Iterate over every model in each make
					for model in item["models"]:  
						year = model["years"][0]["year"]
						make = item["name"]
						model = model["name"]
                        
                        #append item to vehcile array
						vehicles.append({"year": year, "make": make, "model": model})
		except Exception as e:
			print(e)
        
		return vehicles
# 
# Main 
#
if __name__ == '__main__':
	v = Vehicles()
	vehicles = (v.get_data())
	print(vehicles)
	for vehicle in vehicles:
		print("Year: {year} Make: {make} Model: {model}".format(**vehicle))
