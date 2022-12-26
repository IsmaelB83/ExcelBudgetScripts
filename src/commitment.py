# Python Imports
from openpyxl import load_workbook
# Own Imports
from utils import check_previous_data, get_data_row, update_data_cell, print_log
from constants import DATA_COMMITMENT, LOG, PROCESS, PATH, FILENAMES

# Loop trough /data/new/REAL.xlsx entries adding them to /data/old/REAL.xlsx into /data/final/REAL.xlsx file
def process_commitment_data(): 
    # New commitment file replaces old commitment file
    old_workbook = load_workbook(PATH.OLD.value + FILENAMES.COMMITMENT.value)
    old_sheet = old_workbook.active
    new_workbook = load_workbook(PATH.NEW.value + FILENAMES.COMMITMENT.value)
    new_sheet = new_workbook.active

    # Log
    print('\n')
    print_log(PROCESS.COMMITMENT, LOG.INFO, f'Start processing {str(new_sheet.max_row - 1)} rows...')
    
    # Loop trough rows in new commitment file
    counter, counter_error, counter_warnings = 0, 0, 0
    for i in range(2, new_sheet.max_row + 1):
        # get data from row
        data = get_data_row(new_sheet, i, DATA_COMMITMENT.copy())
        # row relevante to insert
        counter += 1
        # check for previous information
        flag_updated, data = check_previous_data(old_sheet, data)
        if (flag_updated):
            counter_warnings += 1
            log_entry = f'Entry updated [row {i} {data["po_number"]["data"]}-{data["po_position"]["data"]}]: ' 
            for key in data:
                if (data[key]["updated"]):    
                    update_data_cell(new_sheet, i, data[key]["column"], data[key]["data"])
                    log_entry += f'{key}#{data[key]["data"]}'
            print_log(PROCESS.COMMITMENT, LOG.WARNING, log_entry.strip())
        # check tagetik stills blank and PO exists (error)
        if (data["tagetik"]["data"] == ""):
            counter_warnings += 1
            print_log(PROCESS.COMMITMENT, LOG.WARNING, f'ERROR - Tagetik not found - {str(data["po_number"]["data"])}-{str(data["po_position"]["data"])}')
    
    # New actual file saved in final path
    new_workbook.save(PATH.FINAL.value + FILENAMES.COMMITMENT.value)

    # Log
    print_log(PROCESS.COMMITMENT, LOG.INFO, f'Finished processing... {str(counter)} final rows (WARNINGS: {str(counter_warnings)} - ERRORS: {str(counter_error)})')
