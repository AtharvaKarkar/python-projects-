import os 
 
if __name__ == '__main__':
    print("Welcome to ROBOSPEAKER 1")
    msg = input("Enter a text which you want me to speak")
    command = f"say {msg}"
    os.system(command)
    
