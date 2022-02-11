#Name: Gwen Guan
#Student ID: 260950108

import matplotlib.pyplot as plt
from build_countries import *

def get_bar_co2_pc_by_continent(iso_country, year):
    
    '''
    (dict, int) -> list
    
    creates a bar plot representing the co2 emissions per capita
    produced by all the countries in each continent
    
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data1 = get_bar_co2_pc_by_continent(d, 2000)
    >>> len(data1)
    6
    >>> data1[0] # AFRICA
    1.0975340644568221
    >>> data2 = get_bar_co2_pc_by_continent(d, 1930)
    >>> data2[1]
    0.23255543279497998
    >>> get_bar_co2_pc_by_continent(d, 1865)
    [0.0013132802726073724, 1.7371901014320072, 1.5021781847258193, 0.27968311438109317]
    '''
    
    #a list of country objects
    list_countries = []
    #the list containing y values across x axis
    co2_per_cont = []
    conts = []
    for iso in iso_country:
        list_countries.append(iso_country[iso])
    #create a dictionary mapping continents to countries in that continent
    cont_countries = Country.get_countries_by_continent(list_countries)
    #iterate through each country in a continent in the dictionary
    for cont in cont_countries:
        #get the co2 emissions per capita in a continent containing a list of countries
        co2 = Country.get_total_co2_emissions_per_capita_by_year(cont_countries[cont], year)
        #exclude continents with 0 co2 emissions per capita
        if co2 != 0:
            conts.append(cont)
            co2_per_cont.append(co2)
            
    plt.bar(conts, co2_per_cont)
    plt.title('CO2 emissions per capita in ' + str(year) + ' by luyue.guan@mail.mcgill.ca')
    plt.ylabel('co2 (in tonnes)')
    plt.savefig('co2_pc_by_continent_' + str(year) +'.png')
    
    return co2_per_cont

def get_bar_historical_co2_by_continent(iso_country, year):
    
    '''
    (dict, int) -> list
    
    creates a bar plot representing the historical co2 emissions
    return a list containing all data plotted
    
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d, 1990)
    >>> len(data)
    6
    >>> round(data[2],4) # EUROPE
    334210.701
    >>> data2 = get_bar_historical_co2_by_continent(d, 1959)
    >>> round(data2[2],4)
    122883.229
    >>> data3 = get_bar_historical_co2_by_continent(d, 1851)
    >>> len(data3)
    2
    '''
    
    #a list of country objects
    list_countries = []
    #the list containing y values across x axis
    co2_per_cont = []
    conts = []
    for iso in iso_country:
        list_countries.append(iso_country[iso])
    #create a dictionary mapping continents to countries in that continent
    cont_countries = Country.get_countries_by_continent(list_countries)
    for cont in cont_countries:
        co2 = Country.get_total_historical_co2_emissions(cont_countries[cont], year)
        #exclude continents with 0 co2 emissions
        if co2 != 0:  
            co2_per_cont.append(co2)
            conts.append(cont)
    #plot the data (same old same old)
    plt.bar(conts, co2_per_cont)
    plt.title('Historical CO2 emissions up to ' + str(year) + ' by luyue.guan@mail.mcgill.ca')
    plt.ylabel('co2 (in millions of tonnes)')
    plt.savefig('hist_co2_by_continent_' + str(year) +'.png')
    return co2_per_cont

def get_bar_co2_pc_top_ten(iso_country, year):
    '''
    (dict, int) -> list
    
    create a bar plot representing the co2 emissions per capita produced by
    the top 10 countries then return the list of the calues being plotted
    
    >>> d = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d, 2000)
    >>> len(data)
    10
    >>> data[0] # QAT
    58.388513513513516
    >>> data2 = get_bar_co2_pc_top_ten(d, 2018)
    >>> data2[0]
    37.966570812365205
    >>> data3 = get_bar_co2_pc_top_ten(d, 1845)
    >>> data3[0]
    4.61877153897706
    '''
    
    d = {}
    #for each country, calculate its co2 per capita that will be added to the dictionary above
    for iso in iso_country:
        co2 = 0
        try:
            co2 += iso_country[iso].get_co2_per_capita_by_year(year)
            d[iso_country[iso]] = co2
        #since the dictionary contains None, we need to except TypeError
        except TypeError:
            continue
    #create a list for x and y
    list_countries = []
    co2_per_country = []
    #use the static method that returns the top ten countries in a dict
    top_ten = Country.get_top_n(d, 10)
    #add elements to the lists for x and y axis
    for (iso,co2) in top_ten:
        list_countries.append(iso)
        co2_per_country.append(co2)
    plt.bar(list_countries, co2_per_country)
    plt.title('Top 10 countries for CO2 emissions pc in ' + str(year) + ' by luyue.guan@mail.mcgill.ca')
    plt.ylabel('co2 (in tonnes)')
    plt.savefig('top_10_co2_pc' + str(year) +'.png')
    return co2_per_country


def get_bar_top_ten_historical_co2(iso_country, year):
    
    '''

    (dict, int) -> list
    
    creates a bar plot representing the historical co2 emissions produced by the top 10 producing
    countries in the dictionary the nreturn a list with the values being plotted
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 2018)
    >>> len(data)
    10
    >>> data2 = get_bar_top_ten_historical_co2(d2, 1930)
    >>> data2[0]
    52939.619
    >>> data3 = get_bar_top_ten_historical_co2(d2, 1860)
    >>> data3[0]
    5043.524
    '''
    
    d = {}
    #iterate through each country in the dict
    for iso in iso_country:
        country = iso_country[iso]
        #get the historical co2 emissions for each year
        co2 = country.get_historical_co2(year)
        #the dictionary maps a country object to its historical co2
        d[country] = co2
    #create lists for x and y axis
    list_countries = []
    co2_per_country = []
    #get the top ten countries
    top_ten = Country.get_top_n(d, 10)
    #add iso codes and its corresponding historical co2 emission to the x and y values
    for (iso,co2) in top_ten:
        list_countries.append(iso)
        co2_per_country.append(co2)
    plt.bar(list_countries, co2_per_country)
    plt.title('Top 10 countries for historical CO2 up to ' + str(year) + ' by luyue.guan@mail.mcgill.ca')
    plt.ylabel('co2 (in millions of tonnes)')
    plt.savefig('top_10_hist_co2' + str(year) +'.png')
    return co2_per_country

def get_plot_co2_emissions(iso_country, iso_codes, min_year, max_year):
    '''

    (dict, list, int, int) -> list
    
    plot and save the co2 emissions of the list of countries
    return a nested list containing all co2 emissions of each country from min year to max year
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> len(data[0])
    201
    >>> data2 = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 2000, 2018)
    >>> data2[0][0]
    5997.299
    >>> data3 = get_plot_co2_emissions(d2, ["RUS", "ALB", "AFG"], 2000, 2018)
    >>> len(data3[0])
    19
    '''
    
    styles = ['o-b','^--g','s-.r','d:k','h--y']
    data = []
    #iterate through each country in the dict
    for i in range(len(iso_codes)):
        x = []
        y = []
        step = (max_year-min_year) // 10
        #for each year in between the min and max with a step calculated above 
        for year in range(min_year, max_year + step, step):
            #get the co2 emissions of that year
            co2 = iso_country[iso_codes[i]].get_co2_emissions_by_year(year)
            #add values to x and y axis
            x.append(year)
            y.append(co2)
        #plot the data of each country with different styles
        plt.plot(x, y, styles[i])
    plt.legend(iso_codes)
    plt.ylabel('co2 (in millions of tonnes)')
    plt.title('CO2 emissions between ' + str(min_year) + ' and ' + str(max_year) +
              ' by luyue.guan@mail.mcgill.ca')
    plt.savefig('co2_emissions_' + str(min_year) + '_' + str(max_year) +'.png')
    #add the data of each country to the list seoarately
    for iso in iso_codes:
        country_data = []
        #get the co2 emissions data for each country
        for year in range(min_year, max_year + 1):
            country_data.append(iso_country[iso].get_co2_emissions_by_year(year))
        data.append(country_data)
    return data
