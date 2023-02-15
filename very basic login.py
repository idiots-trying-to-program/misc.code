import time
def compute():
    for i in range(1000):
        ... 
        yield
from alive_progress import alive_bar
import sys
print("Welcome to the REMSC database!")
time.sleep(.5)
attempts = 0
print("Enter your Service number and your password.")
SN = input()
PW = input()
if SN == "11515523" and PW == "1001_Winning":
  print("Welcome back, Modeus.")
while SN != "11515523" or PW != "1001_Winning":
  attempts += 1
  print("Incorrect username and/or password, please try again.")
  print("Enter your Service number and your password.")
  SN = input()
  PW = input()
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
        print("County Shooting, General Purpose Rifle - L85A3: 2st place, January 2022")
        time.sleep(0.5)
        print("County Shooting, L81 Target Rifle: 2nd place, January 2021")
        main_body()
    else:
        print("Please enter an option")
        main_body()
main_body()