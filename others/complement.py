# given a string of DNA - lower case
# convert that string to its complementary DNA
# use dict


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

dna_string = raw_input('Enter a DNA string:')
comp_string = complement(dna_string)
print "Complement is:", comp_string
