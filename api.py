import tkinter as tk
from tkinter import ttk
import requests

def create_widgets(root, get_weather):
    city_label = ttk.Label(root, text="City:")
    city_label.grid(row=0, column=0)

    city_entry = ttk.Entry(root)
    city_entry.grid(row=0, column=1)

    v = ["Niagara falls","Fort erie","Toronto","Hamilton"]
    cb = ttk.Combobox(="select a city",values=v)
    cb.grid(row=3, column=2)

    get_weather_button = ttk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()))
    get_weather_button.grid(row=0, column=2)

    weather_tree = ttk.Treeview(root, columns=("Temperature", "Description"))
    weather_tree.heading("#0", text="City")
    weather_tree.heading("Temperature", text="Temperature (°C)")
    weather_tree.heading("Description", text="Weather Description")
    weather_tree.grid(row=1, column=0, columnspan=3)
    return weather_tree

def get_weather(city, weather_tree, api_key, option):
    if city:
        try:
            url = f"http://api.openweathermap.org/data/2.5/{option}?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            temperature = f"{data['main']['temp']}°C"
            description = data['weather'][0]['description']

            weather_tree.insert("", "end", text=city, values=(temperature, description))
        except Exception as e:
            print("Error:", e)
    else:
        print("Please enter a city.")

def run():
    root = tk.Tk()
    root.title("Weather App")

    api_key = 'b3dc1e50a6bd71afbbd99555bb2034ba'

    weather_tree = create_widgets(root, lambda city: get_weather(city, weather_tree, api_key, 'weather'))

    root.mainloop()

if __name__ == "__main__":
    run()