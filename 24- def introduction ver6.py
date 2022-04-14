
def import_os():
    import os
    os.system('cls')
import_os()

input_age = int(input('how old are you? '))

# Calender year to Century = divide the time value by 100
def calender_year_to_century(input_age):
    return input_age / 100

# Calender year to Decade = divide the time value by 10
def calender_year_to_decade(input_age):
    return input_age / 10

# Calender year to Month = multiply the time value by 12
def calender_year_to_month(input_age):
    return input_age * 12

# Calender year to Week = for an approximate result, multiply the time value by 52.143
def calender_year_to_week(input_age):
    return input_age * 52.143

# Calender year to Day = multiply the time value by 365
def calender_year_to_day(input_age):
    return input_age * 365

# Calender year to Hour = multiply the time value by 8760
def calender_year_to_hour(input_age):
    return input_age * 8760

# Calender year to Minute = multiply the time value by 525600
def calender_year_to_minute(input_age):
    return input_age * 525600

# Calender year to Second = for an approximate result, multiply the time value by 3.154e+7 =  31540000
def calender_year_to_second(input_age):
    return input_age * 31540000

print('Your age to Century = ',calender_year_to_century(input_age))
print('Your age to Decade  = ',calender_year_to_decade(input_age))
print('Your age to Month   = ',calender_year_to_month(input_age))
print('Your age to Week    = ',calender_year_to_week(input_age))
print('Your age to Day     = ',calender_year_to_day(input_age))
print('Your age to Hour    = ',calender_year_to_hour(input_age))
print('Your age to Minute  = ',calender_year_to_minute(input_age))
print('Your age to Second  = ',calender_year_to_second(input_age))