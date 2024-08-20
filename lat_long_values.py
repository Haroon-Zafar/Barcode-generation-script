import json

json
def lat_long_is_zero(json_file):
    # Parse the JSON data
    try:
        # Parse the JSON data
        with open(json_file, 'r') as file:
            file_content = file.read()
            data = json.loads(file_content)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return []
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    # Extract controlNumbers into a list
    latitude_list = []
    longitude_list = []
    try:
        for stop in data['routeSheetDTO']['stopsDTO']:
            delivery_details = stop['details'].get('deliveryDetails')
            if delivery_details:
                packages = delivery_details.get('packageDTO', [])
                for package in packages:
                    latitude_list.append(package['latitude'])
                    longitude_list.append(package['longitude'])
        # latitude_list.append(0)
                    
    except KeyError as e:
        print(f"Key error: {e}")
        return []
    if 0 or '0' in latitude_list:
        print("ZERO TRUE")
    print(latitude_list, longitude_list)
    print(len(latitude_list), len(longitude_list))
    return(0 in latitude_list, 0 in longitude_list)
    # return (latitude_list, longitude_list)

json_file = "daily_route_sheet_response.json"
lat_long_lists = lat_long_is_zero(json_file)
print(lat_long_lists)
# lat_long_is_zero()
