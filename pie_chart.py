def calc_parts(data, method):

    # add up all parts
    pie_parts = {}
    total = sum(data.values())

    if method == "individual":
        for key in data.keys():
            pie_parts[key] = data[key] / total * 100
    elif method == "cumulative":
        for key in data.keys():
            pie_parts[key] = data[key] / total * 100 + cumulative_total
   
   # Handle errors
    if not pie_parts:
        results = "ERROR: method not found"
    else:
        results = pie_parts

    return results
