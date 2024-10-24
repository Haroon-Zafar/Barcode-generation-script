import time
import tkinter as tk
import json
# always do this >> from file_name import module name 
from control_number_json_extractor import control_number_json_extractor_method 
from tracking_number_json_extractor import tracking_number_json_extractor_method 
from PIL import Image, ImageTk 
import barcode 
# from barcode import ImageWriter 
from barcode.writer import ImageWriter
from io import BytesIO

# control_numbers = [13036279, 12973357, 13044726, 12906422, 12970010, 12970012, 12931597, 13077059, 13078048, 13028923, 13028953, 13031734, 13049053, 12907270, 13054229, 13079990, 13076948, 12962311, 13043825, 13060564, 13030395, 13048393, 13046479, 13063071, 13069494, 13070817, 13070827, 13070932, 13072497, 13073392, 13066827, 13073927, 13068505, 13070472, 13028280, 12965116, 12964672, 12922988, 13042647, 13025485, 13014798, 12902087, 13020307, 13073828, 13057655, 13057766, 12952279, 13058180, 13054177, 12903927, 12956852, 13024233, 13024622, 12965517, 13012637, 13035964, 13054111, 13066327, 13071011, 13076777, 13043152, 13020331, 13023329, 13026230, 13039155, 13039580, 12946363, 12951910, 12908138, 12917434, 12902958, 13057244, 13057273, 13078846, 13044800, 13049596, 13044305]


# def generate_barcodes(start, count):
#     barcodes = []
#     for i in range(start, start + count):
#         barcode_value = f"C1|{i:06d}"
#         barcodes.append(barcode_value)
#     return barcodes

# CODE SNIPPET FOR DYNAMIC CONTROL NUMBERS 
def generate_barcodes(numbers, user_choice):
    barcodes = []
    if user_choice == 1:        
        for control_number in numbers:
            if user_choice == 1:
                barcode_value = f"C1|{control_number}"
                barcodes.append(barcode_value)
    return barcodes

    # elif user_choice == 2:        
    #     for key_value in numbers:
    #         if user_choice == 1:
    #             print(key_value)
    #             barcode_value = f"T1|{account_number}|{tracking_number}"
    #             barcodes.append(key_value)
    # else:
    #     print("Input for User Choice is not valid")

# # CODE SNIPPET FOR DYNAMIC TRACKING NUMBERS 
# def generate_barcodes(tracking_numbers):
#     barcodes = []
#     for tracking_number in tracking_numbers:
#         print(tracking_number)
#         # barcode_value = f"C1|{account_number}|{tracking_numbers}"
#         # barcodes.append(barcode_value)
#     return barcodes

def create_barcode_image(barcode_value):
    code128 = barcode.get('code128', barcode_value, writer=ImageWriter())
    buffer = BytesIO()
    code128.write(buffer)
    buffer.seek(0)
    return Image.open(buffer)

def display_barcode_images(barcodes):
    root = tk.Tk()
    root.title("Barcode Display")
    label = tk.Label(root)
    label.pack()

    for barcode_value in barcodes:
        image = create_barcode_image(barcode_value)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        root.update()
        time.sleep(1.5)

    root.destroy()

if __name__ == "__main__":

    # start_number = 1
    # total_barcodes = 1000  # Change this value to generate a different number of barcodes
    # barcodes = generate_barcodes(start_number, total_barcodes)
    print("To search using Control Numbers, Type 1", "\n"+"To search using Tracking Numbers, Type 2")
    user_choice = int(input(">>"))

    if user_choice == 1:
        json_file_path = "daily_route_sheet_response.json" 
        control_numbers = control_number_json_extractor_method(json_file_path)
        barcodes = generate_barcodes(control_numbers, user_choice)
        display_barcode_images(barcodes)

        
    elif user_choice == 2:
        json_file_path = "daily_route_sheet_response.json" 
        tracking_numbers = tracking_number_json_extractor_method(json_file_path)
        barcodes = generate_barcodes(tracking_numbers, user_choice)
        display_barcode_images(barcodes)
    
