
#Import dependencies
import requests
import json
import db_connector


def update():

	# Get raw data
	headers = {
	  'Accept': 'application/json'
	}
	json_data = requests.get('https://api.carbonintensity.org.uk/generation', params={}, headers = headers).json()
	
	#Store data
	start_date = json_data["data"]["from"]
	end_date = json_data["data"]["to"]

	for i in json_data["data"]["generationmix"]:
		if i["fuel"] == "biomass":
			biomass = i["perc"]
		elif i["fuel"] == "coal":
			coal = i["perc"] 
		elif i["fuel"] == "imports":
			imports = i["perc"]
		elif i["fuel"] == "gas":
			gas = i["perc"]
		elif i["fuel"] == "nuclear":
			nuclear = i["perc"]
		elif i["fuel"] == "other":
			other = i["perc"]
		elif i["fuel"] == "hydro":
			hydro = i["perc"]
		elif i["fuel"] == "solar":
			solar = i["perc"]
		elif i["fuel"] == "wind":
			wind = i["perc"]

	print "start_date: " + start_date
	print "end_date: " + end_date
	print "biomass: " + str(biomass)
	print "coal: " + str(coal)
	print "imports: " + str(imports)
	print "gas: " + str(gas)
	print "nuclear: " + str(nuclear)
	print "other: " + str(other)
	print "hydro: " + str(hydro)
	print "solar: " + str(solar)
	print "wind: " + str(wind)

	# COnnect to database
	conn = db_connector.create_connection()
	curs = conn.cursor()

	#Create table if it doesn't exist
	curs.execute("CREATE TABLE IF NOT EXISTS generation_mix(" +
		"id integer PRIMARY KEY," +
		"start_date text," +
		"end_date text," +
		"biomass real," +
		"coal real," +
		"imports real," +
		"gas real," +
		"nuclear real," +
		"other real," +
		"hydro real," +
		"solar real," +
		"wind real);")

	conn.commit()
	
	#Insert values into table
	curs.execute("INSERT INTO generation_mix(" +
		"start_date," +
		"end_date," +
		"biomass," +
		"coal," +
		"imports," +
		"gas," +
		"nuclear," +
		"other," +
		"hydro," +
		"solar," +
		"wind) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
		(start_date,
		end_date,
		biomass,
		coal,
		imports,
		gas,
		nuclear,
		other,
		hydro,
		solar,
		wind))

	# Finalise DB updates
	conn.commit()
	conn.close()

#def get():
	# conn = connect('renewables_mix.db')
	# curs = conn.cursor()
	# curs.execute("SELECT lastname FROM employees;")
	# for (name) in curs.fetchall():
	#     print name

