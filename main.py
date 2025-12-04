# Will later add sys for user control
import json

from get_data import get_data
from clean_data import clean_data

def main():
  raw_data = get_data() # will later add sys as arguments
  clean_data = clean_data(raw_data) # second arg can be sys later

  # call function to change data => this will just change the dict

  return json.dumps(clean_data)
  # finished product, ready for use :)

main()
