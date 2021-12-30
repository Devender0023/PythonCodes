import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
					text = "CLICK ME!",
					fg = "red",
					command = lambda : print("Hello"))
button2 = tk.Button(frame,
					text = "CLICK ME!",
					fg = "red",
					command = lambda : print("Say Bye"))


button.grid()
button2.grid()

root.mainloop()