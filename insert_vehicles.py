import pypyodbc

from vehicles import Vehicles

# Create new instance of Vehicle utility class
vehicles = Vehicles()

# Download vehicle data from Edmunds API 
vehicle_data = vehicles.get_data()  

# Create database connection string for iSeries ODBC driver
connection_string = "Driver={iSeries Access ODBC Driver}; System=iseries; Uid=user1; Pwd=password1;"

# iterate over each element in the vehicle_data collection
for record in vehicle_data:
	try:
        # connect to the database using the connection and create a cursor to execute SQL 
		conn = pypyodbc.connect(connection_string)
		cur = conn.cursor()
        
        # use the cursor to execute the insert statement 
		cur.execute("INSERT INTO PARKLOT.VEHICLE (YEAR, MAKE, MODEL, STYLE) VALUES ('{}', '{}', '{}', 'Other Do Not Know') WITH NONE".format(record["year"], record["make"], record["model"]))
        
        # print the data that was inserted
		print("INSERTED ('{}', '{}', '{}', 'Other Do Not Know')".format(record["year"], record["make"], record["model"]))
	except Exception as e:
        # print any data that already exists
		print("Skipping ('{}', '{}', '{}'). Data already exists!\n".format(record["year"], record["make"], record["model"]))

