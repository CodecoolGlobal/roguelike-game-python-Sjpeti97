import time
import shutil
import operator
import util


def story():
    main_picture = """

██       ██████  ██████  ██████           ██████  ███████         ████████ ██   ██ ███████         ██████   █████  
██      ██    ██ ██   ██ ██   ██         ██    ██ ██                 ██    ██   ██ ██              ██   ██ ██   ██ 
██      ██    ██ ██████  ██   ██         ██    ██ █████              ██    ███████ █████           ██████  ███████ 
██      ██    ██ ██   ██ ██   ██         ██    ██ ██                 ██    ██   ██ ██              ██      ██   ██ 
███████  ██████  ██   ██ ██████           ██████  ██                 ██    ██   ██ ███████         ██      ██   ██                                                                                                                                                                                                 
"""
    text_line(main_picture.center(100))
    text = "!Welcome to our Lord Of The Pa's game!"
    story_line(text.center(100))
    text2 = "* You can choose of 3 characters with different inventories and abilities."
    print()
    story_line(text2.center(100))
    text3 = "* Find the rings, to move on maps and kill the final boss!"
    print()
    story_line(text3.center(100))
    text4 = "* You can restore you healt and put on armor if need."
    time.sleep(1)
    print()
    story_line(text4.center(100))
    util.clear_screen()
    time.sleep(2)

    print("""
██ ██     ██  █████  ██████  ███    ██ ██ ███    ██  ██████  ██ 
██ ██     ██ ██   ██ ██   ██ ████   ██ ██ ████   ██ ██       ██ 
██ ██  █  ██ ███████ ██████  ██ ██  ██ ██ ██ ██  ██ ██   ███ ██ 
   ██ ███ ██ ██   ██ ██   ██ ██  ██ ██ ██ ██  ██ ██ ██    ██    
██  ███ ███  ██   ██ ██   ██ ██   ████ ██ ██   ████  ██████  ██                                               
""")

    time.sleep(2)
    print()
    text6 = "* You get hit by the enemies without your weapon!"
    story_line(text6)
    time.sleep(2)
    util.clear_screen()

    luck = """
 ██████   ██████   ██████  ██████      ██      ██    ██  ██████ ██   ██ ██ 
██       ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██  ██ 
██   ███ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      █████   ██ 
██    ██ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██     
 ██████   ██████   ██████  ██████      ███████  ██████   ██████ ██   ██ ██                                                                      
"""
    text_line(luck)
    time.sleep(2)
    util.clear_screen()

def story_line(text):
    for char in text:
        print(char, sep=' ', end='', flush=True)
        time.sleep(0.05)
    print()    

def text_line(text):
    for char in text:
        print(char, sep=' ', end='', flush=True)
        time.sleep(0.005)
    print() 
