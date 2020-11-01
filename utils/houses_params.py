## MODULE WITH PYTHON PARAMETERS RELEVANT FOR THE PROBLEM





"------------------------------------------------------------------------------"
###############################
## Main execution parameters ##
###############################


## Path from main execution file to dataset.
data_path_from_main = "../data/"

## Name of files with projects data.
train_data = "casas_entrena.csv"
test_data = "casas_prueba.csv"





"------------------------------------------------------------------------------"
############################
## Definitions dictionary ##
############################


features_dict = {
    "MS SubClass": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "category",
        "notes": "Después de una exploración, se observó que no hay una relación clara entre las 16 categorías de la columna y el precio de venta.",
        "ml_label": False
    },
    "MS Zoning": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False
    },
    "Lot Frontage": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.21,
        "len_uniques": 113,
        "data_obj_type": "float64",
        "notes": "Se realizó una gráfica scatter de esta variable y el precio de venta. No se observó una correlación relevante.",
        "ml_label": False
    },
    "Lot Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 929,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Street": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Alley": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.94,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "Tiene demasiados valores vacíos.",
        "ml_label": False
    },
    "Lot Shape": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False
    },
    "Land Contour": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False
    },
    "Utilities": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Lot Config": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False
    },
    "Land Slope": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también.",
        "ml_label": False
    },
    "Neighborhood": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 27,
        "data_obj_type": "object",
        "notes": "El autor explica que esta variable sería relevante si tuviéramos un mapa.",
        "ml_label": False
    },
    "Condition 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Condition 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Bldg Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "House Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Overall Qual": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 10,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "Overall Cond": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Year Built": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 108,
        "data_obj_type": "int64",
        "notes": "Se observó una corrlación importante entre el precio y esta variable en el GEDA.",
        "ml_label": False
    },
    "Year Remod/Add": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 61,
        "data_obj_type": "int64",
        "notes": "No se observó una relación de esta variable y el precio de venta.",
        "ml_label": False
    },
    "Roof Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Roof Matl": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Exterior 1st": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 14,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Exterior 2nd": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Mas Vnr Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.01,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Mas Vnr Area": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.01,
        "len_uniques": 279,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False
    },
    "Exter Qual": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False
    },
    "Exter Cond": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "category",
        "notes": "-",
        "ml_label": False
    },
    "Foundation": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Bsmt Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Bsmt Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Bsmt Exposure": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "BsmtFin Type 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "BsmtFin SF 1": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 609,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "BsmtFin Type 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "BsmtFin SF 2": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 133,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Bsmt Unf SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 680,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Total Bsmt SF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 646,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "Heating": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Heating QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Central Air": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Electrical": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "1st Flr SF": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 675,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "2nd Flr SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 370,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Low Qual Fin SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Gr Liv Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 782,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "Bsmt Full Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Bsmt Half Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Full Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Half Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Bedroom AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Kitchen AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Kitchen Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "TotRms AbvGrd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 11,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Functional": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Fireplaces": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Fireplace Qu": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.47,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Garage Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Garage Yr Blt": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.04,
        "len_uniques": 96,
        "data_obj_type": "float64",
        "notes": "-",
        "ml_label": False
    },
    "Garage Finish": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Garage Cars": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "Garage Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 399,
        "data_obj_type": "int64",
        "notes": "La matriz de correlación muestra claramente que hay una muy buena relación de esta variable y el precio de venta. (> 0.6)",
        "ml_label": False
    },
    "Garage Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Garage Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Paved Drive": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Wood Deck SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 248,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Open Porch SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 188,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Enclosed Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 118,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "3Ssn Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Screen Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 75,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Pool Area": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Pool QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 1.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Fence": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.8,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Misc Feature": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.95,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Misc Val": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 25,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Mo Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 12,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Yr Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "Sale Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "Sale Condition": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 1,
        "data_obj_type": "object",
        "notes": "-",
        "ml_label": False
    },
    "id": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "int64",
        "notes": "-",
        "ml_label": False
    },
    "SalePrice": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "float64",
        "notes": "This is the variable we are trying to predict.",
        "ml_label": True
    },
}
