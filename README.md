# RESTful-API-coding-challenge
A RESTful API middleman for a public API




## Requirements Analysis
------------------------

### Instructions
I chose option B. I will be creating an API middleman using RESTful principles connecting to a public API. I will fetch thew data and clean it up, restructuring it to return specific data in a JSON structure. I will implement a serverside feature, converting an element of the data before returning it. Lastly, I will document simple and straightforward instructions of how to test the desired endpoint of the program.

The API I will be using will be the Weather API and I will focus this information:
-  Sunrise and Sunset

### What I know how to do
I Know how to clean up data after having access to it. The way I've done it before was by using CSV files and the pythons read function.

### What I don't know how to do
I haven't accessed an API myself before and I don't know how to return the data as a JSON again.

To remidy these issues, I went to the free ChatGPT and did aproximately 30 minutes of research on API structure and and how to access data in API's. I also looked into how to convert back into JSON structure after dealing with data.

## Psuedocode

I'm going to create a raw dictionary of the data from the API, cut out unwanted data, modify temps to fahrenheit, and return the cleaned data

main file (returning the finished product)
```
imports: json

hardcoded variables for the functions

call function to get data from API => create python dictionary object (lets call this raw_data)
  (this will need the lat and long of the area, I will hardcode this to Salt Lake City)
call function to clean data => create python dict (lets call this clean_data)
  (this will need a list of items the user wants to keep, I will hardcode this)
  (this will also need the dictionary from the API data)
call function to change data => create python dict (lets call this changed_data)

use the json dumps feature to change the changed_data dict to JSON output
save this new JSON data (lets call this json_finished_data)

print that the object was succesfully created
```

get data file (the function to get the data from public API)
(I will hardcode the weather API into this function)
```
imports: requests

function: get_data
input: latitude, longitude
output: python dict
===================
get the response from the API by calling the URL with proper params
parse the response into python dict
return the python dict
```

clean data file (remove unnecessary stuff)
```
# i dont want any of the internal data such as generationtime so I will clear all of that
# for simplicities sake, I look through the dict and save things I want, and ignore the things I don't

function: clean_data
input: list of information to keep, API data (uncleaned) dict
output: python dict
==================================
create new (empty) dict
iterate through the uncleaned dict
  if the key matches something on the keep list, add it to the new dict
  ignore if it doesn't

return the new dict
```

change data file (reformat dates and time)
```
# the dates and times aren't sepreated but all times start with "T" before putting the time in military time
# the daily variable in this API already includes the dates as "time", so the individuals shouldn't need the date, just the time.

function: organize times
input: API data dict
output: none
========================
iterate through the dictionary
  if the key is sunrise or sunset, iterate through that
    remove up until the "T" to isolate the times
# no need to return the dict, I will change it not make a new dict
```

## Implementation
-----------------
I started with get_data. The first issue I ran into was a minor type with a "." and a ",", which I fixed quickly. After that the error I received was as follows:
`{'error': True, 'reason': "Data corrupted at path ''. Cannot initialize ForecastVariableDaily from invalid String value sunrise, sunset."}`
I, like I mentioned before, haven't gotten information from API's before so I wans't sure where my issue was. I showed my code to ChatGPT, where it said that some API's prefer no spaces in strings. I changed it and it worked from there.

The clean_data file was straight forward enough. I didn't have any notable issues in writing this one. 

**Note:** I wrote in my pseudocode that I would hardcode the variables in main, but I now believe that defaults for the functions works better. I will be doing that instead.
