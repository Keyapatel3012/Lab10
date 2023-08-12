import requests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk 
from poke_api import get_pokemon_info



# Function to set the desktop background
def set_desktop_background(image_path):
    try:
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Desktop background set successfully.")
    except Exception as e:
        print("Error setting desktop background:", str(e))

# Function to handle button click event
def set_desktop_image():
    selected_pokemon = combo_var.get()
    if selected_pokemon:
        poke_info = get_pokemon_info(selected_pokemon)
        if poke_info:
            image_url = poke_info['sprites']['other']['official-artwork']['front_default']
            response = requests.get(image_url)
            if response.status_code == requests.codes.ok:
                image_data = response.content
                image_path = selected_pokemon + ".png"
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data)
                set_desktop_background(image_path)
                print("Image saved and set as desktop background.")

# Create the main window
root = Tk()
root.title("Pokemon Image Viewer")
root.resizable(False, False)

# Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frame_image = ttk.LabelFrame(root, text="Image")
frame_image.grid(row=1, column=0, padx=10, pady=10)

# Populate the user input frame with widgets
label_name = ttk.Label(frame_input, text="Select a Pokemon:")
label_name.grid(row=0, column=0, padx=5, pady=5)

# Create a Combobox to select Pokemon names
pokemon_list = ["Pikachu", "Charmander", "Squirtle"]  # You can add more Pokemon names
combo_var = StringVar()
combo_box = ttk.Combobox(frame_input, textvariable=combo_var, values=pokemon_list)
combo_box.grid(row=0, column=1, padx=5, pady=5)

btn_set_image = ttk.Button(frame_input, text="Set as Desktop Image", command=set_desktop_image)
btn_set_image.grid(row=0, column=2, padx=5, pady=5)

# Define a callback function for the Combobox selection event
def combo_selected(event):
    selected_pokemon = combo_var.get()
    if selected_pokemon:
        poke_info = get_pokemon_info(selected_pokemon)
        if poke_info:
            image_url = poke_info['sprites']['other']['official-artwork']['front_default']
            response = requests.get(image_url)
            if response.status_code == requests.codes.ok:
                image_data = response.content
                image = PhotoImage(data=image_data)
                image_label.config(image=image)
                image_label.image = image  # Keep a reference to prevent garbage collection
                btn_set_image['state'] = 'normal'  # Enable the button

# Create an image label in the image frame
image_label = ttk.Label(frame_image)
image_label.grid(row=0, column=0, padx=10, pady=10)

# Bind the Combobox selection event to the callback function
combo_box.bind("<<ComboboxSelected>>", combo_selected)

root.mainloop()