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
        gen_mix[i["fuel"]] = i["perc"]

    return gen_mix
