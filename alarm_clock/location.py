inf = open("location.txt", "r")
location = inf.read()
inf.close()

ldict = {
    
    'Newton'        : 'https://www.accuweather.com/en/us/newton/07860/current-weather/334489',
    'Augusta'       : 'https://www.accuweather.com/en/us/augusta/07822/current-weather/2174793',
    'Atlantic City' : 'https://www.accuweather.com/en/us/atlantic-city/08401/current-weather/329552',
    'Hawley'        : 'https://www.accuweather.com/en/us/hawley/18428/current-weather/345448'
    'Newark'        : 'https://www.accuweather.com/en/us/newark/07103/current-weather/349530'
}

st = ldict.get(location)

#print("\n" + st + "\n")

outf = open("source.txt", "w+")
outf.write(str(st))
outf.close()
