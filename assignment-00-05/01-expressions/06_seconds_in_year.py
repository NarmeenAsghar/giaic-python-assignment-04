# --------------PROGRAM STATEMENT
'''
Use Python to calculate the number of seconds in a year
'''

def main():
# constant of year, days, hours, minutes, seconds
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minutes =  60
# calculation the number of seconds in year
    number_of_seconds = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minutes
    print(f"There are {number_of_seconds} seconds in a year")
# calling function
if __name__ == "__main__":
    main()