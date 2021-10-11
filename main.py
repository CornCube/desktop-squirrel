import random
import time
import os
from tkinter import *

window = Tk()

screen_width = str(window.winfo_screenwidth())
screen_height = str(window.winfo_screenheight() - 40)
resolution = screen_width + "x" + screen_height

movement = 0

#window config
window.geometry("75x55+0+0")
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', window['bg'])
window.attributes('-topmost',True)

while True:
  event = random.randrange(0,4,1)
  if (event == 0): #left
    frameCnt = 5
    base_folder = os.path.dirname(__file__)
    image_path = os.path.join(base_folder, 'Assets', 'sqrl_left.gif')
    frames = [PhotoImage(file=image_path,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    movement = 1
  elif (event == 1): #right
    frameCnt = 5
    base_folder = os.path.dirname(__file__)
    image_path = os.path.join(base_folder, 'Assets', 'sqrl_right.gif')
    frames = [PhotoImage(file=image_path,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    movement = 2
  elif (event == 2): #up
    frameCnt = 5
    base_folder = os.path.dirname(__file__)
    image_path = os.path.join(base_folder, 'Assets', 'sqrl_up.gif')
    frames = [PhotoImage(file=image_path,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    movement = 3
  elif (event == 3): #down
    frameCnt = 5
    base_folder = os.path.dirname(__file__)
    image_path = os.path.join(base_folder, 'Assets', 'sqrl_down.gif')
    frames = [PhotoImage(file=image_path,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    movement = 4

  def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
      ind = 0
    label.configure(image=frame)
    if movement == 1 and window.winfo_x() >= 0: #left
      window.geometry("75x55+" + str(window.winfo_rootx() - 10) + "+" + str(window.winfo_rooty()))
    elif movement == 2 and window.winfo_x() <= int(screen_width) - 75: #right
      window.geometry("75x55+" + str(window.winfo_rootx() + 10) + "+" + str(window.winfo_rooty()))
    elif movement == 3 and window.winfo_y() >= 0: #up
      window.geometry("75x55+" + str(window.winfo_rootx()) + "+" + str(window.winfo_rooty() - 10))
    elif movement == 4 and window.winfo_y() <= int(screen_height) - 70: #down
      window.geometry("75x55+" + str(window.winfo_rootx()) + "+" + str(window.winfo_rooty() + 10))
    window.after(100, update, ind)

  label = Label(window)
  label.pack()
  event = random.randrange(0,4,1)
  window.after(0, update, 0)
  window.mainloop()