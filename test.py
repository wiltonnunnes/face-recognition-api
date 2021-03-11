from tkinter import *
import cv2 as cv
import numpy as np
from PIL import Image, ImageTk

class Application(Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.take_photo = Button(self)
    self.take_photo["text"] = "Take photo"
    self.take_photo["command"] = self.take_photo
    self.take_photo.pack(side = BOTTOM)

  def take_photo(self):
    print("Hello")

root = Tk()
app = Application(master=root)
app.mainloop()