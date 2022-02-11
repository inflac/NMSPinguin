import requests

#Age guesser
def get_age(name):
    url = f'https://api.agify.io/?name=' 
    data = requests.get(url +name).json()
    return str(data['age'])

#Math Facts
def get_new_mathfact():
    url = f'http://numbersapi.com/random/math'
    data = requests.get(url).text
    return data

#Chuch Norris Facts
def get_new_chuckfact():
    url = f'https://api.chucknorris.io/jokes/random'
    data = requests.get(url).json()
    return data['value']

#Cat Facts
def get_new_catfact():
    url = f'https://catfact.ninja/fact'
    data = requests.get(url).json()
    return data['fact']

#Cat Pics
def get_new_catpic():
    url = f'https://cataas.com/cat?json=true'
    data = requests.get(url).json()
    return "https://cataas.com" + data['url'] 

#Dog Pics
def get_new_dogpic():
    url = f'https://dog.ceo/api/breeds/image/random'
    data = requests.get(url).json()
    return data['message']

#Nasa Pics
def get_new_nasapic():
    url = f'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    data = requests.get(url).json()
    return data['url']

#Corona Inzidenz
def corona_updater():
    url = f'https://api.corona-zahlen.org/districts/05911'
    data = requests.get(url).json()
    return data

class corona_update:
    def __init__(self, data):
        self.cases = data['data']['05911']['cases']
        self.deaths = data['data']['05911']['deaths']
        self.casesperweek = data['data']['05911']['casesPerWeek']
        self.deathsperweek = data['data']['05911']['deathsPerWeek']
        self.recovered = data['data']['05911']['recovered']
        self.weekincidence = data['data']['05911']['weekIncidence']
        self.source = data['meta']['source']

    def get_cases(self):
        return self.cases
    def get_deaths(self):
        return self.deaths
    def get_casesperweek(self):
        return self.casesperweek
    def get_deathsperweek(self):
        return self.deathsperweek
    def get_recovered(self):
        return self.recovered
    def get_weekincidence(self):
        return self.weekincidence
    def get_source(self):
        return self.source
    def get_corona_update(self):
        return  "# Bislang erkrankter Personen: " + str(self.cases) + \
                "\n# Bislang verstorbener Personen: " + str(self.deaths) + \
                "\n# Erkrankter in dieser Woche: " + str(self.casesperweek) + \
                "\n# Verstorbener in dieser Woche: " + str(self.deathsperweek) + \
                "\n# Genesener Personen: " + str(self.recovered) + \
                "\nWöchentliche Inzidenz: " + str(self.weekincidence) + \
                "\nDieser Bot nutzt die API von: " + str(self.source)

#Jokes
def get_new_joke():
    url = f'https://v2.jokeapi.dev/joke/Programming?lang=de&blacklistFlags=nsfw,racist,sexist,explicit'
    data = requests.get(url).json()
    return data

class joker:
    def __init__(self, data):
        self.type = data['type']
        if self.type == "single":
            self.joke = data['joke']
            self.setup = False
            self.delivery = False
        else:
            self.joke = False
            self.setup = data['setup'] 
            self.delivery = data['delivery']

    def get_joke_type(self):
        return self.type
    def get_single(self):
        return self.joke
    def get_setup(self):
        return self.setup
    def get_delivery(self):
        return self.delivery
