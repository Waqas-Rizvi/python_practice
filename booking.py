# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "car_model": "", # corolla, civic

    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone and car_model

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone  and car_model
# above program should not accept this booking as the slot is already booked by the first iteration

# You must write the following functions

# add_tz() # this should convert naive date to tz_awre
# convert_tz() # this should convert date from one tz to another
# is_slot_available() # this should return True or False
# book_the_car() # this should add the detail in booking_storage

# I didn't mention what info you need to pass to the above functions. Its part of your assigment to pass info to the function and return the value from function.


from datetime import datetime
import pytz


booking_storage = []


def is_slot_available(start_Date, end_Date, car_Model):
    for booking in booking_storage:
        if start_Date == booking["start_date"] or end_Date == booking["end_date"]:
            return False
    else:
        return True


def add_tz(date, timezone):
    return timezone.localize(date)


def convert_tz(date, timezone):
    return date.astimezone(timezone)


def book_the_car():
    for i in range(5):
        start_date_str = input(
            "Enter booking start date and time (YYY-MM-DD HH:MM:SS): ")
        end_date_str = input(
            "Enter booking end date and time (YYY-MM-DD HH:MM:SS): ")
        timezone_str = input("Enter timezone: ")
        car_model = input("Enter Car Model: ")

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
        timeZone = pytz.timezone(timezone_str)

        start_date_tzDetails = add_tz(start_date, timeZone)
        end_date_tzDetails = add_tz(end_date, timeZone)
        utc_format = pytz.utc
        convert_start_Date = convert_tz(start_date_tzDetails, utc_format)
        convert_end_Date = convert_tz(end_date_tzDetails, utc_format)

        match = is_slot_available(
            convert_start_Date, convert_end_Date, car_model)
        if match:
            booking_storage.append({
                "start_date": convert_start_Date,
                "end_date": convert_end_Date,
                "car_model": car_model
            })
            print("Booking Successful")
        else:
            print("Slot Already Booked")
            continue


book_the_car()
