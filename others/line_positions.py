myfile = open('myfile.txt')
line_pos = []

mypos = myfile.tell()
line_pos.append(mypos)
line = myfile.readline()
while line != '':
    mypos = myfile.tell()
    line_pos.append(mypos)
    line = myfile.readline()

