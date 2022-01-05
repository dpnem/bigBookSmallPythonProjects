"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
View this code at https://inventwithpython.com/bigbookpython/project8.html
Tags: short"""

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:  # Lo to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numberic year, like 2023.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for a calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Pleasee enter a numeric month, like 3 for March.')
        continue
    
    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')

def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar

    # Put the month and year at the top of the calendar:
    print(MONTHS[month-1])
    calText += (' ' * 34) + MONTHS[month-1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abreviations: SUN, MON, TUE, etc.
    calText += '...Sunday.....Monday....Tuesday...Wedensday...Thursday....Friday....Saturday..\n'
 
    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have twn spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date of the month. (The dateime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back the Current Date until it is a Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):  # (!) Try chaning the 4 to a 5 or 10.
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    return calText

calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

