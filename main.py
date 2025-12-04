# Will later add sys for user control
import json

from get_data import get_data
from clean_data import clean_data
from change_data import fix_times

def main():
    raw_data = get_data() # will later add sys as arguments
    cleaned_data = clean_data(raw_data) # second arg can be sys later
    fix_times(cleaned_data)
  
    return json.dumps(cleaned_data, indent=1)
    # finished product, ready for use :)

print(main())
