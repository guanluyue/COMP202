fi = open('hello', 'r')
fo = open('fout', 'w')
text = ''
for _ in fi:
    text += _
fo.writeline(text.string())
fi.close()
fo.close()