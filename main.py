import tkinter as tk
import requests

API_KEY = "b2f743ba3c4b4318dc6da37a00cb4007"

def get_weather(location_query):
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={location_query}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return f"Error: {data['error']['info']}"

    location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
    description = data['current']['weather_descriptions'][0]
    temperature = data['current']['temperature']
    feels_like = data['current']['feelslike']
    humidity = data['current']['humidity']
    local_time = data['location']['localtime']

    return (f"Location: {location}\n"
            f"Condition: {description}\n"
            f"Temperature: {temperature}°C (feels like {feels_like}°C)\n"
            f"Humidity: {humidity}%\n"
            f"Local Time: {local_time}")


def show_weather():
    city = entry.get().strip()
    if city:
        result = get_weather(city)
        output_label.config(text=result)

root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("700x500")
root.resizable(True, True)


tk.Label(root, text="Enter ZIP Code or DD Coordinates:", font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
output_label.pack(pady=10)

root.mainloop()
