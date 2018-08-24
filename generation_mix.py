# Import dependencies
import requests

# Set up common vars
base_url = "https://api.carbonintensity.org.uk/generation"


# Get the gen mix from the last 30 mins
def get_last_30_mins():

    # Get raw data
    headers = {'Accept': 'application/json'}
    json_data = requests.get(
        base_url,
        params={},
        headers=headers).json()

    gen_mix = {}

    # Parse data
    for i in json_data["data"]["generationmix"]:
        if i["fuel"] == "biomass":
            gen_mix["biomass"] = i["perc"]
        elif i["fuel"] == "coal":
            gen_mix["coal"] = i["perc"]
        elif i["fuel"] == "imports":
            gen_mix["imports"] = i["perc"]
        elif i["fuel"] == "gas":
            gen_mix["gas"] = i["perc"]
        elif i["fuel"] == "nuclear":
            gen_mix["nuclear"] = i["perc"]
        elif i["fuel"] == "other":
            gen_mix["other"] = i["perc"]
        elif i["fuel"] == "hydro":
            gen_mix["hydro"] = i["perc"]
        elif i["fuel"] == "solar":
            gen_mix["solar"] = i["perc"]
        elif i["fuel"] == "wind":
            gen_mix["wind"] = i["perc"]

    return gen_mix
