import requests

def get_weather():
    print("--- Basic Weather App ---")
    
    # You will need to sign up at openweathermap.org to get a free API key
    api_key = "YOUR_API_KEY_HERE"
    city = input("Enter the name of the city: ")
    
    # API URL
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] == 200:
            # Extract basic information
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {desc.capitalize()}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_weather()
