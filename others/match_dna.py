def match_dna(query, sequence):
    if query in sequence:
        return True
    else:
        return False
        
    # if query is in sequence:
    # return True
    # else
    # return False
    
    # for example
    # match_dna('gaa', 'gaatta') returns True
    # match_dna('aaa', 'gaatta') returns False


mydna = 'gaaacctta'
myquery = 'ggc'
if match_dna(myquery, mydna):
    print "Yay it matches"
else:
    print "No it doesn't match"
