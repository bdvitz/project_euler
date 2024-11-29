# projecteuler.net solutions
def solution0019():
    """ Count Sundays between 1 Jan 1901 and 31 Dec 2000 """
    
    def feb(year: int) -> int:
        """ Return the days in February given the year """
        # there are no exceptions for the time period in question
        # if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
        # if leap year
        if (year % 4 == 0):
            return 29
        else:
            return 28
        
    def days_per_month(month: int, year: int) -> int:
        """ Return the number of days in the X month of the Y year """
        constant = {
            0: 31,
            2: 31,
            3: 30,
            4: 31,
            5: 30,
            6: 31,
            7: 31,
            8: 30,
            9: 31,
            10: 30,
            11: 31
        }
        if month in constant: return constant[month]
        else: return feb(year)
    
    day = 1 # start on a monday in 1900, only track in 1901 thru 2000
    month = 0
    year = 1900
    sunday_count = 0
    while year <= 2000:
        # check if first day of month is a Sunday for 1901 thru 2000
        if year >= 1901 and day % 7 == 0:
            sunday_count += 1
            print(day,month,year)
        
        # increment day, month, year
        day += days_per_month(month, year)
        month = (month+1) % 12
        year = year + (month == 0)
    
    return sunday_count
    
if __name__ == "__main__":
    print(solution0019())