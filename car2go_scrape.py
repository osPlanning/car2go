# This script continuosly downloads (currently un-rented) Car2Go vehicle locations. 
# Users must first register for a Car2Go API key and specify this in the "user_key" field. 
# The script runs until stopped by the user at user-specified intervals.
#
# Author: Brice Nichols, Puget Sound Regional Council
# bnichols@psrc.org

import time
import urllib2
import json
import pandas as pd
import numpy as np

# Input parameters
download_interval = 5     # in minutes. (Don't exhaust Car2Go's patience with overly-frequent calls.) 
city = 'seattle'
user_key = 'YOUR_KEY_GOES_HERE'

# Initialize dictionary fields to store results
data_fields = {"name": [],
               "vin" : [],
               "fuel" : [],
               "exterior" : [],
               "interior": [],
               "coordinates" : [],
               "address" : []}

# Access the Car2Go API and save the results
def get_data(city, user_key):
        baseurl = 'https://www.car2go.com/api/v2.1/vehicles?loc=' \
            + city + '&oauth_consumer_key=' + user_key + '&format=json'
        page = urllib2.urlopen(baseurl)
        request_results = json.loads(page.read())
        return request_results

def main():

    request_results = get_data(city, user_key)
    data_store = np.array(request_results)

    # Save each vehicle's data in an array
    available_vehs = request_results["placemarks"]
    for line_count in range(len(available_vehs)):
        vehicle = available_vehs[line_count]
        for key, value in data_fields.iteritems(): 
            value.append(vehicle[key])
    
    # Further processing the results with a pandas dataframe  
    data = {"name": data_fields["name"],
            "vin" : data_fields["vin"],
            "fuel" : data_fields["fuel"],
            "exterior" : data_fields["exterior"],
            "interior": data_fields["interior"],
            "coordinates" : data_fields["coordinates"], 
            "address" : data_fields["address"]}

    frame = pd.DataFrame(data)

    # Save results to a time-stamped JSON file. 
    file_name = time.strftime("Data/August/%m_%d_%Y_%H_%M_%S.json")
    frame.to_json(file_name)

    # Reset variables from this loop. 
    del(request_results, data_store, frame, data)

    print "Downloading available vehicle data | " + time.strftime("%m/%d/%Y | %H:%M:%S")

# Run until script is stopped (Ctrl+C to cancel or close CMD prompt). 
# Alternatively, remove this loop and run the script with a task scheduler or some other approach.

while True:  
    main()
    time.sleep(60*download_interval)
 
