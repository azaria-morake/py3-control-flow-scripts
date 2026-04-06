#!/usr/bin/env python3

current_temp = int(input("Enter current temperature: "))
desired_temp = int(input("Enter desired temperature: "))
system_status = input("Enter system status: ")

def smart_thermo(current_temp, desired_temp, system_status):

    if system_status == "maintenance":
        print("System offline for repairs.")
    elif system_status == "on":
        if current_temp > (desired_temp + 2):
            print("Cooling active.")
        elif current_temp < (desired_temp - 2):
            print("Heating active.")
        else:
            print("Temperature stable. Standby mode.")
    else:
        print("System is powered down.")

smart_thermo(current_temp, desired_temp,
   system_status)
