import json

def tracking_number_json_extractor_method(json_file=""):
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
    
    # Extract trackingNumbers into a list
    tracking_numbers = {}
    try:
        for stop in data['routeSheetDTO']['stopsDTO']:
            delivery_details = stop['details'].get('deliveryDetails')
            if delivery_details:
                packages = delivery_details.get('packageDTO', [])
                for package in packages: 
                    package['trackingNumber'] = package['accountNumber']
                    # tracking_numbers.append(package['trackingNumber'])
    except KeyError as e:
        print(f"Key error: {e}")
        return []
    return (tracking_numbers)

# json_file = "daily_route_sheet_response_S01162A.json"
# tracking_numbers = json_extractor()
# print(tracking_numbers)
# json_extractor()
