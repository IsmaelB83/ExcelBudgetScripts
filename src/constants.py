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
    
DATA_ACTUAL = {
    "sociedad":             {  "column": 1,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "orden":                {  "column": 2,   "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "descripcion_orden":    {  "column": 3,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "proveedor":            {  "column": 4,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "po_number":            {  "column": 5,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "po_position":          {  "column": 6,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "ejercicio":            {  "column": 7,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "periodo":              {  "column": 8,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "descripcion_cuenta":   {  "column": 9,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "fecha_registro":       {  "column": 10,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "fecha_contable":       {  "column": 11,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "cantidad":             {  "column": 12,  "data": "",  "check": False,  "updated": False,  "type": "float"   },
    "unidad":               {  "column": 13,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "descripcion":          {  "column": 14,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "coste":                {  "column": 15,  "data": "",  "check": False,  "updated": False,  "type": "float"   },
    "clase_documento":      {  "column": 16,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "doc_referencia":       {  "column": 17,  "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "texto_pedido":         {  "column": 18,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "texto_cabecera":       {  "column": 19,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "solicitante":          {  "column": 20,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "tagetik":              {  "column": 21,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "co_number":            {  "column": 22,  "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "ignorar":              {  "column": 23,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "observaciones":        {  "column": 24,  "data": "",  "check": True,   "updated": False,  "type": "string"  }
}

DATA_COMMITMENT = {
    "sociedad":             {  "column": 1,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "orden":                {  "column": 2,   "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "descripcion_orden":    {  "column": 3,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "proveedor":            {  "column": 4,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "po_number":            {  "column": 5,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "po_position":          {  "column": 6,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "ejercicio":            {  "column": 7,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "periodo":              {  "column": 8,   "data": "",  "check": False,  "updated": False,  "type": "int"     },
    "descripcion_cuenta":   {  "column": 9,   "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "fecha_registro":       {  "column": 10,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "fecha_contable":       {  "column": 11,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "cantidad":             {  "column": 12,  "data": "",  "check": False,  "updated": False,  "type": "float"   },
    "unidad":               {  "column": 13,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "texto_pedido":         {  "column": 14,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "comprometido" :        {  "column": 15,  "data": "",  "check": False,  "updated": False,  "type": "float"   },
    "solicitante":          {  "column": 16,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "tagetik":              {  "column": 17,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "tipo":                 {  "column": 18,  "data": "",  "check": False,  "updated": False,  "type": "string"  },
    "ignorar":              {  "column": 19,  "data": "",  "check": True,   "updated": False,  "type": "string"  },
    "observaciones":        {  "column": 20,  "data": "",  "check": True,   "updated": False,  "type": "string"  }
}

LOG_HEADER = ['PROCESS', 'TYPE', 'ROW', 'PO_NUMBER', 'PO_POSITION', 'AMOUNT', 'MESSAGE']
LOG_ERRORS = []
LOG_WARNING = []