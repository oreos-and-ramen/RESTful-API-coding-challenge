def fix_times(data):
    for var in data["daily"]: #operating under assumtion that this will be based on daily variable
        if var == "sunrise" or "sunset":
            for i in data["daily"][var]:
                i = i.split("T", 1) # ignore past the T and just give the time
