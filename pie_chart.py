def calc_parts(data, method):

    # add up all parts
    pie_parts = {}
    total = sum(data.values())
    cumulative_total = 0

    for key in data.keys():
        if method == "individual":
            pie_parts[key] = data[key] / total * 100
        elif method == "cumulative":
            pie_parts[key] = data[key] / total * 100 + cumulative_total
    
    if not pie_parts:
        results = "ERROR: method not found"
    else:
        results = sorted(pie_parts.items(), key=lambda x:x[1])
    
    return results
