"""
Author: Nadia Gainer
Date: 6/30/24
File Name: gainer_lemonadestandschedule.py
Description: lemonadestand schedule
"""

tasks = ["make lemonade", "promote lemonade stand", "clean lemonade stand", "open lemonade stand", "close lemonade stand"]
def lemonadetasks():
    for task in tasks:
        print(task)

lemonadetasks()
days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for i,day in enumerate(days):
    if day in ["saturday","sunday"]:
        print("off day")
    else:
        print(f"{day}-{tasks[i]}")