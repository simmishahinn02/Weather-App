from tkinter import *
import requests
import time


def getWeather(canvas):
    cityName = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    weather_info = condition + "\n" + str(temp) + "°C"
    weather_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=weather_info)
    label2.config(text=weather_data)



canvas = Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
#canvas.iconbitmap()

bg= PhotoImage(file='weather.png')
img= Label(canvas, image=bg)
img.place(x=0, y=0, relwidth=1, relheight=1)
f1 = ("poppins", 35, "bold")
f2 = ("poppins", 25, "bold")
f3 = ("poppins", 15, "bold")

textField = Entry(canvas, justify='center', width=20,fg="red", font=f1)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = Label(canvas, font=f2)
label1.pack()
label2 = Label(canvas, font=f3)
label2.pack()

canvas.mainloop()