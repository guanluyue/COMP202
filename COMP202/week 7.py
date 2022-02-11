def g(words, prefix):
    wanted_words = []
    for w in words:
        if w[0:len(prefix)] == prefix:
            wanted_words.append(w)
    return wanted_words

def f(a, b):
    dups = [] #G1
    for x1 in a: #B1
        c = 0
        for x in a: #F2
            if x == x1:
                c += 1 #A4
        for x in b: #D2
            if x == x1:
                c += 1 #A4
        if c == 3: #E2
            if x1 not in dups:
                dups.append(x1)
    return dups#C1

ALPHABET = 'qwertyuiopasdfghklzxcvbnm'
def b(valid_password):
    password = [0] * 4
    for letter in ALPHABET:
        password[0] = letter
        for letter in ALPHABET:
            password[1] = letter
            for letter in ALPHABET:
                password[2] = letter
                for letter in ALPHABET:
                    password[3] = letter
                    if password == valid_password:
                        return True
    return False
#create a new list containing the ranks of the card
    ranks = []
    for c in cards:
        #add the rank of each card to the list
        ranks.append(str(get_rank(c)))
        #e.p. ranks = ['2', '7', '1', '2']
    number_each_rank = []
    #generates a list containing how many times each rank appears in cards
    for r in ranks:
        number_each_rank.append(ranks.count(r))
        #e.p. number_each_rank = [2, 1, 1, 2]
    for r in number_each_rank:
        if r >=3 and r == len(ranks):
            #if the rank appears 3 or more times and the cards only contains this rank
            return True
    return False