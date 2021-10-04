# DiscordCleaner.py
# 10/4/2021
#
# Made by: Will Schick
#
# Support Cybersecurity Awareness! 
# https://staysafeonline.org/cybersecurity-awareness-month/about-the-month/
#
# Instructions:
#   1. Execute script and navigate to discord chat window (within 5 seconds)
#   2. Navigate to chat window (make sure your x in the top right of discord's gui is visible)
#   3. The script will now begin deleting messages
#   4. When you're satisfied with the number of messages deleted you can minimize discord and the script will activate its failsafe
#       4.5 Alternatively you can move your mouse to the top left of the screen to activate pyautogui's failsafe

import pyautogui;
import os, time, random;

# Our version of Robots.txt compliance
NUM_COMMANDS = 6.1
MIN_SLEEP = 120//NUM_COMMANDS # In MS
MAX_SLEEP = 250//NUM_COMMANDS # In MS
KEYPRESS_INTERVAL = 0.120; # Time between pressing down a key and lifting it (in ms)
    
# Sleeps for a random amount of time in ms
def randomSleep(minSleep=MIN_SLEEP, maxSleep=MAX_SLEEP):
    if minSleep < maxSleep:
        sleepTime = random.randint(minSleep, maxSleep)
    else:
        sleepTime = minSleep

    time.sleep(sleepTime//1000)

# Returns true if an image is on screen
def isGuiOnScreen(imageName):
    cwd = os.path.dirname(os.path.realpath(__file__))
    projDir = os.path.abspath(os.path.join(cwd, os.pardir))
    guiDir = projDir + "\\resources\\discordGUI\\"

    try:
        location = pyautogui.locateOnScreen(guiDir + imageName, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        return False

    if location is None:
        return False
    
    return True

# Determine if the discord client is still on screen
def isDiscordVisible():

    darkExitOnScreen = isGuiOnScreen("discordExitButton(Dark).png")
    lightExitOnScreen = isGuiOnScreen("discordExitButton(Light).png")

    if darkExitOnScreen or lightExitOnScreen:
        return True
    
    print("Discord client not found on screen, aborting...")
    return False


def upArrow():
    if not isDiscordVisible():
        return
    
    pyautogui.press("up", interval=KEYPRESS_INTERVAL)

def ctrl_A():
    if not isDiscordVisible():
        return

    pyautogui.hotkey("ctrl", "a")

def delete():
    if not isDiscordVisible():
        return

    pyautogui.press("delete", interval=KEYPRESS_INTERVAL)

def enter():
    if not isDiscordVisible():
        return

    pyautogui.press("enter", interval=KEYPRESS_INTERVAL)

def pageUp():
    if not isDiscordVisible():
        return
        
    pyautogui.press("pageup", interval=KEYPRESS_INTERVAL)

def main():

    time.sleep(5)

    loopCount = 0
    while isDiscordVisible():
        delete()
        randomSleep()

        upArrow()
        randomSleep()
        
        ctrl_A()
        randomSleep()

        delete()
        randomSleep()

        enter()
        randomSleep(minSleep=1000)

        # failsafe: If the gui for deleting a message isn't on screen we need to break
        if not isGuiOnScreen("delete.png"):
            print("No delete button found on screen, aborting...")
            break;

        enter()
        randomSleep()

        loopCount += 1

        # every ten messages page up so we're continuously loading old messages
        if (loopCount % 10) == 0:
            pageUp()
    
    print("I completed", loopCount, "loops!")


main()
