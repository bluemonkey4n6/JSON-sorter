import json
from datetime import datetime

hiValue = datetime(2000, 1, 1, 0, 0, 0)
lastTitle = None
hiTitle = None

def extract_titles(obj):
    global hiValue
    global hiTitle
    global lastTitle
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "title":
                lastTitle = value
            elif key == "firstInstallationTime":
                strpValue = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                if (hiValue < strpValue):
                    hiValue = strpValue
                    hiTitle = lastTitle
            extract_titles(value)
    elif isinstance(obj, list):
        for item in obj:
            extract_titles(item)
        
# Main routine
with open('Installs.json', 'r') as file:
    data = json.load(file)
extract_titles(data)

#print("Latest firstInstalltionTime:", hiValue)
print("Latest Title associated with latest firstInstallationTime:", hiTitle)
