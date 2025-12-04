# the dates and times aren't sepreated but all times start with "T" before putting the time in military time
# the daily variable in this API already includes the dates as "time", so the individuals shouldn't need the date, just the time.

# function: organize times
# input: API data dict
# output: none
# ========================
# iterate through the dictionary
#   if the key is sunrise or sunset, iterate through that
#     remove up until the "T" to isolate the times
# no need to return the dict, I will change it not make a new dict
