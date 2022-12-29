# Own imports
from constants import DATA_ACTUAL, DATA_COMMITMENT, LOG_ERRORS, LOG_WARNING

# Checks if co_number already exists in final ACTUAL file (duplicated)
def check_duplicated (file_sheet, max_row, co_number):
    for i in range(2,  max_row):
        old_number = file_sheet.cell(row=i, column=22).value
        if (old_number == co_number):
            return True
    return False

# For non-po costs this function tries with default assignments based on allocation and vendor information
def check_default_assignments (process, data_row):
    # Initialization
    flag_updated = True
    # Relevant fields
    orden = data_row['orden']['data']
    proveedor = data_row['proveedor']['data']
    descripcion_cuenta = data_row['descripcion_cuenta']['data']
    if (process.value == 'ACTUAL'):
        clase_documento = data_row['clase_documento']['data']
        if (clase_documento == 'AA' or clase_documento == 'ZL'):    # Capex (ignore)
            data_row['ignorar']['updated'] = True
            data_row['ignorar']['data'] = True
            data_row['observaciones']['updated'] = True
            data_row['observaciones']['data'] = 'CAPEX'
        else:
            match orden:
                case '100000000192':                                # Licencias
                    data_row['tagetik']['updated'] = True
                    data_row['tagetik']['data'] = 'EN00272'
                case '100000000193':                                # Corp
                    data_row['tagetik']['updated'] = True
                    data_row['tagetik']['data'] = 'NA'
                case '100000000893':                                # Comms
                    data_row['tagetik']['updated'] = True
                    data_row['tagetik']['data'] = 'EN00187'
                case '100000000350':                            
                    match proveedor:
                        case '10002973':                            # Renting  
                            data_row['tagetik']['updated'] = True
                            data_row['tagetik']['data'] = 'EN00166'
                        case _:
                            flag_updated = False
                case '100000000354':
                    match proveedor:
                        case '30002547':                            # Tasas RadioElectríco
                            data_row['tagetik']['updated'] = True
                            data_row['tagetik']['data'] = 'EN00201'
                        case _:
                            flag_updated = False
                case _:
                    flag_updated = False
    else:
        flag_updated = False
    return flag_updated, data_row
    
# Checks if previous entry in ACTUAL/COMMITMENT file has different information in relevant fields for the dashboard
# In that case current extraction is udpated with old information, which is supossed to be validated in previous budget loads.
def check_previous_data (process, file_sheet, data_row):
    # Initialization
    flag_updated = False
    current_pedi = data_row['po_number']['data']
    current_posi = data_row['po_position']['data']
    # Only check items coming from POs
    if (current_pedi == None or current_pedi == ''):
        return False, data_row
    # Loop trough all old actual file
    for i in range(2,  file_sheet.max_row + 1):
        old_pedi = file_sheet.cell(row=i, column=data_row['po_number']['column']).value
        old_posi = file_sheet.cell(row=i, column=data_row['po_position']['column']).value
        # Only check against PO items
        if (old_pedi != None and old_pedi == current_pedi and old_posi == current_posi):
            for key in data_row :
                if (data_row[key]['check']):
                    old_data = get_data_cell(process, file_sheet, i, key)
                    if (old_data != data_row[key]['data']):
                        flag_updated = True
                        data_row[key]['data'] = old_data
                        data_row[key]['updated'] = True
            return flag_updated, data_row
    return False, data_row

# Get data from cell depending of the data structure (ACTUAL/COMMITMENT)
def get_data_cell(process, file_sheet, row, key):
    col_index = DATA_ACTUAL[key]['column']
    if (process.value == 'COMMITMENT'):
        col_index = DATA_COMMITMENT[key]['column']
    return file_sheet.cell(row=row, column=col_index).value
    
# Extract data information form a row in the ACTUAL file
def get_data_row(process, sheet, row, data):
    for key in data:
        column_index = data[key]['column']
        if (column_index != None):
            raw_data = sheet.cell(row=row, column=column_index).value
            try:
                # Transform data format
                if (raw_data == None or raw_data == ''):
                    data[key]['data'] = raw_data
                else:
                    match data[key]['type']:
                        case 'string':
                            # Solicitante replaces 'i:0#.w|acciona\\' with nothing
                            if (key == 'solicitante'):
                                raw_data = raw_data.replace('i:0#.w|acciona\\', '')
                            data[key]['data'] = raw_data
                        case 'int':
                            data[key]['data'] = int(raw_data)
                        case 'float':
                            data[key]['data'] = float(raw_data)
            except Exception:
                data[key]['data'] = raw_data
    return data

# Insert current data dictionary into destination excel sheet
def insert_data_row(sheet, row, data): 
    for key in data:
        sheet.cell(row=row, column=data[key]['column']).value = data[key]['data']

# Updates data of specific cell
def update_data_cell(sheet, row, col, data): 
    sheet.cell(row=row, column=col).value = data

# Prints log
def print_log(process, type, po_number, po_position, co_number, amount, message):
    if (type.value == 'E'): 
        LOG_ERRORS.append([process.value, type.value, po_number, po_position, co_number, amount, message])
    else:
        LOG_WARNING.append([process.value, type.value, po_number, po_position, co_number, amount, message])