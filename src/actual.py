# Python Imports
from openpyxl import load_workbook
# Own Imports
from utils import check_previous_data, get_data_row, insert_data_row, print_log
from constants import DATA_ACTUAL, LOG, PROCESS, PATH, FILENAMES

# Checks if co_number already exists in final ACTUAL file (duplicated)
def check_duplicated (file_sheet, co_number):
    for i in range(2,  file_sheet.max_row + 1):
        po = file_sheet.cell(row=i, column=5).value
        position = file_sheet.cell(row=i, column=6).value
        amount = file_sheet.cell(row=i, column=15).value
        old_number = file_sheet.cell(row=i, column=22).value
        if (old_number == co_number):
            print_log(PROCESS.ACTUAL, LOG.ERROR, "Entry duplicated - " + str(po) + "-" + str(position) + " (amount " + str(amount) + ") with CO number " + str(co_number))
            return True
    return False

# Loop trough /data/new/REAL.xlsx entries adding them to /data/old/REAL.xlsx into /data/final/REAL.xlsx file
def process_actual_data(): 
    # Add new lines from NEW_ACTUAL to OLD_ACTUAL
    old_workbook = load_workbook(PATH.OLD.value + FILENAMES.ACTUAL.value)
    old_sheet = old_workbook.active
    new_workbook = load_workbook(PATH.NEW.value + FILENAMES.ACTUAL.value)
    new_sheet = new_workbook.active

    # Log
    print('\n')
    print_log(PROCESS.ACTUAL, LOG.INFO, f'Start processing {str(new_sheet.max_row - 1)} rows...')

    # Loop trough rows in new actual file
    counter, counter_error, counter_warnings = 0, 0, 0
    for i in range(2, new_sheet.max_row + 1):
        # get data from row
        data = get_data_row(new_sheet, i, DATA_ACTUAL.copy())
        # check if co_number already exists in final_actual
        if (check_duplicated(old_sheet, data["co_number"]["data"])):
            counter_error += 1
            continue
        # row relevante to insert
        counter += 1
        # check for previous information
        flag_updated, data = check_previous_data(old_sheet, data)
        if (flag_updated):
            counter_warnings += 1
            log_entry = f'Entry updated [row {i} {data["po_number"]["data"]}-{data["po_position"]["data"]}]: ' 
            for key in data:
                if (data[key]["updated"]):
                    log_entry += f'{key}#{data[key]["data"]} '
            print_log(PROCESS.ACTUAL, LOG.WARNING, log_entry.strip())
        # check tagetik stills blank (error)
        if (data["tagetik"]["data"]):
            counter_warnings += 1
            print_log(PROCESS.ACTUAL, LOG.WARNING, f'Tagetik not found - {str(data["po_number"]["data"])}-{str(data["po_position"]["data"])}--{str(data["co_number"]["data"])}')
        # insert data at the end of file
        insert_data_row(old_sheet, old_sheet.max_row + i - 1, data)
    
    # New actual file saved in final path
    old_workbook.save(PATH.FINAL.value + FILENAMES.ACTUAL.value)
    
    # Log
    print_log(PROCESS.ACTUAL, LOG.INFO, f'Finished processing... {str(counter)} rows added (WARNINGS: {str(counter_warnings)} - ERRORS: {str(counter_error)})')
