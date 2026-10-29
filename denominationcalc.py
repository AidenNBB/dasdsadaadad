from tkinter import *
from tkinter import messagebox

try:
    from PIL import Image, ImageTk  # type: ignore
except ImportError:
    Image = None
    ImageTk = None

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

if Image is not None and ImageTk is not None:
    try:
        upload = Image.open("app_img.jpg")
        upload = upload.resize((300, 300))
        image = ImageTk.PhotoImage(upload)
    except Exception:
        image = None
else:
    image = None

if image is not None:
    label = Label(root, image=image, bg="light blue")
else:
    label = Label(root, text="Image unavailable", bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application",
    bg="light blue",
    font=("Arial", 12),
)
label1.place(x=120, y=330)



def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(
        top,
        text="Here are number of notes for each Denomination",
        bg="light grey",
    )
    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please Enter a number.")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=120)
    l1.place(x=140, y=170)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)


topwin()
root.mainloop()