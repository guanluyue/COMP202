#Name: Gwen Guan
#Student ID: 260950108

class Country:
    '''
    represents a country
    
    Instance Attributes: iso_code (str), name (str), continents (list),
                         co2_emissions (dict), population (dict)
    Class Attributes: min_year_recorded (int), max_year_recorded (int)
    '''
    
    #define the class attributes
    min_year_recorded = 9999
    max_year_recorded = 0
    
    def __init__(self, iso_code, country, conts, year, co2, pop):
        
        '''
        (Country, str, str, list, int, float, int) -> Country
        
        initialize a Country object
        
        >>> Country('RUS', 'Russia', ['ASIA', 'EUROPE'], 1979, 13.395, 3958000)
        >>> Country.name
        'RUS'
        >>> Country('RUS', 'Russia', ['ASIA', 'EUROPE'], 1979, -1, 3958000)
        >>> Country.co2_emission
        {}
        >>> Country('RUSS', 'Russia', ['ASIA', 'EUROPE'], 1979, 13.395, 3958000)
        Traceback (most recent call last):
        AssertionError
        '''
        
        if len(iso_code) >3 and iso_code != 'OWID_KOS':
            raise AssertionError
        
        
        self.iso_code = iso_code
        self.name = country
        self.continents = conts[:]
        self.co2_emissions = {}
        self.population = {}
        self.year = year
        
        #if the input co2 and population is not -1, update their dictionary respectively
        if co2 != -1 :
            self.co2_emissions[year] = co2
        if pop != -1 :
            self.population[year] = pop
        #update the two class attributes when initializing a Country object
        if year < Country.min_year_recorded:
            Country.min_year_recorded = year
        elif year > Country.max_year_recorded:
            Country.max_year_recorded = year
        
    def __str__(self):
        
        '''
        Country -> str
        
        >>> r = Country('RUS', 'Russia', ['ASIA', 'EUROPE'], 1979, 13.395, 3958000)
        >>> str(r)
        'Russia\\t[ASIA,EUROPE]\\t{1979: 13.395}\\t{1979: 395800}'
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> str(c)
        'China\\t[ASIA]\\t{1969: 1.25}\\t{1979: 4848000}'
        
        >>> a = Country('AFG', 'Afghnistan', ['ASIA'], 1949, 0.015, 766783)
        >>> str(a)
        'Afghnistan\\t[ASIA]\\t{1949: 0.015}\\t{1949: 766783}'
        '''
        
        name = self.name
        #join the list of continents as one string
        conts = ','.join(self.continents)
        co2 = str(self.co2_emissions)
        pop = str(self.population)
        return '\t'.join([name, conts, co2, pop])
    
    def add_yearly_data(self, year_co2_pop):
        
        '''
        Country, str -> Country
        
        updates the population and co2 emission of the country
        
        >>> r = Country('RUS', 'Russia', ['ASIA', 'EUROPE'], 1979, 13.395, 3958000)
        >>> r.add_yearly_data('2018\\t3.231\\t28958000')
        >>> r.co2_emissions
        {1979: 13.395, 2018: 3.231}
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> c.add_yearly_data('2018\\t245.251\\t1349288000')
        >>> c.population
        {1969: 4848000, 2018: 1349288000}
        
        >>> a = Country('AFG', 'Afghnistan', ['ASIA'], 1949, 0.015, 766783)
        >>> a.add_yearly_data('2018\\t\\t1349288000')
        {1949: 0.015}
        >>> Country.max_year_recorded
        2018
        '''
        
        #first split the data by columns
        data = year_co2_pop.split('\t')
        year = int(data[0])
        #if the data is not an empty string, update the corresponding dictionary
        if data[1] != '':
            co2 = float(data[1])
            self.co2_emissions[year] = co2
        if data[2] != '':
            pop = int(data[2])
            self.population[year] = pop
            
        #the class attributes are also updated accordingly
        if year < Country.min_year_recorded:
            Country.min_year_recorded = year
        elif year > Country.max_year_recorded:
            Country.max_year_recorded = year

    
    def get_co2_emissions_by_year(self, year):
        
        '''
        Country, int -> int
        
        returns the co2 emission of the country in the specified year if available
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> c.add_yearly_data('2018\\t245.251\\t1349288000')
        >>> c.get_co2_emissions_by_year(1969)
        1.25
        
        >>> c.get_co2_emissions_by_year(2018)
        245.251
        
        >>> c.get_co2_emissions_by_year(2000)
        0.0
        '''
        
        #try getting the value for the input year
        try:
            co2 = self.co2_emissions[year]
        #if the input year is not recorded in the dictionary, return 0.0
        except KeyError:
            return 0.0
        return co2
    
    def get_co2_per_capita_by_year(self, year):
        
        '''
        Country, int -> float
        
        returns the co2 emission per capita in tonnes
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> c.add_yearly_data('2018\\t245.251\\t1349288000')
        >>> round(c.get_co2_per_capita_by_year(1969),2)
        0.26
        
        >>> round(c.get_co2_per_capita_by_year(2018),2)
        1.82
        
        >>> round(c.get_co2_per_capita_by_year(2000),2)
        None
        '''
        
        try:
            #calculate the total co2 emissions in tonnes
            co2_in_tons = self.co2_emissions[year] * (10 ** 6)
            #calculate co2 per capita by dividing total co2 by the population
            co2_per_capita = co2_in_tons / self.population[year]
        except KeyError:
            #if the input year is not in the dictionary, return None
            return None
        return co2_per_capita

    def get_historical_co2(self, year):
        
        '''
        Country, int -> float
        
        returns the historical co2 emission for all years up to the input year
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> c.add_yearly_data('2018\\t245.251\\t1349288000')
        >>> c.get_historical_co2(1969)
        1.25
        
        >>> c.get_historical_co2(2018)
        246.501
        
        >>> c.get_historical_co2(1900)
        0.0
        '''
        
        co2 = 0
        #for each year ranging from the minimum year recorded to the input year
        #calculate the co2 emissions
        for i in range(Country.min_year_recorded, year + 1):
            co2 += self.get_co2_emissions_by_year(i)
        return co2
    
    @classmethod
    def get_country_from_data(cls, data):
        
        '''
        (type, str) -> Country
        
        returns a new Country object created from the data in the input string
        
        >>> r = Country.get_country_from_data('RUS\\tRussia\\t[ASIA,EUROPE]\\t1979\\t13.395\\t395800')
        >>> r.name
        'Russia'
        
        >>> c = Country.get_country_from_data('CHN\\tChina\\t[ASIA]\\t{1969\\t1.25\\t4848000')
        >>> str(c)
        'China\\t[ASIA]\\t{1969: 1.25}\\t{1979: 4848000}'
        
        >>> r = Country.get_country_from_data('RUS\\tRussia\\t[ASIA,EUROPE]\\t1979\\t\\t95800')
        >>> r.co2_emissions
        {}
        '''
        
        column = data.split('\t')
        #assign each column of data to the instance attributes
        iso_code = column[0]
        name = column[1]
        continents = column[2].split(',')
        year = int(column[3])
        #icheck f the input co2 or population is an empty column
        try:
            co2_emissions = float(column[4])
        except ValueError:
            co2_emissions = -1
        try:
            population = int(column[5].strip())
        except ValueError:
            population = -1
        #return a class object from the data
        return cls(iso_code, name, continents, year, co2_emissions, population)
    
    @staticmethod
    def get_countries_by_continent(countries):
        
        '''
        list -> dict
        
        returns a dictionary mapping a string representing a continent to a
        list of objects of type Country which belong to the continent
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> d = Country.get_countries_by_continent([c])
        >>> len(d['AFRICA'])
        0
        
        >>> c = Country('CHN', 'China', ['ASIA'], 1969, 1.25, 4848000)
        >>> r = Country('RUS', 'Russia', ['ASIA', 'EUROPE'], 1979, 13.395, 3958000)
        >>> d = Country.get_countries_by_continent([c,r])
        >>> len(d['EUROPE'])
        1
        >>> len(d['ASIA']
        2
        '''
        
        #create a dictionary with the continents in alphabetical order
        d = {'AFRICA':[], 'ASIA':[], 'EUROPE':[], 'NORTH AMERICA':[],
             'OCEANIA':[], 'SOUTH AMERICA':[]}
        #iterate through each country in the list
        for country in countries:
            #for yearly_country in country:
            for continent in country.continents:
                #for each continent that the country belongs to
                #add the country object to its coresponding continent
                d[continent].append(country)
        return d
    
    @staticmethod
    def get_total_historical_co2_emissions(countries, year):
        
        '''
        (list, int) -> float
        
        returns the total co2 emissions produced by all countries in the list
        for all years up to and including the input year
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data('2018\\t3.231\\t28958000')
        >>> Country.get_historical_co2_emissions([a, b], 2007)
        3.939
        >>> Country.get_historical_co2_emissions([a, b], 2018)
        13.378
        >>> Country.get_historical_co2_emissions([a, b, c], 1851)
        0.0
        '''
        
        co2 = 0
        #use the instance method on each country to calculate the co2
        #add the data of each country to the total
        for country in countries:
            co2 += country.get_historical_co2(year)
        return co2
    
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(countries, year):
        
        '''
        (list, int) -> float
        
        returns the co2 emissions per capita in tonnes prodyced by the countries
        in the list in the specified year
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data('2018\\t3.231\\t28958000')
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([a, b, r], 2007), 1)
        92.99
        >>> Country.get_total_co2_emissions_per_capita_by_year([a, b, r], 2000)
        0.0
        >>> round(Country.get_total_co2_emissions_per_capita_by_year([a, b, r], 1949), 4)
        0.0019
        '''
        co2 = 0
        population = 0
        #iterate through each country and add to the total co2 and total population
        for country in countries:
            co2 += country.get_co2_emissions_by_year(year) * (10 ** 6)
            #check if the country has data for the input year
            try:
                population += country.population[year]
            #if not, skip this country
            except KeyError:
                continue
        #if none of the countries has data for the input year, a ZeroDivisionError will be raised
        try:
            co2_per_capita = co2 / population
        #then return 0.0 in this case
        except ZeroDivisionError:
            return 0.0
        return co2_per_capita
    
    @staticmethod
    def get_co2_emissions_per_capita_by_year(countries, year):
        
        '''
        (list, int) -> dict
        
        returns a dictionary mapping objects of type Country to floats representing
        co2 emissions per capita in tonnes
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data('2018\\t3.231\\t28958000')
        >>> d = Country.get_co2_emissions_per_capita_by_year([a, b, r], 2007)
        >>> d[b]
        3.924
        >>> d = Country.get_co2_emissions_per_capita_by_year([a, b, r], 2000)
        >>> d[a]
        None
        >>> d = Country.get_co2_emissions_per_capita_by_year([a, b, r], 1949)
        >>> d[a]
        0.015
        '''
        
        d = {}
        #create a pair of key and value in the dictionary for every country
        for country in countries:
            #if the country has no data for the input year, the value will be None
            d[country] = country.get_co2_per_capita_by_year(year)
        return d
    
    @staticmethod
    def get_historical_co2_emissions(countries, year):
        
        '''

        (list, int) -> dict
        returns a dictionary mapping objects of type Country to floats representing
        the total co2 emission for all years up to the input year
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data('2018\\t3.231\\t28958000')
        >>> d = Country.get_historical_co2_emissions([a, b, r], 2018)
        >>> d[a]
        9.454
        
        >>> d = Country.get_historical_co2_emissions([a, b, r], 2000)
        >>> d[b]
        0.0
        
        >>> d = Country.get_historical_co2_emissions([a, b, r], 1949)
        >>> len(d)
        3
        '''
        
        d ={}
        #create a pair of key and value in the dictionary for every country
        for country in countries:
            d[country] = country.get_historical_co2(year)
        return d
    
    @staticmethod
    def get_top_n(country_num, n):
        
        '''
        (dict, int) -> list
        
        returns a list of tuples containing the iso code of a country and the number
        to which the country is mapped in the input dict
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t[:5]
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        
        >>> d = {a: 5, b: 5, c: 3}
        >>> t = Country.get_top_n(d, 10)
        >>> t
        [('ALB', 5), ('AUT', 5), ('BEL', 3)]
        
        >>> d = {a: 1.25, b: 6.18, c: 15.2, d: 10, e: 51.21}
        >>> t = Country.get_top_n(d, 5)
        >>> t
        [('BRA', 51.21), ('BEL', 15.2), ('BOL', 10), ('AUT', 6.18), ('ALB', 1.25)]
        '''
        
        #a dictionary contains ISO codes as keys
        names_num = {}
        list_countries = []
  
        for k in country_num:
            names_num[k.name] = country_num[k]
            list_countries.append(k)
        names = list(names_num.keys())
        names.sort()
        #a new dictionary mapping iso codes to the number in the alphabetical order
        iso_num = {}
        for name in names:
            for country in list_countries:
                if country.name == name:
    
                    iso_num[country.iso_code] = country_num[country]
        num_iso = {}
        #add to the dictionary a number as a key and names in alphabetical order
        for iso in iso_num:
            num = iso_num[iso]
            if num in num_iso:
                num_iso[num].extend([iso])
                continue
            num_iso[num] = [iso]
        #get a list of all the numbers in the num_iso dictionary for sorting
        numbers = list(num_iso.keys())
        numbers.sort()
        #make a copy of the list with a reversed order from large to small
        reverse_num = numbers[::-1]
        list_iso_num = []
        #append the tuples with acending order of numbers and it's coresponding ISO
        for number in reverse_num:
            for iso in num_iso[number]:
                list_iso_num.append((iso, number))
        try:
            return list_iso_num[:n]
        #if the elements in the list is fewer then input n
        except IndexError:
            return list_iso_num
    
def get_countries_from_file(filename):
    
    '''
    str -> dict
    
    creates and returns a dictionary mapping ISO codes to objects of Country
    
    >>> d = Country.get_countries_from_file("large_co2_data.tsv")
    >>> len(d)
    193
    
    >>> d = Country.get_countries_from_file("test1_countries.tsv")
    >>> d['RUS'].name
    'Russia'
    
    >>> d = Country.get_countries_from_file("test2_countries.tsv")
    >>> len(d)
    50
    '''
    
    d = {}
    #open the input file and create a file object
    fobj = open(filename, 'r', encoding = 'utf-8')
    #iterate through each line of the file
    for line in fobj:
        data = line.split('\t')
        if data[0] in d: #if the iso code already exists in the dictionary
            #then we just need to update the data using the add_yearly_data function
            add_data = '\t'.join([data[3],data[4],data[5].strip()])
            d[data[0]].add_yearly_data(add_data)
        else: #if the iso code has not been added yet
            #then create a country object and add it to the dictionary
            country = Country.get_country_from_data(line)
            d[country.iso_code] = country
    fobj.close()
    return d