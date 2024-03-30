import cv2
import tkinter as tk
from PIL import Image, ImageTk
TYPES = [("File", "file"), ("Web", "web"), ("Camera", "camera")]
global video_file
class Options(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.var = tk.StringVar()
        self.var.set("OFF")
        self.buttons = [self.create_radio(c) for c in TYPES]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)


        self.entry = tk.Entry()
        self.entry.pack(padx=6,pady=6)

        self.videopath = tk.Label(text='Videopath')
        self.videopath.pack(pady=20)

        def get_entry_value():
            value = self.entry.get()
            print(value)
            self.videopath.config(text=value)

        button = tk.Button(text="Change path", command=get_entry_value)
        button.pack(pady=25)


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

class VideoPlayer:
    def __init__(self, video_file, master=None, width=100, height=100):
        video_file=self.entry.get()
        self.cap = cv2.VideoCapture(video_file)
        self.master = master
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.delay = int(1000 / self.cap.get(cv2.CAP_PROP_FPS))

    def place(self, x, y):
        self.canvas.place(x=x, y=y)
        self.update()

    def update(self):
        if button['text'] == 'stop':
            ret, frame = self.cap.read()
        else:
            self.master.after(self.delay, self.update)
            return
        if ret:
            if button['text'] == 'stop':
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.master.after(self.delay, self.update)
        else:
            self.cap.release()


def pause_unpause():
    if button['text'] == 'stop':
        button['text'] = 'play'
    else:
        button['text'] = 'stop'


window = tk.Tk()
window.geometry('1000x1000')
button = tk.Button(window, text='stop', command=pause_unpause)
button.place(x=0, y=0)
video = VideoPlayer('cats_video.mp4', master=window, width=800, height=1000)
video.place(x=50, y=0)


window.mainloop()
