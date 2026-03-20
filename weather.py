import requests
api_key = "c3181bf6028e02ecb4a7e5847b181a5c"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Error:", response.text)
else:
    try:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather}")
    except:
        print("Invalid response format")