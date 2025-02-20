import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time
from working import fin_list  # Assuming fin_list is the function that returns the list of alphabet.jpg

def start_conversion():
    messagebox.showinfo("Info", "Recording started...")
    # Call the function to get the list of alphabet.jpg format names
    alphabet_list = fin_list()
    messagebox.showinfo("Info", "Recording stopped. Processing...")

    # Display images and build the sentence
    sentence = ""
    for alphabet in alphabet_list:
        img_path = os.path.join("hand sign for A - Z", alphabet)
        img = Image.open(img_path)
        img = img.resize((300, 300), Image.ANTIALIAS)  # Increase size by 150%
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img
        root.update()
        time.sleep(1)

        if alphabet == "space.jpg":
            sentence += " "
        else:
            sentence += alphabet.split('.')[0]
        sentence_label.config(text=sentence)
        root.update()

# Create the main window
root = tk.Tk()
root.title("Speech to Sign Language Converter")
root.geometry("500x700")  # Adjust window size to accommodate larger images

# Create and place the button
convert_button = tk.Button(root, text="Convert Speech to Sign", command=start_conversion)
convert_button.pack(pady=20)

# Create and place the heading label
heading_label = tk.Label(root, text="SIGN LANGUAGE", font=("Helvetica", 18, "bold"))
heading_label.pack(pady=10)

# Create and place the image label
img_label = tk.Label(root, width=300, height=300, bd=2, relief="solid")
img_label.pack(pady=20)

# Create and place the sentence heading label
sentence_heading_label = tk.Label(root, text="YOUR SENTENCE ", font=("Helvetica", 16, "bold"))
sentence_heading_label.pack(pady=10)

# Create and place the sentence label
sentence_label = tk.Label(root, text="", font=("Helvetica", 16, "italic"))
sentence_label.pack(pady=10)

# Run the application
root.mainloop()
