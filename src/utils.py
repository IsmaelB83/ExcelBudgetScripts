# Checks if co_number already exists in final ACTUAL file (duplicated)
def check_duplicated (file_sheet, max_row, co_number):
    for i in range(2,  max_row):
        old_number = file_sheet.cell(row=i, column=22).value
        if (old_number == co_number):
            return True
    return False

# For non-po costs this function tries with default assignments based on allocation and vendor information
def check_default_assignments (process, file_sheet, data_row):
    # Initialization
    flag_updated = False
    # Relevant fields
    orden = data_row["orden"]["data"]
    proveedor = data_row["proveedor"]["data"]
    descripcion_cuenta = data_row["descripcion_cuenta"]["data"]
    if (process.value == 'ACTUAL'):
        clase_documento = data_row["clase_documento"]["data"]
        if (clase_documento == 'AA' or clase_documento == 'ZL'):    # Capex (ignore)
            flag_updated = True
            data_row["ignorar"]["updated"] = True
            data_row["ignorar"]["data"] = True
            data_row["observaciones"]["updated"] = True
            data_row["observaciones"]["data"] = 'CAPEX'
        elif(orden == 100000000192):                                # Licencias
            data_row["tagetik"]["updated"] = True
            data_row["tagetik"]["data"] = 'EN00272'
        elif(orden == 100000000193):                                # Corp
            data_row["tagetik"]["updated"] = True
            data_row["tagetik"]["data"] = 'NA'
        elif(orden == 100000000893 ):                               # Comms
            data_row["tagetik"]["updated"] = True
            data_row["tagetik"]["data"] = 'EN00187'
        elif(orden == 100000000350 and proveedor == 10002973):      # Renting
            data_row["tagetik"]["updated"] = True
            data_row["tagetik"]["data"] = 'EN00166'
        elif(orden == 100000000354 and proveedor == 30002547):      # Tasas RadioElectríco
            data_row["tagetik"]["updated"] = True
            data_row["tagetik"]["data"] = 'EN00201'
    return flag_updated, data_row
    
# Checks if previous entry in ACTUAL/COMMITMENT file has different information in relevant fields for the dashboard
# In that case current extraction is udpated with old information, which is supossed to be validated in previous budget loads.
def check_previous_data (process, file_sheet, data_row):
    # Initialization
    flag_updated = False
    current_pedi = data_row["po_number"]["data"]
    current_posi = data_row["po_position"]["data"]
    # Only check items coming from POs
    if (current_pedi == None or current_posi == None):
        return False, data_row
    # Loop trough all old actual file
    for i in range(2,  file_sheet.max_row + 1):
        old_pedi = file_sheet.cell(row=i, column=data_row["po_number"][get_column_index(process)]).value
        old_posi = file_sheet.cell(row=i, column=data_row["po_position"][get_column_index(process)]).value
        # Only check against PO items
        if (old_pedi != None and old_posi != None and old_pedi == current_pedi and old_posi == current_posi):
            for key in data_row :
                if (data_row[key]["check"]):
                    old_data = get_data_cell(process, file_sheet, i, data_row[key])
                    if (old_data != data_row[key]["data"]):
                        flag_updated = True
                        data_row[key]["data"] = old_data
                        data_row[key]["updated"] = True
            return flag_updated, data_row
    return False, data_row

# Get data from cell depending of the data structure (ACTUAL/COMMITMENT)
def get_data_cell(process, file_sheet, row, item):
    return file_sheet.cell(row=row, column=item[get_column_index(process)]).value 
    
# Extract data information form a row in the ACTUAL file
def get_data_row(process, sheet, row, data):
    for key in data:
        data[key]["data"] = sheet.cell(row=row, column=data[key][get_column_index(process)]).value
    return data

# Insert current data dictionary into destination excel sheet
def insert_data_row(process, sheet, row, data): 
    for key in data:
        sheet.cell(row=row, column=data[key][get_column_index(process)]).value = data[key]["data"]

# Updates data of specific cell
def update_data_cell(sheet, row, col, data): 
    sheet.cell(row=row, column=col).value = data

# Prints log
def print_log(process, type, log):
    print(f'[{process.value}] - {type.value} - {log}')
    
def get_column_index (process):
    if (process.value == 'COMMITMENT'):
        return 'column_com'
    return 'column_act'