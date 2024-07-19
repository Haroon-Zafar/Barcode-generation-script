import time
import tkinter as tk
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

def generate_barcodes(start, count):
    barcodes = []
    for i in range(start, start + count):
        barcode_value = f"C1|{i:06d}"
        barcodes.append(barcode_value)
    return barcodes

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
        time.sleep(3)

    root.destroy()

if __name__ == "__main__":
    start_number = 1
    total_barcodes = 100  # Change this value to generate a different number of barcodes
    
    barcodes = generate_barcodes(start_number, total_barcodes)
    display_barcode_images(barcodes)
