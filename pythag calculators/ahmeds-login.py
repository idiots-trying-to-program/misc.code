import time
def compute():
    for i in range(1000):
        ... 
        yield
from alive_progress import alive_bar
import sys
#LOGIN TABLE
sntable = ["11515523"]
name = ["Erin"]
#LOGIN TABLE END
print("Welcome to the REMSC database!")
time.sleep(.5)
attempts = 0
print("Enter your Service number")
SN = input()
if SN in sntable:
    print("Place your finger on the scanner")
    input()
    for i in range(1):
        with alive_bar(50, ctrl_c=False, title=f'Scanning...') as bar:
            for i in range(100):
                time.sleep(0.02)
                bar()
    if SN == sntable[0]:
        name1 = name[0]
    print("Welcome back,", name1)
while SN not in sntable:
  attempts += 1
  print("Incorrect service number.")
  print("Enter your Service number.")
  SN = input()
  if attempts == 3:
   sys.exit("Too many failed attempts.")
time.sleep(1)
def main_body(): 
    print("What services would you like to access?")
    time.sleep(0.5)
    print("1. Mission Briefing")
    print("2. Current Rank Progress")
    print("3. Skills progress")
    ch = input()
    if ch == "1":
        print("tobedone")
    if ch == "2":
        for i in range(1):
            with alive_bar(100, ctrl_c=False, title=f'Retrieving info...') as bar:
                for i in range(100):
                    time.sleep(0.02)
                    bar()
        print("Current Rank: L.Cpl")
        time.sleep(0.8)
        print("Press enter to continue...")
        input()
        main_body()
    if ch == "3":
        print("Shooting progress:")
        for i in range(1):
            with alive_bar(100, ctrl_c=False, title=f'Retrieving info...') as bar:
                for i in range(100):
                    time.sleep(0.02)
                    bar()        
        time.sleep(0.5)
        print("Weapon Handling test, General Purpose Rifle - L85A3: Passed")
        time.sleep(0.5)
        print("Weapon Handing test, L81 Target Rifle: Passed")
        time.sleep(0.5)
        print("County Shooting, General Purpose Rifle - L85A3: 1st place, July 2022")
        time.sleep(0.5)
        print("County Shooting, General Purpose Rifle - L85A3: 2st place, January 2023")
        time.sleep(0.5)
        print("County Shooting, L81 Target Rifle: 2nd place, January 2021")
        main_body()
    else:
        print("Please enter an option")
        main_body()
main_body()