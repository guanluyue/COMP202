words = line.split()
        if most_sim_word(words[0], words[2:len(words)], semantic_descriptors, similarity_fn) == words[1]:
            num_correct += 1
            total_num += 1
            continue
        
        else:
            total_num += 1
            
            if '--' in sentence:
            new_sentence = sentence.replace('--',' ')
            list_words = new_sentence.split()
        elif '-' in sentence:
            new_sentence = sentence.replace('-', ' ')
            list_words = new_sentence.split()
        elif '’' in sentence:
            new_sentence = sentence.replace('’', ' ')
            list_words = new_sentence.split()
        elif '“' in sentence:
            new_sentence = sentence.replace('“', ' ')
            list_words = new_sentence.split()
        elif '”' in sentence:
            new_sentence = sentence.replace('”', ' ')
            list_words = new_sentence.split()
            
            for char in sentence:
            new_sentence = sentence
            if char in ['-', '’', '“', '”', ',', ':', ';', '\'']:
                new_sentence = new_sentence.replace(char, ' ')
            #create a list with words that might have some other punctuations attached to it
            else:
                continue