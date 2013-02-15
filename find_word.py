
def find_word(search_term, word_list):
    # matching words is those elements of word_list, such that the element matches search_term
    matching_words = []
    for element in word_list:
        if search_term in element:
            matching_words.append(element)
    return matching_words
    
mystrings = [ 'frog', 'fox', 'foxtrot', 'toad' ]

search_term = raw_input("Enter a word to search for:")

words_found = find_word(search_term, mystrings)
print "I found:", words_found, "my search term was:", 'fox'

myotherlist = ['bang', 'thump', 'biff']
print "Searched for 'b'", find_word('b', myotherlist)
