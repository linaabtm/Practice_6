import tkinter as tk
TYPES = [("File", "file"), ("Web", "web"), ("Camera", "camera")]

class Options(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.var = tk.StringVar()
        self.var.set("OFF")
        self.buttons = [self.create_radio(c) for c in TYPES]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)
        self.email = tk.Label(text="VideoPath").place(x=30, y=100)
        self.entry = tk.Entry()
        self.entry.pack(padx=6,pady=6)

    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self, text=text, value=value,
                                command=self.print_option,
                                variable=self.var)

    def print_option(self):
        print(self.var.get())



def main():
    app = Options()
    app.title("Анализ видео")
    app.geometry('500x700')
    app.mainloop()

if __name__ == '__main__':
    main()
