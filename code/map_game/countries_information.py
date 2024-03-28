class Country:
    def __init__(self, country):
        CAPITALS = {"finland": "Helsinki", "sweden": "Stockholm", "norway": "Oslo"}
        POPULATION = {"finland": "5.5", "sweden": "10.4", "norway": "5.4"}
        NEIGHBORS = {"finland": "Norway, Russia, Sweden", "sweden": "Denmark, Norway, Finland", "norway": "Finland, Russia, Sweden"}

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
        string = f"\nThe country in question is {self.name.capitalize()}!\n"  # Name is given in lowercase, capitalize.
        string += f"Its capital is {self.capital} and the population is {self.population} million.\n"
        string += f"The neighboring countries are {self.neighboring_countries}."

        return string
