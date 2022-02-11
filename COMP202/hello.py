fi = open('hello.txt', 'r')
fo = open('fout', 'w')

fo.write(fi.read()[::-1].strip())

fi.close()
fo.close()

x = [1,2,3]
while x.sort() != x:
    x = []