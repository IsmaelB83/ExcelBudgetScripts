from enum import Enum
 
class LOG(Enum):
    ERROR = 'E'
    INFO = 'I'
    WARNING = 'W'   
    
class PROCESS(Enum):
    ACTUAL = 'ACTUAL'
    COMMITMENT = 'COMMITMENT'    
    
class PATH(Enum):    
    OLD = "../data/old/"
    NEW = "../data/new/"
    FINAL = "../data/final/"

class FILENAMES(Enum):    
    ACTUAL = "REAL.xlsx"
    COMMITMENT = "COMPROMETIDO.xlsx"
    
DATA_ACTUAL = {
    "sociedad":             {  "column": 1,   "data": "",  "check": False,  "updated": False  },
    "orden":                {  "column": 2,   "data": "",  "check": True,   "updated": False  },
    "descripcion_orden":    {  "column": 3,   "data": "",  "check": False,  "updated": False  },
    "proveedor":            {  "column": 4,   "data": "",  "check": False,  "updated": False  },
    "po_number":            {  "column": 5,   "data": "",  "check": False,  "updated": False  },
    "po_position":          {  "column": 6,   "data": "",  "check": False,  "updated": False  },
    "ejercicio":            {  "column": 7,   "data": "",  "check": False,  "updated": False  },
    "periodo":              {  "column": 8,   "data": "",  "check": False,  "updated": False  },
    "descripcion_cuenta":   {  "column": 9,   "data": "",  "check": False,  "updated": False  },
    "fecha_registro":       {  "column": 10,  "data": "",  "check": False,  "updated": False  },
    "fecha_contable":       {  "column": 11,  "data": "",  "check": False,  "updated": False  },
    "cantidad":             {  "column": 12,  "data": "",  "check": False,  "updated": False  },
    "unidad":               {  "column": 13,  "data": "",  "check": False,  "updated": False  },
    "descripcion":          {  "column": 14,  "data": "",  "check": False,  "updated": False  },
    "coste":                {  "column": 15,  "data": "",  "check": False,  "updated": False  },
    "clase_documento":      {  "column": 16,  "data": "",  "check": False,  "updated": False  },
    "doc_referencia":       {  "column": 17,  "data": "",  "check": False,  "updated": False  },
    "texto_pedido":         {  "column": 18,  "data": "",  "check": False,  "updated": False  },
    "texto_cabecera":       {  "column": 19,  "data": "",  "check": False,  "updated": False  },
    "solicitante":          {  "column": 20,  "data": "",  "check": True,   "updated": False  },
    "tagetik":              {  "column": 21,  "data": "",  "check": True,   "updated": False  },
    "co_number":            {  "column": 22,  "data": "",  "check": False,  "updated": False  },
    "ignorar":              {  "column": 23,  "data": "",  "check": True,   "updated": False  },
    "observaciones":        {  "column": 24,  "data": "",  "check": True,   "updated": False  }
}

DATA_COMMITMENT = {
    "sociedad":             {  "column": 1,   "data": "",  "check": False,  "updated": False  },
    "orden":                {  "column": 2,   "data": "",  "check": True,   "updated": False  },
    "descripcion_orden":    {  "column": 3,   "data": "",  "check": False,  "updated": False  },
    "proveedor":            {  "column": 4,   "data": "",  "check": False,  "updated": False  },
    "po_number":            {  "column": 5,   "data": "",  "check": False,  "updated": False  },
    "po_position":          {  "column": 6,   "data": "",  "check": False,  "updated": False  },
    "ejercicio":            {  "column": 7,   "data": "",  "check": False,  "updated": False  },
    "periodo":              {  "column": 8,   "data": "",  "check": False,  "updated": False  },
    "descripcion_cuenta":   {  "column": 9,   "data": "",  "check": False,  "updated": False  },
    "fecha_registro":       {  "column": 10,  "data": "",  "check": False,  "updated": False  },
    "fecha_contable":       {  "column": 11,  "data": "",  "check": False,  "updated": False  },
    "cantidad":             {  "column": 12,  "data": "",  "check": False,  "updated": False  },
    "unidad":               {  "column": 13,  "data": "",  "check": False,  "updated": False  },
    "descripcion":          {  "column": 14,  "data": "",  "check": False,  "updated": False  },
    "coste":                {  "column": 15,  "data": "",  "check": False,  "updated": False  },
    "clase_documento":      {  "column": 16,  "data": "",  "check": False,  "updated": False  },
    "doc_referencia":       {  "column": 17,  "data": "",  "check": False,  "updated": False  },
    "texto_pedido":         {  "column": 18,  "data": "",  "check": False,  "updated": False  },
    "texto_cabecera":       {  "column": 19,  "data": "",  "check": False,  "updated": False  },
    "solicitante":          {  "column": 20,  "data": "",  "check": True,   "updated": False  },
    "tagetik":              {  "column": 21,  "data": "",  "check": True,   "updated": False  },
    "co_number":            {  "column": 22,  "data": "",  "check": False,  "updated": False  },
    "ignorar":              {  "column": 23,  "data": "",  "check": True,   "updated": False  },
    "observaciones":        {  "column": 24,  "data": "",  "check": True,   "updated": False  }
}