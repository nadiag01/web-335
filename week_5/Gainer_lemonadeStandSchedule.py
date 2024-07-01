"""
Author: Nadia Gainer
Date: 6/30/24
File Name: gainer_lemonadestandschedule.py
Description: lemonadestand schedule
"""

tasks = ["make lemonade", "promote lemonade stand", "clean lemonade stand", "open lemonade stand", "close lemonade stand"]//tasks//
def lemonadetasks():
    for task in tasks:
        print(task)

lemonadetasks()
days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]//days of the week// 
for i,day in enumerate(days):
    if day in ["saturday","sunday"]:
        print("off day") //states days off for saturday and sunday// 
    else:
        print(f"{day}-{tasks[i]}") //print that task for each day of the week// 