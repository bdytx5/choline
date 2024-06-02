import sys
from choline.commands import repeat, code, status, init, stream, launch, sync, kill, transer_data, chat
import os 

###### THIS IS FOR DEBG 
############### FOR PROD, rename REMOVETHISTRINGcholine.py to cj


def main():
    # command = sys.argv[1] if len(sys.argv) > 1 else None
    command = 'launch'
    cho_yaml_pth_or_model = ''
    if command == 'chat':
        if cho_yaml_pth_or_model == '':
            print("Choline launch must be run as root!")     

        chat.run(cho_yaml_pth_or_model)    
    if command == 'code':
        code.run()
    elif command == 'status':
        status.run()
    elif command == 'init':
        init.run()
    elif command == 'stream':
        stream.run()
    elif command == 'kill':
        kill.run()        
    elif command == 'launch':
        if os.geteuid() != 0:
            print("Choline launch must be run as root!")
            sys.exit(1)
        launch.run()
    elif command == 'sync':
        sync.run()
    elif command == 'spot':
        transer_data.run("byyoung3@34.28.218.185") 
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
