#creating algorithm to unify 2 different data models
#This model helps to unify the two different manufacturing telemetry data models for Macora Industries.
#The goal is to create a unified data model that can be used to analyze the data from both models.
#The data models are:
#let's assume two data models are:
#Model a:Device id,timestamp,temperature,vibration level.

# model_a= {

#   "device_id":"ABC123",
#   "timestamp":"2025-07-16T14:43:00z",
#   "temperature":55.5,
#   "vibration_level":0.02
# }
#Model b:id,timestamp,temp_celcius,vibration level.

# model_b={
#   "id":"ABC123",
#   "Timestamp":"2025-07-16T14:43:00z",
#   "temp_celcius":55.5,
#   "vibration":{"level":0.02}

# }

#Now convert both models to a unified format
# Unified_Format={
#   "device_id":"ABC123",
#   "timestamp":"2025-07-16T14:43:00z",
#   "metrics":{
#     "temperature":55.5,
#     "vibration_level":0.02
#   }
# }

# Now creating python algorithm to unify the models
#importing modules
from datetime import datetime  #to convert the timestamp to iso format
from typing import Dict, Any  #to define the data type of the function

from datetime import datetime
from typing import Dict, Any


# Now defining the function named unify_model which takes a dictionary as an argument and returns a dictionary
def unify_model(
    data: Dict[str, Any]
) -> Dict[str,
          Any]:  #data is the dictionary that we are passing to the functions
    # Determine source model based on available keys
    if "device_id" in data:  #check if the key device id  is exists in the dictionary data
        # Model a   #if yes then it is model a
        unified = {  #creating a new dictionary called unified
            "device_id": data[
                "device_id"],  #we copy device_id and timestamp directly from the data dictionary
            "timestamp": data["timestamp"],
            "metrics":
            {  #we create a new nested dictionary called metrics and copy the temperature and vibration level from the data dictionary
                "temperature": data.get(
                    "temperature"
                ),  #we use get method to get the value of the key temperature and vibration level               
                "vibration_level": data.get("vibration_level")
            }
        }
    elif "id" in data:             #check if the key id exists in the model b
        # Model b
        # Using the given timestamp directly
        timestamp = data["timestamp"]                #we copy the timestamp directly from the data dictionary

        unified = {
            "device_id": data["id"],             #we use id as device_id & use the converted timestamp
            "timestamp": timestamp,
            "metrics": {
                "temperature": data.get("temp_celcius"),
                "vibration_level": data.get("vibration", {}).get("level")       #firstly safely get the vibration dictionary if missing return empty {}.
            }
        }
    else:
        raise ValueError("Unknown data model format")          #if neither deviceid nor id found then raise an error

    return unified         #send the new dictionary back to the caller

# Example data for model a
#example data for testing the function
#simulated data for a device following Model A
model_a = {
    "device_id": "ABC123",
    "timestamp": "2025-07-16T14:43:00z",
    "temperature": 55.5,
    "vibration_level": 0.02
}

# Example data for model b
#simulated data for a device following Model B
model_b = {
    "id": "XYZ789",
    "timestamp": "2025-07-16T15:55:00z",
    "temp_celcius": 60.0,
    "vibration": {
        "level": 0.03
    }
}

# Call the function and print output
#print unified dictionary for model a and model b
output_a = unify_model(model_a)
print("Unified Model A Output:")
print(output_a)

print("\nUnified Model B Output:")
output_b = unify_model(model_b)
print(output_b)
