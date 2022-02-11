def a(line):   

    list_of_elements = line.split('\t')


    if find_delim(line) != ',':
        #'BFA \t Burkina \t Faso \t 000 \t 1,031 \t 11608000'
        if ',' in list_of_elements[-2]: #1.031
            with_dot = list_of_elements[-2].replace(',', '.') #change to 1.031
            new_list = []
            new_list.extend(list_of_elements[0:3])
            new_list.append(with_dot)
            new_list.append(list_of_elements[4])
            output_line='\t'.join(new_list) #!!!!
        
        if len(list_of_elements) > 5:
            #'SAU Saudi Arabia 1950 5,141 3121000'
            #cases when country names are seperated by spaces
            country_name = ''
            
            #try if the first character of the third column is a number
            #if not, then it belongs to the country name
            try:
                int(list_of_elements[2][0])
            except ValueError:
                #check if the following columns are still part of the name
                for i in range(5):
                    try:
                        y = int(list_of_elements[2 + i][0])
                    except ValueError:
                        list_country_name = list_of_elements[1 : 3 + i]
                        country_name = ' '.join(list_country_name)
                        continue
                    modified_line = '\t'.join([list_of_elements[0], country_name,
                                               list_of_elements[-2], list_of_elements[-1]])
                    output_line=modified_line
                    break
    else: #if the data IS seperated by ','
    #For example: 'HND,Honduras,1970,1,388,2717000'
    #the number 1,388 will be seperated to two columns
        if len(list_of_elements) > 5:
            co2_emission = '.'.join(list_of_elements[3:5])
            output_line=(list_of_elements[0] + list_of_elements[1] + list_of_elements[2] +
                              co2_emission + list_of_elements[5])

    return  output_line
\
  
added_iso = continent_iso.get(continent)
        added_iso.append(iso_cont[0])