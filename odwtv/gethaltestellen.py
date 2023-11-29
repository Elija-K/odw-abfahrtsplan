import requests

def get_stations_in_beringen():
    api_url = "http://transport.opendata.ch/v1/locations"
    params = {
        "query": "Beringen"
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        stations = data.get("stations", [])

        if stations:
            for station in stations:
                print(f"Station ID: {station['id']}")
                print(f"Station Name: {station['name']}")
                print(f"Coordinates: {station['coordinate']}")
                print("-------------------------")
        else:
            print("No stations found in Beringen.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    get_stations_in_beringen()
