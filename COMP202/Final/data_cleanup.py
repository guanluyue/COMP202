#Name: Gwen Guan
#Student ID: 260950108

#Ho! Ho! Ho! Happy holidays! XD

def find_delim(line):
    
    '''
    str -> str
    
    returns the most commonly used delimiter in the input
    
    >>> find_delim('h.e,l,l,o')
    ','
    >>> find_delim('h!e!l!l!o')
    Traceback (most recent call last):
    AssertionError: There is no valid delimiter in the string.
    >>> find_delim('okay\\tfine\\tyeah')
    '\\t'
    '''
    
    #a list of elements containing the strings seperated by a space
    splitted_by_space = line.split(' ')
    #count the number of elements in a list
    #then subtract by 1 to get the number of delimiters
    num_init = len(splitted_by_space) - 1
    most_common_dilimiter = ' '
    
    #count the number of each delimiter and compare to the initial value
    for dilimiter in ['\t', ',', '-']:
        splitted_by_dilimiter = line.split(dilimiter)
        num_dilimiter = len(splitted_by_dilimiter) - 1
        if num_dilimiter > num_init:
            num_init = num_dilimiter
            most_common_dilimiter = dilimiter
    #raise an AssertionError if there's no valid delimiter
    if num_init == 0:
        raise AssertionError ('There is no valid delimiter in the string.')
    
    return most_common_dilimiter

def clean_one(input_filename, output_filename):
    
    '''
    (str, str) -> int
    
    reads the input file and make changes to each of the lines and write
    the new version to output file
    then returns the number of lines in the output file
    
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10
    >>> clean_one('test1.txt', 'test1_tab_sep') #this is a test file I created containing 3 lines
    3
    >>> clean_one('test2.txt', 'test2_tab_sep') #this is a test file I created containing 50 lines
    50
    '''
    
    #first open the file 
    fobj = open(input_filename, 'r', encoding = 'utf-8')
    output_file = open(output_filename, 'w')
    lines_in_file = 0
    #iterate through each line of the file, seperate the data by a tab
    #and add 1 to the number of lines in file
    for line in fobj:
        delimiter = find_delim(line)
        output_file.write(line.replace(delimiter, '\t'))
        lines_in_file += 1
    output_file.close()
    fobj.close()
    return lines_in_file

def comma_to_dot(line):
    
    '''
    list -> list
    
    helper function that replaces the comma in the fourth column with dot
    assuming that the input line has exact 5 columns
    
    >>> ['RUS', 'Russia', '1979', '1,209', '23410000']
    ['RUS', 'Russia', '1979', '', '23410000']
    >>> ['RUS', 'Russia', '1979', '', '23410000'] #case where the co2 is an empty column
    ['RUS', 'Russia', '1979', '', '23410000']
    >>> ['RUS', 'Russia', '1979', '0', '23410000'] #case where the co2 is 0
    ['RUS', 'Russia', '1979', '0', '23410000']
    
    '''
    
    new_list = []
    #if the co2 emission has a ',' in it, we replace it with a dot
    if ',' in line[-2]: 
        with_dot = line[-2].replace(',', '.') 
        new_list = []
        #add the rest of the data into the new modified list
        new_list.extend([line[0],line[1],line[2], with_dot, line[4]])
        return new_list
    elif line[-2] == '-1' or line[-2] == '' or line[-2] == '0':
        return line
    else:
        return line
    
def final_clean(input_filename, output_filename):
    '''
    (str, str) -> int
    
    reads the input file and make changes to each of the lines and write
    the new version to output file
    
    >>> final_clean('large_tab_sep_co2_data.tsv', 'large_clean_co2_data.tsv')
    17452
    >>> final_clean('test3.txt', 'test3_tab_sep') #this is a test file I created containing 10 lines
    10
    >>> final_clean('test4.txt', 'test4_tab_sep') #this is a test file I created containing 15 lines
    15
    '''
    
    fobj = open(input_filename, 'r', encoding = 'utf-8')
    output_file = open(output_filename, 'w')
    lines_in_file = 0
    
    for line in fobj:
        #get the list containing all data in coloumns
        list_of_elements = line.split('\t')
        #if the there's no more than 5 columns, then it's normal data
        #we only need to check if the co2 emissions are separated by a comma
        if len(list_of_elements) <= 5:
               modified_list = comma_to_dot(list_of_elements)
               output_file.write('\t'.join(modified_list))
               lines_in_file += 1
               continue
            
        elif len(list_of_elements) > 5:

            #for example, 'SAU   Saudi   Arabia   1950   5,141   3121000'
            #Case when country names are seperated by spaces
            country_name = ''
            #try if the first character of the third column is a number
            #if not, then it belongs to the country name
            try:
                int(list_of_elements[2][0])
            except ValueError:
                #check if the following columns are still part of the name
                modified_line = []
                for i in range(5):
                    #check if the first digit of the column can be converted to integer
                    try:
                        y = int(list_of_elements[2 + i][0])
                    #if not, then it's an alphabet, so it should be added to the country name
                    except ValueError:
                        list_country_name = list_of_elements[1 : 3 + i]
                        country_name = ' '.join(list_country_name)
                        continue
                    #if it is an integer, which means that the country name has been stored in the country_name variable
                    #the list below contains the modified line with the country name in one column
                    modified_line.extend([list_of_elements[0], country_name, list_of_elements[-3],
                                          list_of_elements[-2], list_of_elements[-1]])
                    #and then convert the comma for co2 emission to dot
                    fixed_line = comma_to_dot(modified_line)
                    output_file.write('\t'.join(fixed_line))
                    lines_in_file += 1
                    break
                continue
                
            #Case when the co2 emission column is seperated into 2 due to the comma
            #which means comma is the delimiter, so no country name will be seperated
            #if the co2 emission is seperated, the second and third last column will contain integers without ',' or '.'
            if ',' not in list_of_elements[-2] and '.' not in list_of_elements[-2]:
                if list_of_elements[-2] != '0' and list_of_elements[-2] != '-1' and list_of_elements[-2] != '':
                    co2_emission = '.'.join(list_of_elements[3:5])
                    fixed_line = []
                    fixed_line.extend([list_of_elements[0],list_of_elements[1],list_of_elements[2],
                                       co2_emission, list_of_elements[5]])
                    output_file.write('\t'.join(fixed_line))
                    lines_in_file += 1
                    continue
 
    output_file.close()
    fobj.close()
    return lines_in_file


