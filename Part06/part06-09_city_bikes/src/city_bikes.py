# Write your solution here

def get_station_data(filename: str):
    stations = {}

    with open(filename) as file:
        for line in file:
            line = line.split(";")
            if line[0] not in "Longitude":
                line[0] = float(line[0])
                line[1] = float(line[1])
                stations[line[3]] = (line[0], line[1])
    
    return stations


def distance(stations: dict, station1: str, station2: str):
    import math

    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict):
    greatest_d = 0

    for i in stations.keys():
        for j in stations.keys():
            d = distance(stations, i, j)
            if d > greatest_d:
                greatest_d = d
                greatest = (i, j, greatest_d)
    
    return greatest

if __name__ == "__main__":
    stations_data = get_station_data("src/stations1.csv")
    for i, j in stations_data.items():
        print(f"{i}: {j}")

    d = distance(stations_data, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations_data, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations_data)
    print(station1, station2, greatest)
