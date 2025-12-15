#Elvis Nguyen
cities = ["New York", "Boston", "Atlanta", "Dallas"]

outfile = open("cities.txt", "w")

for city in range(len(cities)):
    outfile.write(cities[city] + "\n")

outfile.close()
