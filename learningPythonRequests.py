import requests

links = [
    "https://swapi.co/api/people/1/",
    "https://swapi.co/api/people/2/",
    "https://swapi.co/api/people/3/",
    "https://swapi.co/api/people/4/",
    "https://swapi.co/api/people/5/",
    "https://swapi.co/api/people/6/",
]
for index, link in enumerate(links): 
    test = requests.get(link)
    swfile = open("starwars" + str(index) +".txt", "w")
    test.encoding = 'ISO-8859-1'
    swfile.write(str(test.text))