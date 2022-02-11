#Name: Gwen Guan
#Student ID: 260950108

def get_iso_codes_by_continent(filename):
    
    '''
    str -> dict
    returns a dictionary mapping continents' names to a list of ISO codes
    
    >>> d = get_iso_codes_by_continent('iso_codes_by_continent.tsv')
    >>> d['AFRICA'][0]
    'NGA'
    >>> d1 = get_iso_codes_by_continent('iso_cont_test1.tsv')
    >>> d1['ASIA'][0]
    'CHN'
    >>> d2 = get_iso_codes_by_continent('iso_cont_test2.tsv')
    >>> len(d2)
    3
    '''
    
    #create a dictionary with the name of each continent to start with
    continent_iso = {'AFRICA':[], 'ASIA':[], 'EUROPE':[], 'NORTH AMERICA':[],
                     'OCEANIA':[], 'SOUTH AMERICA':[]}
    fobj = open(filename, 'r', encoding = 'utf-8')
    for line in fobj:
        #first split the data by columns
        iso_cont = line.split('\t')
        upper_continent = iso_cont[1].upper()
        continent = upper_continent.strip()
        #add the ISO code to its corresponding continent
        continent_iso[continent].append(iso_cont[0])
    fobj.close()
    return continent_iso


def add_continents_to_data(input_filename, continents_filename, output_filename):
    '''
    (str, str, str) -> int
    
    make changes to the input file and write the new version to output file
    add a new column containing the continents which the country belongs to
    
    >>> add_continents_to_data('test5.txt', 'iso_cont_test1.tsv', 'test5_continents.txt') 
    3
    >>> add_continents_to_data('test6.txt', 'iso_cont_test2.tsv', 'test6_continents.txt') 
    50
    >>> add_continents_to_data("large_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
"large_co2_data.tsv")
    17452
    '''
    
    input_fobj = open(input_filename, 'r', encoding = 'utf-8')
    #get the dictionary mapping continents to iso codes using the previous function
    cont_iso = get_iso_codes_by_continent(continents_filename)
    output_file = open(output_filename, 'w')
    num_lines = 0
    for line in input_fobj:
        num_conts = 0
        #get a list containing data in each column
        columns = line.split('\t')
        #create a list for the continents which a country belongs to in case there are more than 1 continent
        conts = []
        #iterate through each country
        for key, value in cont_iso.items():
            #chekc if the iso code matches 
            if columns[0] in value:
                #add its corresponding continent into the list
                conts.append(key)
        #insert the new column into the line of data
        columns.insert(2, ','.join(conts))
        #then seperate the colomns by a tab and write the line into the output file
        output_file.write('\t'.join(columns))
        #update the number of lines for each line iterated in the for loop
        num_lines += 1
    input_fobj.close()
    output_file.close()
    return num_lines
