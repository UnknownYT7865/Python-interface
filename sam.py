from termcolor import colored
import os
def sam():
    os.system('clear')
    a="""
      _    _ _   _ _  ___   _  ______          ___   _     __     _________ 
     | |  | | \ | | |/ / \ | |/ __ \ \        / / \ | |    \ \   / /__   __|
     | |  | |  \| | ' /|  \| | |  | \ \  /\  / /|  \| |     \ \_/ /   | |   
     | |  | | . ` |  < | . ` | |  | |\ \/  \/ / | . ` |      \   /    | |   
     | |__| | |\  | . \| |\  | |__| | \  /\  /  | |\  |       | |     | |   
      \____/|_| \_|_|\_\_| \_|\____/   \/  \/   |_| \_|       |_|     |_|   
                                                                        
                                                                        
    """
    colored_text=colored(a,'yellow')
    print(colored_text)
sam()
while True:
    print(colored("Password kay hai tera : ","green"))
    key=str(input())
    
    if key == "Sameer":
        sam()
        break
    sam()
    print(colored("Galat Password dala hai bhai tune","red"))
