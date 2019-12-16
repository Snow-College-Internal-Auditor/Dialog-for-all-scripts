import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Select file:", anchor="w")
        #self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit")
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
        self.prompt.pack(side="top", fill="x")
        # lay the widgets out on the screen. 
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")
        

    

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()