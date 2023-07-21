import os 
 
if __name__ == '__main__':
    print("Welcome to ROBOSPEAKER 1")
    while True:
        msg = input("Enter a text which you want me to speak")
        if  msg =="q":
            break
        command = f"say {msg}"
        os.system(command)
        
        
   
    
