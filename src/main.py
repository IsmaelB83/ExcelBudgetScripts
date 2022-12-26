# Python imports
# Own imports
from actual import process_actual_data
from commitment import process_commitment_data

def main():
    # Process actual files
    process_actual_data()
    # Process commitment files
    process_commitment_data()

if __name__ == '__main__':
    main()