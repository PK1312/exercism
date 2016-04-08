year = raw_input("What year are you testing?" )

while True:
    try:
        if int(year) % 4 == 0 and int(year) % 100 == 0 and int(year) % 400 == 0:
            print str(year) + " is a leap year, and a special case one at that!"
            break
        elif int(year) % 4 == 0 and int(year) % 100 == 0 and int(year) % 400 != 0:
            print str(year) + " is not a leap year, because it is evenly divisble by 100 but not 400."
            break
        elif int(year) % 4 == 0 and int(year) % 100 != 0:
            print str(year) + " is a normal leap year!"
            break
        else:
            print str(year) + " is not a leap year."
            break
    except:
        print "Oops! You need to enter a number!"
        break
    break
