# Python imports
import sys
from os import path
from tabulate import tabulate
from datetime import datetime
# Own imports
from constants import PROCESS, LOG_HEADER, LOG_ERRORS, LOG_WARNING, PATH, FILENAMES
from commitment import process_commitment_data  
from actual import process_actual_data

# Process actual and then commitment 
def main():
    
    # Save reference to original stdout
    original_stdout = sys.stdout
    
    # Process actual
    if (path.isfile(PATH.NEW.value + FILENAMES.ACTUAL.value)):  
        process_actual_data()
    else:
        print(f'\n{PROCESS.ACTUAL.value}, File not found...') 
    
    # Process commitment
    if (path.isfile(PATH.NEW.value + FILENAMES.COMMITMENT.value)):  
        process_commitment_data()
    else:
        print(f'\n{PROCESS.COMMITMENT.value}, File not found...') 

    # Display errors in screen
    print('ERROR LOG: \n')
    print(tabulate(LOG_ERRORS, headers=LOG_HEADER, tablefmt="grid"))
    
    # Save logs to file
    with open(f'./logs/log_{datetime.now().date()}.txt', 'w') as f:
        sys.stdout = f
        print(tabulate(LOG_ERRORS, headers=LOG_HEADER, tablefmt="grid"))
        print('\n')
        print(tabulate(LOG_WARNING, headers=LOG_HEADER, tablefmt="grid"))
        sys.stdout = original_stdout
    
   
# Entry point
if __name__ == '__main__':
    main()