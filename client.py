from tkinter import *
import requests

def sensor(sensorId):
    URL = "http://127.0.0.1:5000/get/"

    response = requests.get(url=URL).json()
    print(response)

    temperature = response.get("text")
    print(temperature)

    new_window = Tk()
    new_window.title("Sensor #" + sensorId)
    new_window.geometry('800x600')
    Label(new_window, text=temperature, font=("Helvetica", 20)).pack()

window = Tk()
window.title("Temperature Sensor")
window.geometry('1280x720')

Label(window, text="TEMPERATURE SENSOR CLIENT", font=("Helvetica", 20)).pack(pady=10)
Label(window, text="Choose a sensor to retrieve data:", font=("Helvetica", 16)).pack(pady=10)

button_frame = Frame(window)
button_frame.pack()

Button(button_frame, text="S1", command=lambda: sensor("1"), height=2, width=10).grid(row=0, column=0, padx=5)
Button(button_frame, text="S2", height=2, width=10).grid(row=0, column=1, padx=5)
Button(button_frame, text="S3", height=2, width=10).grid(row=0, column=2, padx=5)
Button(button_frame, text="S4", height=2, width=10).grid(row=0, column=3, padx=5)
Button(button_frame, text="S5", height=2, width=10).grid(row=0, column=4, padx=5)
window.mainloop()