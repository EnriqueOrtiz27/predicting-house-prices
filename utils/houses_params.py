## MODULE WITH PYTHON PARAMETERS RELEVANT FOR THE PROBLEM





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
        "notes": "Después de una exploración, se observó que no hay una relación clara entre las 16 categorías de la columna y el precio de venta."
    },
    "MS Zoning": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Lot Frontage": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.21,
        "len_uniques": 113,
        "data_obj_type": "float64",
        "notes": "Se realizó una gráfica scatter de esta variable y el precio de venta. No se observó una correlación relevante."
    },
    "Lot Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 929,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Street": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Alley": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.94,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Lot Shape": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también."
    },
    "Land Contour": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también."
    },
    "Utilities": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Lot Config": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también."
    },
    "Land Slope": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "La descripción de los datos indica que no es una variable relevante. Se realizó GEDA también."
    },
    "Neighborhood": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 27,
        "data_obj_type": "object",
        "notes": "El autor explica que esta variable sería relevante si tuviéramos un mapa."
    },
    "Condition 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Condition 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Bldg Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "House Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 8,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Overall Qual": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 10,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Overall Cond": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 9,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Year Built": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 108,
        "data_obj_type": "int64",
        "notes": "Se observó una corrlación importante entre el precio y esta variable en el GEDA."
    },
    "Year Remod/Add": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 61,
        "data_obj_type": "int64",
        "notes": "No se observó una relación de esta variable y el precio de venta."
    },
    "Roof Style": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Roof Matl": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Exterior 1st": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 14,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Exterior 2nd": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 15,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Mas Vnr Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.01,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Mas Vnr Area": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.01,
        "len_uniques": 279,
        "data_obj_type": "float64",
        "notes": "-"
    },
    "Exter Qual": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Exter Cond": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Foundation": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Bsmt Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Bsmt Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Bsmt Exposure": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "BsmtFin Type 1": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-"
    },
    "BsmtFin SF 1": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 609,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "BsmtFin Type 2": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.03,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-"
    },
    "BsmtFin SF 2": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 133,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Bsmt Unf SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 680,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Total Bsmt SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 646,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Heating": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Heating QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Central Air": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 2,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Electrical": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "1st Flr SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 675,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "2nd Flr SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 370,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Low Qual Fin SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Gr Liv Area": {
        "relevant": True,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 782,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Bsmt Full Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Bsmt Half Bath": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Full Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Half Bath": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Bedroom AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Kitchen AbvGr": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Kitchen Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "TotRms AbvGrd": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 11,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Functional": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Fireplaces": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 4,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Fireplace Qu": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.47,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Garage Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Garage Yr Blt": {
        "relevant": False,
        "data_default_type": "float64",
        "null_perc": 0.04,
        "len_uniques": 96,
        "data_obj_type": "float64",
        "notes": "-"
    },
    "Garage Finish": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Garage Cars": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Garage Area": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 399,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Garage Qual": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Garage Cond": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.04,
        "len_uniques": 6,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Paved Drive": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 3,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Wood Deck SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 248,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Open Porch SF": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 188,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Enclosed Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 118,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "3Ssn Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 17,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Screen Porch": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 75,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Pool Area": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 6,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Pool QC": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 1.0,
        "len_uniques": 4,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Fence": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.8,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Misc Feature": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.95,
        "len_uniques": 5,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Misc Val": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 25,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Mo Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 12,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Yr Sold": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 5,
        "data_obj_type": "int64",
        "notes": "-"
    },
    "Sale Type": {
        "relevant": False,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 7,
        "data_obj_type": "object",
        "notes": "-"
    },
    "Sale Condition": {
        "relevant": True,
        "data_default_type": "object",
        "null_perc": 0.0,
        "len_uniques": 1,
        "data_obj_type": "object",
        "notes": "-"
    },
    "id": {
        "relevant": False,
        "data_default_type": "int64",
        "null_perc": 0.0,
        "len_uniques": 1203,
        "data_obj_type": "int64",
        "notes": "-"
    }
}
