month = raw_input('What month is it? ')

if month == 'January':
    print 1
elif month == 'February':
    print 2
elif month == 'March':
    print 3
else:
    print "later than March"
    
if month == 'January':
    print 1
else:
    if month == 'February':
        print 2
    else:
        if month == 'March':
            print 3
