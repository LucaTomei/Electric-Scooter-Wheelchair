import tkinter as tk
from tkinter import font
import PIL.Image, PIL.ImageTk, requests, time

from manage_firmware import Manage_Firmware

cfw_obj = Manage_Firmware()

HEIGHT = 550
WIDTH = 660


def download_bg_image():
    url = "https://www.impactsurf.com/images/thumbs/002/0025731_ninebot-kickscooter-max-g30-powered_870.jpeg"
    response = requests.get(url)
    content = response.content
    cfw_obj.write_bin_file(cfw_obj.ninebot_jpeg, content)



update_status = 0

root = tk.Tk()

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def destroy():
    root.destroy()


def download_custom_firmware():
    api_link = ""


def get_firmware_informations():
    global update_status
    if update_status == 0:
        to_print = cfw_obj.params
        cfw_obj.main()
        to_print = to_print + "\n\n\n" + "Generated firmware is in Download directory.\nClick the button above to exit"
        label.config(font=('Courier', 14))
        label['text'] = to_print
        update_status = 1
        button["highlightbackground"] = "red"
        button["fg"] = "white"
        button["text"] = "EXIT"
    else:
        button["state"] = "disabled"
        button["highlightbackground"] = "grey"
        to_print = "Bye Bye"
        label['text'] = to_print
        label.after(2000, destroy)



download_bg_image()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

im = PIL.Image.open(cfw_obj.ninebot_jpeg)
photo = PIL.ImageTk.PhotoImage(im)
background_label = tk.Label(root, image=photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#87cefa", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



button = tk.Button(frame, text="Get Modified Custom Firmware", bg="gray", fg="white", font=('Courier', 14), command=lambda: get_firmware_informations())
button.place(relx=0, rely=0, relwidth=1, relheight=1)



lower_frame = tk.Frame(root, bg='#90c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

label["text"] = "Click the buttton above to\ngenerate modified custom firmware."


# Center window
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))


root.mainloop()