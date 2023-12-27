import os 
os.system('cls')
from colorama import Back, Style, Fore
print(Fore.GREEN+'please stand by...')

import tkinter as tk 
from tkinter import filedialog
import playsound 
from imageai.Detection import ObjectDetection
import random as rd
os.system('cls')

openFile = tk.Tk()
openFile.title('OPEN A FILE')
openFile.resizable(False, False)
openFile.geometry('200x600')

def choose_file():
    global file_path
    os.system('cls')
    file_path = filedialog.askopenfilename()
    print(Back.GREEN+'opened file: '+file_path + Style.RESET_ALL)

fileButton = tk.Button(text='OPEN FILE', command=choose_file, width=20, height=12)
fileButton.place(x=30, y=10)

#* resim işleme alanı
def process():
    detector = ObjectDetection()
    model_path = "yolov3.pt"

    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)

    detector.loadModel()

    detector.CustomObjects()

    fpath = str(rd.randint(0, 99999)) + '.png'
    global file_path

    detections = detector.detectObjectsFromImage(
        
        input_image=file_path,
        output_image_path=fpath,
        minimum_percentage_probability=30)
    
    names_list = [detection['name'] for detection in detections if 'name' in detection]

    print(names_list)
    detected = tk.Toplevel()
    n_l = tk.Label(detected, text= names_list, font='Helvetica 16')
    n_l.pack()
    os.system(fpath)
    detected.mainloop()
    

    



processButton = tk.Button(text='PROCESS IMAGE', command=process, width=20, height=12)
processButton.place(x=30, y=300)








openFile.mainloop()