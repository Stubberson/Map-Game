class Country:
    def __init__(self, country):
        CAPITALS = {"finland": "Helsinki", "sweden": "Stockholm", "norway": "Oslo", "russia": "Moscow",
                    "denmark": "Copenhagen", "estonia": "Tallinn", "latvia": "Riga", "lithuania": "Vilnius",
                    "belarus": "Minsk", "poland": "Warsaw", "ukraine": "Kyiv", "moldova": "Chisinau",
                    "romania": "Bucharest", "serbia": "Belgrade", "bulgaria": "Sofia", "north macedonia": "Skopje",
                    "kosovo": "Pristina", "greece": "Athens", "turkey": "Ankara", "albania": "Tirana",
                    "montenegro": "Podgorica", "bosnia and herzegovina": "Sarajevo", "croatia": "Zagreb",
                    "slovenia": "Ljubljana", "hungary": "Budapest", "czechia": "Prague", "slovakia": "Bratislava",
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
                     "russia": "Azerbaijan, Belarus, China, Estonia, Finland, Georgia, \nKazakhstan, North Korea, Latvia, Lithuania, Mongolia, Norway, Poland, and Ukraine",
                     "denmark": "Germany",
                     "estonia": "Latvia, Russia",
                     "latvia": "Estonia, Lithuania, Russia, Belarus",
                     "lithuania": "Latvia, Russia, Belarus, Poland",
                     "belarus": "Lithuania, Latvia, Russia, Poland, Ukraine",
                     "poland": "Germany, Belarus, Ukraine, Lithuania, Russia, Czechia, Slovakia",
                     "ukraine": "Moldova, Belarus, Poland, Russia, Romania, Slovakia, Hungary",
                     "moldova": "Romania, Ukraine",
                     "romania": "Moldova, Ukraine, Bulgaria, Serbia, Hungary",
                     "serbia": "Kosovo, Romania, Hungary, Croatia, Bosnia and Herzegovina, \nMontenegro, North Macedonia, Bulgaria",
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
                     "germany": "Austria, Czechia, Switzerland, The Netherlands, Belgium, \nPoland, Denmark, France, Luxembourg",
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

        EXTRA = {"finland": "Finland has the most lakes in Europe, with approximately 188,000 lakes.",
                 "sweden": "In the capital of Sweden, Stockholm, the metro system also doubles as an art gallery, with 90% of metro stations decorated.",
                 "norway": "Norway is home to the longest road tunnel in the world, the Lærdal Tunnel (24.5 km).",
                 "russia": "Russia‘s Lake Baikal is the world’s deepest and oldest freshwater lake.",
                 "denmark": "Denmark is frequently ranked as one of the world’s happiest countries.",
                 "estonia": "Estonia has the highest number of meteorite craters per land area in the world.",
                 "latvia": "Latvia has one of the world’s highest rates of forest coverage.",
                 "lithuania": "Lithuania was the last European country to convert to Christianity, in the late 14th century.",
                 "belarus": "Belarus has the world’s largest population of European bison, also known as wisent.",
                 "poland": "Poland has the world’s largest castle by land area, it is known as the Castle of the Teutonic Order in Malbork.",
                 "ukraine": "Slava Ukraini!",
                 "moldova": "Moldova is home to the largest wine cellar in the world, Milestii Mici, which spans over 200 kilometres.",
                 "romania": "Romania is home to Europe’s largest virgin forests.",
                 "serbia": "Serbia‘s capital, Belgrade, has been fought over in 115 wars and razed to the ground 44 times throughout history.",
                 "bulgaria": "The Cyrillic alphabet, used by many Eastern European countries,\nwas created in Bulgaria during the 9th century.",
                 "north macedonia": "North Macedonia is the only country to gain independence from Yugoslavia without any bloodshed.",
                 "kosovo": "Kosovo is the youngest country in Europe, declaring independence from Serbia in 2008.",
                 "greece": "The Olympic Games originated in ancient Greece in 776 BC.",
                 "turkey": "Istanbul, Turkey, is the only city in the world that straddles two continents, Europe and Asia.",
                 "albania": "In some areas on the country,\nAlbanians nod their heads to indicate “no” and shake their heads for “yes.”",
                 "montenegro": "The Bay of Kotor in Montenegro is one of the world’s deepest and longest fjord-like bays.",
                 "bosnia and herzegovina": "The Stari Most (Old Bridge) in Mostar is a UNESCO World Heritage Site",
                 "croatia": "Croatia has the world’s smallest town, Hum, with a population of around 30 people.",
                 "slovenia": "Slovenia is home to the Postojna Cave, the largest show cave in Europe, which has a unique train ride for visitors.",
                 "hungary": "Hungary is home to the world’s largest thermal water cave system.",
                 "czechia": "Czechia has the highest beer consumption per capita in the world.",
                 "slovakia": "Slovakia has more than 6,000 caves, including the remarkable ice caves of the Slovak Paradise National Park.",
                 "germany": "There's a German girl that I love. She's caring, beautiful, intelligent; the whole package...",
                 "austria": "In Austria the Alps mountain range covers about 62% of the country.",
                 "switzerland": "Switzerland is famous for its neutrality and has not been involved in any wars since 1815.",
                 "netherlands": "The Netherlands is the world’s biggest flower exporter.",
                 "italy": "Italy has the most UNESCO World Heritage Sites, with over 50 locations.",
                 "belgium": "Brussels, Belgium, is home to the European Union and NATO headquarters.",
                 "france": "The Eiffel Tower in Paris, France was initially meant to be a temporary structure for the 1889 World’s Fair.",
                 "spain": "Spain is home to the world’s oldest restaurant, Sobrino de Botín, established in 1725.",
                 "portugal": "Portugal is one of the world’s top cork producers, responsible for over 50% of global cork production.",
                 "united kingdom": "Windsor Castle in the United Kingdom is the oldest and longest-occupied palace by a monarch in the world.",
                 "ireland": "Halloween’s origins can be traced back to the ancient Celtic festival of Samhain in Ireland.",
                 "iceland": "Iceland is one of the few countries in the world with no mosquitoes."}

        self.name = country
        self.capital = CAPITALS[country]
        self.population = POPULATION[country]
        self.neighboring_countries = NEIGHBORS[country]
        self.extra = EXTRA[country]

    def get_capital(self):
        return self.capital

    def get_population(self):
        return self.population

    def get_neighbors(self):
        return self.neighboring_countries

    def get_extra(self):
        return self.extra

    def __str__(self):
        string = f"\nCountry: {self.name.capitalize()}\n"  # Name is given in lowercase, capitalize.
        string += f"Capital: {self.capital}\n"
        string += f"Population: {self.population} million\n"
        string += f"Neighboring countries: {self.neighboring_countries}"

        return string
