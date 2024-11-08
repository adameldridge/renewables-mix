# Import dependencies
import requests

# Set up common vars
base_url = "https://api.carbonintensity.org.uk/generation"

# Set up fuel types
fuel_types = {
    'biomass': 'dirty',
    'coal': 'dirty',
    'gas': 'dirty',
    'hydro': 'clean',
    'imports': 'dirty',
    'nuclear': 'dirty',
    'other': 'dirty',
    'solar': 'clean',
    'wind': 'clean'}


# Get the gen mix for all fuels from the last 30 mins
def get_last_30_mins(fuel_type):

    # Get raw data
    headers = {'Accept': 'application/json'}
    json_data = requests.get(
        base_url,
        params={},
        headers=headers).json()

    gen_mix = {}

    # Get percentages for fuels based on fuel type
    for i in json_data["data"]["generationmix"]:

        if fuel_type == 'all':
            gen_mix[i["fuel"]] = i["perc"]
        elif (fuel_type == 'clean') or (fuel_type == 'dirty'):
            if fuel_types[i["fuel"]] == fuel_type:
                gen_mix[i["fuel"]] = i["perc"]

    # Handle errors
    if not gen_mix:
        results = "ERROR: Fuel type not found"
    else:
        results = gen_mix

    return results
