#Name: Gwen Guan
#Student ID: 260950108
from file_processing import *
import matplotlib.pyplot as plt
def most_sim_word(word, choices, semantic_descriptors, similarity_fn):
    
    '''
    (str, 
    returns the element of choices which has the largest similarity function
    
    '''
    
    similarity = similarity_fn(semantic_descriptors[choices[0]],semantic_descriptors[word])
    choice = choices[0]
    #get the similarity of the word and each of the choices
    for c in choices:
        updated_similarity = similarity_fn(semantic_descriptors[c], semantic_descriptors[word])
        if updated_similarity > similarity:
            choice = c
    
    return choice

#choices = ['dog', 'cat', 'horse']
#c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
#f = {'furry' : 2, 'nimble' : 5}
#d = {'furry' :  3, 'bark' : 5, 'loyal' : 8}
#h = {'race' : 4, 'queen' : 2}
#sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
#print(most_sim_word('feline', choices, sem_descs, get_cos_sim))

def run_sim_test(filename, semantic_descriptors, similarity_fn):
    
    '''
    returns the percentage of questions on which most_sim_word guesses the answer correctly
    
    '''
    
    fobj = open(filename, 'r')
    content = fobj.readlines()
    fobj.close()
    num_correct = 0
    total_num = 0
    for line in content:
        words = line.split()
        if most_sim_word(words[0], words[2:len(words)], semantic_descriptors, similarity_fn) == words[1]:
            num_correct += 1
            total_num += 1
        else:
            total_num += 1
    
    return round(num_correct / total_num * 100, 1)
#print(run_sim_test('test.txt', build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt']), get_cos_sim))
def generate_bar_graph(similarity_fns, filename):
    '''
    list ->
    generates a bar graph of the performace of each funtion on the given file test
    '''
    desc = build_semantic_descriptors_from_files(filename)
    scores = []
    fns = []
    for func in similarity_fns:
        scores.append(run_sim_test('test.txt', desc, func))
        fns.append(func.__name__)
    plt.bar(fns, scores)
    plt.show()
    
#desc = build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt'])

#generate_bar_graph([get_cos_sim, get_euc_sim, get_norm_euc_sim], ['swanns_way.txt', 'war_and_peace.txt'])
#print(run_sim_test('test.txt', build_semantic_descriptors_from_files(['test.txt']), get_cos_sim))