day = raw_input('What day is it? ')

if day == "Friday":
    date = int(raw_input('What date is it? '))
    if date != 13:
        print "TGIF"
    else:
        print "Ooooo spooky Friday the 13th"
else:
    print "Oh no..... zzzzzzzzz"
