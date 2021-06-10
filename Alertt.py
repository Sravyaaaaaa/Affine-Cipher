from tkinter import * #  imports every object in Tkinter current namespace

def alert_popup(title, message):
    """Generate a pop-up window for special messages."""
    root = Tk()  # root window is created-title bars and windows
    root.title(title)  # to set the title of the popup window
    w = 400      # popup window width
    h = 200      # popup window height
    sw = root.winfo_screenwidth()    # to determine width of screen
    sh = root.winfo_screenheight()  # to determine height of screen
    x = (sw - w)/2  # makes window size half the screen size
    y = (sh - h)/2  # makes window size half the screen size
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # sets dimensions of tkinter window
    m = message
    m += '\n'
    # m += path
    w = Label(root, text=m, width=120, height=10)  # implements display boxes
    w.pack()  # packs widgets in rows,columns
    b = Button(root, text="OK", command=root.destroy, width=10)  # to add buttons and destroy-come back
    b.pack()  # packs widgets in rows,columns
    mainloop()  ## to run the Tkinter event loop continuously
# Examples
# alert_popup("Title goes here..", "Hello World!", "A path or second message can go here..")