import sys
from choline.commands import repeat, code, status, init, stream, launch, sync, kill
import os 
def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None

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
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
