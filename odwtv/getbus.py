import requests
from datetime import datetime, timezone

def get_stationboard_for_beringen_sonne():
    api_url = "http://transport.opendata.ch/v1/stationboard"
    station_name = "Beringen, Sonne"

    params = {
        "station": station_name,
        "limit": 5  # You can adjust the limit to get more or fewer connections
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        stationboard = data.get("stationboard", [])

        if stationboard:
            print(f"Next connections at {station_name}:")
            for connection in stationboard:
                departure_time = connection["stop"]["departure"]
                time_until_departure = calculate_time_until_departure(departure_time)
                
                print(f"Bus: {connection['name']}")
                print(f"Destination: {connection['to']}")
                print(f"Departure Time: {departure_time} ({time_until_departure} until departure)")
                print("-------------------------")
        else:
            print(f"No upcoming connections at {station_name}.")
    else:
        print(f"Error: {response.status_code}")

def calculate_time_until_departure(departure_time):
    current_time = datetime.now(timezone.utc)
    departure_datetime = datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S%z")
    time_until_departure = departure_datetime - current_time

    # Extract only hours and minutes from the time delta
    hours, remainder = divmod(time_until_departure.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{hours}h {minutes}m"

if __name__ == "__main__":
    get_stationboard_for_beringen_sonne()
