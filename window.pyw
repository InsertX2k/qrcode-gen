from tkinter import *
import qrcode as gen
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image

def btn_clicked():
    print("Generating your QR Code, Please wait...")
    print()
    try:
        text = entry0.get()
        text = str(text)
        text = '"' + text + '"'
        qr = gen.make(text)
        
        # opening a save dialog.
        save_path = filedialog.asksaveasfilename(filetypes=(("JPG Image", "*.jpg"), ("PNG Image", "*.png"), ("GIF Image", "*.gif")))
        save_path = str(save_path) # -> converting the result to a string value.
        qr.save(save_path) # -> saving the result to the given directory(s).

        img_open = Image.open(save_path)
        img_open.show()
        messagebox.showinfo("All done", f"Successfully created the QR Code file : \n {save_path}")
        print()
        print("Generated your QR Code!")
        pass
    except Exception as excpt0:
        if save_path == '' or save_path == None:
            print("You didn't specify a path to save the generated QR Code in.")
            print()
            pass
        else:
            messagebox.showerror("An exception has occured", f"An exception has occured while trying to generate the QR Code : \nException details are : \n{excpt0}")
            print(f"\nUnable to generate the QR Code file : \n {save_path} \n Due to Exception : \n {excpt0}")
            print()
            pass

    


def call_create_qr(keybinding_arg):
    btn_clicked()

window = Tk()

window.geometry("1000x600")
window.title("Advanced QR Code Generator")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 179.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    503.0, 378.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e4e1e1",
    highlightthickness = 0)

entry0.place(
    x = 87.5, y = 342,
    width = 831.0,
    height = 71)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",
    cursor='hand2')

b0.place(
    x = 377, y = 479,
    width = 251,
    height = 62)

window.resizable(False, False)



window.bind("<F5>", call_create_qr)
window.mainloop()
