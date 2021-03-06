import time
import shutil
import operator
import util
import shutil

middle = shutil.get_terminal_size().columns

def story():
    main_picture = """
    ██       ██████  ██████  ██████           ██████  ███████         ████████ ██   ██ ███████         ██████   █████  
    ██      ██    ██ ██   ██ ██   ██         ██    ██ ██                 ██    ██   ██ ██              ██   ██ ██   ██ 
    ██      ██    ██ ██████  ██   ██         ██    ██ █████              ██    ███████ █████           ██████  ███████ 
    ██      ██    ██ ██   ██ ██   ██         ██    ██ ██                 ██    ██   ██ ██              ██      ██   ██ 
    ███████  ██████  ██   ██ ██████           ██████  ██                 ██    ██   ██ ███████         ██      ██   ██                                                                                                                                                                                                 
    """
    text_line(main_picture.center(middle))
    time.sleep(3)
    util.clear_screen()
    time.sleep(1.5)
    print()
    text = "!Welcome to our Lord Of The Pa's game!"
    print()
    print()
    story_line(text.center(middle))
    time.sleep(1.5)
    print()
    text2 = "* You can choose from 3 characters with different inventories and abilities."
    print()
    story_line(text2.center(middle))
    time.sleep(1.5)
    print()
    text3 = "* Find the rings, to move on maps and kill the final boss!"
    print()
    story_line(text3.center(middle))
    time.sleep(1.5)
    print()
    text4 = "* You can restore your health and put on armor if needed."
    time.sleep(1.5)
    print()
    story_line(text4.center(middle))
    time.sleep(1.5)
    print()
    time.sleep(2)
    util.clear_screen()

    print("""
    ██ ██     ██  █████  ██████  ███    ██ ██ ███    ██  ██████  ██ 
    ██ ██     ██ ██   ██ ██   ██ ████   ██ ██ ████   ██ ██       ██ 
    ██ ██  █  ██ ███████ ██████  ██ ██  ██ ██ ██ ██  ██ ██   ███ ██ 
       ██ ███ ██ ██   ██ ██   ██ ██  ██ ██ ██ ██  ██ ██ ██    ██    
    ██  ███ ███  ██   ██ ██   ██ ██   ████ ██ ██   ████  ██████  ██                                               
    """.center(middle))

    time.sleep(2)
    util.clear_screen()
    print()
    text6 = "* You'll get hit by the enemies without your weapon!"
    story_line(text6.center(middle))
    time.sleep(2)
    util.clear_screen()

    luck = """
     ██████   ██████   ██████  ██████      ██      ██    ██  ██████ ██   ██ ██
    ██       ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██  ██
    ██   ███ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      █████   ██ 
    ██    ██ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██     
     ██████   ██████   ██████  ██████      ███████  ██████   ██████ ██   ██ ██                                                                      
    """.center(middle)
    text_line(luck.center(middle))
    time.sleep(2)
    util.clear_screen()

def dead():
    util.clear_screen()
    text_dead = """      
    ██    ██ ██████  ██    ██      █████  ██████  ███████     ██████  ███████  █████  ██████      ██ 
     ██  ██ ██    ██ ██    ██     ██   ██ ██   ██ ██          ██   ██ ██      ██   ██ ██   ██     ██ 
      ████  ██    ██ ██    ██     ███████ ██████  █████       ██   ██ █████   ███████ ██   ██     ██ 
       ██   ██    ██ ██    ██     ██   ██ ██   ██ ██          ██   ██ ██      ██   ██ ██   ██        
       ██    ██████   ██████      ██   ██ ██   ██ ███████     ██████  ███████ ██   ██ ██████      ██ 
       """
    flash(text_dead)

def win():
    util.clear_screen()
    win_text = """
    ██     ██    ██      ██████      ██    ██             ██     ██     ██     ███    ██     ██ 
    ██      ██  ██      ██    ██     ██    ██             ██     ██     ██     ████   ██     ██ 
    ██       ████       ██    ██     ██    ██             ██  █  ██     ██     ██ ██  ██     ██ 
              ██        ██    ██     ██    ██             ██ ███ ██     ██     ██  ██ ██        
    ██        ██         ██████       ██████               ███ ███      ██     ██   ████     ██
    """
    flash(win_text)
        
def oldman():
    util.clear_screen()
    print()
    text1 = "-Hello traveler, I have waited for you."
    text2 = "-You have to kill the final boss before he attacks the city!"
    text3 = "-Here is the final ring for the fight 💍 "
    text4 = "-Good luck! You are our last chance to survive..."
    text5 = "HINT: Do you have the rigth weapon's level?"
    text6 = "HINT: Do you have enough healt and armor?"
    story_line(text1.center(middle))
    time.sleep(1.5)
    print()
    story_line(text2.center(middle))
    time.sleep(1.5)
    print()
    story_line(text3.center(middle))
    time.sleep(1.5)
    print()
    story_line(text4.center(middle))
    time.sleep(3)
    print()
    story_line(text5.center(middle))
    time.sleep(1.5)
    print()
    story_line(text6.center(middle))
    time.sleep(1.5)
    print()
    util.clear_screen()

def flash(text):
    flash_time = 3
    for flash in range(flash_time):
        util.clear_screen()
        time.sleep(1)
        print(text)
        time.sleep(1)

def story_line(text):
    for char in text:
        print(char, sep=' ', end='', flush=True)
        time.sleep(0.005) 

def text_line(text):
    for char in text:
        print(char, sep=' ', end='', flush=True)
        time.sleep(0.005)
    print() 
