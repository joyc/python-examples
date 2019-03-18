# use the complement function
# read in lines from a file
# convert them to their DNA complement
# print the result

def complement(dna_string):
    dna_complement = {'a': 't',
                      'g': 'c',
                      't': 'a',
    #dna_complement = dict(a='t', c='g', t='a', g='c')
                      'c': 'g'}
    comp_string = ''
    for base in dna_string:
        comp_string += dna_complement.get(base, 'n')
        #if base in dna_complement:
            #comp_string += dna_complement[base]
        #else:
            #comp_string += 'n'
    return comp_string

dna_string = raw_input('Enter a DNA string file name:')
han = open(dna_string,'r').read()
comp_string = complement(han)
print "Complement is:", comp_string