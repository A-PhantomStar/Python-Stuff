def timeUser(days, hours, minutes, seconds):
    days*=24*60*60
    hours*=60*60 
    minutes*=60
    seconds = seconds + minutes + hours + days
    print("The total seconds is:", seconds)

daysUser = int(input("Enter days\n >"))
hourUser = int(input("Enter hours\n >"))
minutesUser = int(input("Enter minutes\n >"))
secondsUser = int(input("Enter seconds\n >"))

timeUser(daysUser, hourUser, minutesUser, secondsUser)
