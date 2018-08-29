def calc_parts(data, method):

    # add up all parts
    pie_parts = {}
    total = sum(data.values())

    if method == "individual":
        for key in data.keys():
            pie_parts[key] = data[key] / total * 100
            results = sorted(pie_parts.items(), key=lambda x:x[1])
    elif method == "cumulative":
        cumulative_total = 0
        for key in data.keys():
            pie_parts[key] = data[key] / total * 100 + cumulative_total
            results = sorted(pie_parts.items(), key=lambda x:x[1])
    else:
        results = "ERROR: method not found"

    return results
