def get_keys(d, v):
    keys = []
    for i in d:
        if d[i] == v:
            keys.append(i)
    return keys

def diag_dict(m):
    d = {}
    i = 0
    for x in m:
        d[x[i]] = x[:i] + x[i+1:]
        i += 1
    return d
my_list = [['a',2],['b',5],['c',5],['q','q'],[3,2]]
d = {}
for i in range(len(my_list)-1):
    d[my_list[i][0]],d[my_list[i+1][0]] = my_list[i][1], my_list[i+1][1]
print(d)


x='hello'
c=x.split('\t')
print(c[:-1])
