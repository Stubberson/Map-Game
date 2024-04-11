class Country:
    def __init__(self, country):
        CAPITALS = {"finland": "Helsinki", "sweden": "Stockholm", "norway": "Oslo", "russia": "Moscow",
                    "denmark": "Copenhagen", "estonia": "Tallinn", "latvia": "Riga", "lithuania": "Vilnius",
                    "belarus": "Minsk", "poland": "Warsaw", "ukraine": "Kyiv", "moldova": "Chisinau",
                    "romania": "Bucharest", "serbia": "Belgrade", "bulgaria": "Sofia", "north macedonia": "Skopje",
                    "kosovo": "Pristina", "greece": "Athens", "turkey": "Ankara", "albania": "Tirana",
                    "montenegro": "Podgorica", "bosnia and herzegovina": "Sarajevo", "croatia": "Zagreb",
                    "slovenia": "Ljublana", "hungary": "Budapest", "czechia": "Prague", "slovakia": "Bratislava",
                    "germany": "Berlin", "austria": "Vienna", "switzerland": "Bern", "netherlands": "Amsterdam",
                    "italy": "Rome", "belgium": "Brussels", "france": "Paris", "spain": "Madrid", "portugal": "Lisbon",
                    "united kingdom": "London", "ireland": "Dublin", "iceland": "Reykjavik"}
        POPULATION = {"finland": "5.5", "sweden": "10.4", "norway": "5.4", "russia": "144.2", "denmark": "5.9",
                      "estonia": "1.4", "latvia": "1.9", "lithuania": "2.8", "belarus": "9.2", "poland": "36.8",
                      "ukraine": "33.2", "moldova": "2.5", "romania": "19.1", "serbia": "6.6", "bulgaria": "6.5",
                      "north macedonia": "2.1", "kosovo": "1.9", "greece": "10.4", "turkey": "85.0", "albania": "2.8",
                      "montenegro": "0.6", "bosnia and herzegovina": "3.4", "croatia": "3.9", "slovenia": "2.1",
                      "hungary": "9.6", "czechia": "10.9", "slovakia": "5.5", "germany": "84.6", "austria": "9.0",
                      "switzerland": "8.9", "netherlands": "18.1", "italy": "58.9", "belgium": "11.7", "france": "68.3",
                      "spain": "48.6", "portugal": "10.5", "united kingdom": "67.6", "ireland": "5.3", "iceland": "0.4",
                      }
        NEIGHBORS = {"finland": "Norway, Russia, Sweden",
                     "sweden": "Denmark, Norway, Finland",
                     "norway": "Finland, Russia, Sweden",
                     "russia": "Azerbaijan, Belarus, China, Estonia, Finland, Georgia, Kazakhstan, North Korea, Latvia, Lithuania, Mongolia, Norway, Poland, and Ukraine",
                     "denmark": "Germany",
                     "estonia": "Latvia, Russia",
                     "latvia": "Estonia, Lithuania, Russia, Belarus",
                     "lithuania": "Latvia, Russia, Belarus, Poland",
                     "belarus": "Lithuania, Latvia, Russia, Poland, Ukraine",
                     "poland": "Germany, Belarus, Ukraine, Lithuania, Russia, Czechia, Slovakia",
                     "ukraine": "Moldova, Belarus, Poland, Russia, Romania, Slovakia, Hungary",
                     "moldova": "Romania, Ukraine",
                     "romania": "Moldova, Ukraine, Bulgaria, Serbia, Hungary",
                     "serbia": "Kosovo, Romania, Hungary, Croatia, Bosnia and Herzegovina, Montenegro, North Macedonia, Bulgaria",
                     "bulgaria": "Türkiye, Greece, North Macedonia, Serbia, Romania",
                     "north macedonia": "Kosovo, Serbia, Bulgaria, Albania, Montenegro",
                     "kosovo": "Serbia, North Macedonia, Albania, Montenegro",
                     "greece": "North Macedonia, Bulgaria, Türkiye, Albania",
                     "turkey": "Bulgaria, Greece, Syria, Armenia, Georgia, Iraq, Iran",
                     "albania": "Greece, North Macedonia, Kosovo, Montenegro",
                     "montenegro": "Albania, Kosovo, Serbia, Bosnia and Herzegovina, Croatia",
                     "bosnia and herzegovina": "Croatia, Montenegro, Serbia",
                     "croatia": "Bosnia and Herzegovina, Montenegro, Hungary, Slovenia",
                     "slovenia": "Hungary, Croatia, Italy, Austria",
                     "hungary": "Croatia, Slovenia, Austria, Slovakia, Romania, Ukraine, Serbia",
                     "czechia": "Poland, Germany, Austria, Slovakia",
                     "slovakia": "Poland, Hungary, Austria, Czechia, Ukraine",
                     "germany": "Austria, Czechia, Switzerland, The Netherlands, Belgium, Poland, Denmark, France, Luxembourg",
                     "austria": "Germany, Switzerland, Italy, Slovenia, Slovakia, Hungary",
                     "switzerland": "Germany, Austria, Italy, France",
                     "netherlands": "Germany, Belgium",
                     "italy": "France, Switzerland, Austria, Slovenia, Monaco",
                     "belgium": "France, Netherlands, Germany, Luxembourg",
                     "france": "Spain, Belgium, Luxembourg, Switzerland, Italy, Germany",
                     "spain": "Portugal, France",
                     "portugal": "Spain",
                     "united kingdom": "Ireland",
                     "ireland": "United Kingdom",
                     "iceland": "–"}

        self.name = country
        self.capital = CAPITALS[country]
        self.population = POPULATION[country]
        self.neighboring_countries = NEIGHBORS[country]

    def get_capital(self):
        return self.capital

    def get_population(self):
        return self.population

    def get_neighbors(self):
        return self.neighboring_countries

    def __str__(self):
        string = f"\nCountry: {self.name.capitalize()}\n"  # Name is given in lowercase, capitalize.
        string += f"Capital: {self.capital}\n"
        string += f"Population: {self.population} million\n"
        string += f"Neighboring countries: {self.neighboring_countries}"

        return string
