# Checks if previous entry in ACTUAL/COMMITMENT file has different information in relevant fields for the dashboard
# In that case current extraction is udpated with old information, which is supossed to be validated in previous budget loads.
def check_previous_data (file_sheet, data_row):
    flag_updated = False
    for i in range(2,  file_sheet.max_row + 1):
        po_number = file_sheet.cell(row=i, column=data_row["po_number"]["column"]).value
        po_position = file_sheet.cell(row=i, column=data_row["po_position"]["column"]).value
        if (po_number == data_row["po_number"]["data"] and po_position == data_row["po_position"]["data"]):
            for key in data_row :
                if (data_row[key]["check"]):    
                    old_data = file_sheet.cell(row=i, column=data_row[key]["column"]).value                    
                    if (old_data != data_row[key]["data"]):
                        flag_updated = True
                        data_row[key]["data"] = old_data
                        data_row[key]["updated"] = True
            return flag_updated, data_row
    return False, data_row

# Extract data information form a row in the ACTUAL file
def get_data_row(sheet, row, data): 
    for key in data:
        data[key]["data"] = sheet.cell(row=row, column=data[key]["column"]).value
    return data

# Insert current data dictionary into destination excel sheet
def insert_data_row(sheet, row, data): 
    for key in data:
        sheet.cell(row=row, column=data[key]["column"]).value = data[key]["data"]

# Updates data of specific cell
def update_data_cell(sheet, row, col, data): 
    sheet.cell(row=row, column=col).value = data

# Prints log
def print_log(process, type, log):
    print(f'[{process.value}] - {type.value} - {log}')
    
    