# Python imports
from os import path
# Own imports
from constants import PROCESS, LOG, PATH, FILENAMES
from commitment import process_commitment_data
from actual import process_actual_data
from utils import print_log

# Process actual and then commitment 
def main():
    
    # Process actual
    if (path.isfile(PATH.NEW.value + FILENAMES.ACTUAL.value)):  
        process_actual_data()
    else:
        print('\n')
        print_log(PROCESS.ACTUAL, LOG.ERROR, f'ACTUAL file not found...') 
    
    # Process commitment
    if (path.isfile(PATH.NEW.value + FILENAMES.COMMITMENT.value)):  
        process_commitment_data()
    else:
        print('\n')
        print_log(PROCESS.COMMITMENT, LOG.ERROR, f'COMMITMENT file not found...')

# Entry point
if __name__ == '__main__':
    main()