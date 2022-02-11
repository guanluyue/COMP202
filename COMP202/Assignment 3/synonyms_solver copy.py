#Name: Gwen Guan
#Student ID: 260950108
from file_processing import *
import matplotlib.pyplot as plt
import math
def most_sim_word(word, choices, semantic_descriptors, similarity_fn):
    
    '''
    (str, list, dict, function) -> str
    
    returns the element of choices which has the largest similarity function
    
    >>> fobj = open('test.txt', 'r', encoding = 'utf-8')
    >>> file_content = fobj.read()
    >>> fobj.close()
    >>> sem_descs = get_all_semantic_descriptors(file_content)
    >>> most_sim_word('draw', ['walk', 'paint'], get_cos_sim)
    'walk'
    >>> most_sim_word('draw', ['walk', 'paint'], sem_descs, get_cos_sim)
    'task'
    >>> most_sim_word('earnest', ['serious', 'amusing'], sem_descs, get_cos_sim)
    'serious'
    >>> most_sim_word('a', ['f', 'g'], {'a': {'b':2, 'g':4}, 'g':{'b': 2}}, get_cos_sim) #where f will raise KeyError
    'g'
    '''
    
    try:
        similarity = similarity_fn(semantic_descriptors[choices[0]],semantic_descriptors[word])
    except KeyError:
        similarity = float('-inf')
    choice = choices[0]
    #get the similarity of the word and each of the choices
    for c in choices:
        try:
            updated_similarity = similarity_fn(semantic_descriptors[c], semantic_descriptors[word])
        except KeyError:
            updated_similarity = float('-inf')
            continue
        if updated_similarity > similarity:
                similarity = updated_similarity
                choice = c
    if similarity == float('-inf'):
        return ''
    return choice

def run_sim_test(filename, semantic_descriptors, similarity_fn):
    
    '''
    (file, dict, function) -> float
    
    returns the percentage of questions on which most_sim_word guesses the answer correctly
    
    >>> round(run_sim_test('test.txt', build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt']),
    get_cos_sim), 1)
    65.0
    >>> round(run_sim_test('test.txt', build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt']),
    get_euc_sim), 1)
    32.5
    >>> round(run_sim_test('test.txt', build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt']),
    get_norm_euc_sim), 1)
    65.0
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

def generate_bar_graph(similarity_fns, filename):
    '''
    (list, str) -> matplotlib
    generates a bar graph of the performace of each funtion on the given files
    
    '''
    desc = build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt'])
    scores = []
    fns = []
    for func in similarity_fns:
        scores.append(run_sim_test(filename, desc, func))
        fns.append(func.__name__)
    plt.title('The performance of each function on the test', fontsize = 10)
    plt.xlabel('Function names', fontsize = 10)
    plt.ylabel('Percentage', fontsize = 10)
    plt.bar(fns, scores)
    plt.savefig('synonyms_test_results.png')
    plt.show()
    
#desc = build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt'])

generate_bar_graph([get_cos_sim, get_euc_sim, get_norm_euc_sim], 'test.txt')
#print(run_sim_test('test.txt', build_semantic_descriptors_from_files(['test.txt']), get_cos_sim))