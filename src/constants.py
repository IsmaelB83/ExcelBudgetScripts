from enum import Enum
 
class LOG(Enum):
    ERROR = 'E'
    INFO = 'I'
    WARNING = 'W'   
    
class PROCESS(Enum):
    ACTUAL = 'ACTUAL'
    COMMITMENT = 'COMMITMENT'    
    
class PATH(Enum):    
    OLD = "./data/old/"
    NEW = "./data/new/"
    FINAL = "./data/final/"

class FILENAMES(Enum):    
    ACTUAL = "REAL.xlsx"
    COMMITMENT = "COMPROMETIDO.xlsx"
    
DATA = {
    "sociedad":             {  "column_act": 1,   "column_com": 1,     "data": "",  "check": False,  "updated": False  },
    "orden":                {  "column_act": 2,   "column_com": 2,     "data": "",  "check": False,  "updated": False  },
    "descripcion_orden":    {  "column_act": 3,   "column_com": 3,     "data": "",  "check": False,  "updated": False  },
    "proveedor":            {  "column_act": 4,   "column_com": 4,     "data": "",  "check": False,  "updated": False  },
    "po_number":            {  "column_act": 5,   "column_com": 5,     "data": "",  "check": False,  "updated": False  },
    "po_position":          {  "column_act": 6,   "column_com": 6,     "data": "",  "check": False,  "updated": False  },
    "ejercicio":            {  "column_act": 7,   "column_com": 7,     "data": "",  "check": False,  "updated": False  },
    "periodo":              {  "column_act": 8,   "column_com": 8,     "data": "",  "check": False,  "updated": False  },
    "descripcion_cuenta":   {  "column_act": 9,   "column_com": 9,     "data": "",  "check": False,  "updated": False  },
    "fecha_registro":       {  "column_act": 10,  "column_com": 10,    "data": "",  "check": False,  "updated": False  },
    "fecha_contable":       {  "column_act": 11,  "column_com": 11,    "data": "",  "check": False,  "updated": False  },
    "cantidad":             {  "column_act": 12,  "column_com": 12,    "data": "",  "check": False,  "updated": False  },
    "unidad":               {  "column_act": 13,  "column_com": 13,    "data": "",  "check": False,  "updated": False  },
    "descripcion":          {  "column_act": 14,  "column_com": None,  "data": "",  "check": False,  "updated": False  },
    "coste":                {  "column_act": 15,  "column_com": None,  "data": "",  "check": False,  "updated": False  },
    "clase_documento":      {  "column_act": 16,  "column_com": None,  "data": "",  "check": False,  "updated": False  },
    "doc_referencia":       {  "column_act": 17,  "column_com": None,  "data": "",  "check": False,  "updated": False  },
    "texto_pedido":         {  "column_act": 18,  "column_com": 14,    "data": "",  "check": False,  "updated": False  },
    "texto_cabecera":       {  "column_act": 19,  "column_com": 15,    "data": "",  "check": False,  "updated": False  },
    "solicitante":          {  "column_act": 20,  "column_com": 16,    "data": "",  "check": True,   "updated": False  },
    "tagetik":              {  "column_act": 21,  "column_com": 17,    "data": "",  "check": True,   "updated": False  },
    "co_number":            {  "column_act": 22,  "column_com": 18,    "data": "",  "check": False,  "updated": False  },
    "ignorar":              {  "column_act": 23,  "column_com": 19,    "data": "",  "check": True,   "updated": False  },
    "observaciones":        {  "column_act": 24,  "column_com": 20,    "data": "",  "check": True,   "updated": False  }
}