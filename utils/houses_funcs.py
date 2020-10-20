## MODULE WITH PYTHON FUNCTIONS RELEVANT FOR THE PROBLEM





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import json

import numpy as np


## Ancillary modules

from houses_params import *





"------------------------------------------------------------------------------"
###############################
## General purpose functions ##
###############################


## Pretty print a dictionary and preserving special characters
def json_dump_dict(dictionary):
    """
    Pretty print a dictionary and preserving special characters
        args:
            dictionary (dictionary): dict that will be pretty printed
        returns:
            -
    """

    print(json.dumps(dictionary, indent=4, ensure_ascii=False).encode("utf8").decode())

    return



## Creating features dictionary
def features_dictrionary(data):
    """
    Creating features dictionary
        args:
            data (dataframe): table with all data that will populate the dictionary.
        returns:
            -
    """

    def_dict = {}

    for col in data.columns:
        def_dict[col] = {
            "relevant": False,
            "data_type": str(data[col].dtype),
            "null_perc": round(data[col].isnull().sum()/data.shape[0], 2),
            "len_uniques": len(data[col].unique())
        }

    json_dump_dict(def_dict)

    return



## Transform columns' names to standard format
def clean_col_names(dataframe):
    """
    Transform columns' names to standard format (lowercase, no spaces, no points)
        args:
            dataframe (dataframe): df whose columns will be formatted.
        returns:
            dataframe (dataframe): df with columns cleaned.
    """

    ## Definition of cleaning funcitons that will be applied to the columns' names
    fun1 = lambda x: x.lower() ## convert to lowercase
    fun2 = lambda x: re.sub("( |¡|!|¿|\?|\.|,|;|:)", "_", x) ## eliminate spaces and punctuation signs for underscore
    fun3 = lambda x: unicodedata.normalize("NFD", x).encode("ascii", "ignore").decode("utf-8") ## substitute accents for normal letters
    funcs = [fun1, fun2, fun3]

    ## Applying the defined functions to the columns' names
    for fun in funcs:
        dataframe.columns = [fun(col) for col in dataframe.columns]

    return dataframe



## Data profiling for numeric variables
def data_profiling_numeric(data, num_vars):
    """
    Data profiling for numeric variables
        Args:
            data(dataframe): dataframe that will be analyzed.
        num_vars (list): list of variables' names in the dataframe that will be analyzed.
        Retruns:
            Dataframe with the data profiling (type, number of observations, mean, sd, quartiles, max, min, unique observations, top 5 repeated observations, number of null variables)
            of the choosen numeric variables.
    """

    ## Copy of initial dataframe to select only numerical columns
    dfx = data.loc[:, num_vars]


    ## Pipeline to create dataframe with general data description
    print("*********************************")
    print("** General description of data **")
    print("*********************************")

    #### List where the resulting dataframes will be stored for further concatenation
    res_dfs = []

    #### Type of numeric variables
    dfx_dtype = dfx.dtypes.to_frame().T
    dfx_dtype.index = ["dtype"]
    res_dfs.append(dfx_dtype)

    #### Counting unique variables
    dfx_uniqvars = dfx.nunique().to_frame().T
    dfx_uniqvars.index = ["count_unique"]
    res_dfs.append(dfx_uniqvars)

    #### Counting missing values
    dfx_missing = dfx.isnull().sum().to_frame().T
    dfx_missing.index = ["missing_v"]
    res_dfs.append(dfx_missing)

    #### General description of the data and addition of min values
    dfx_desc = dfx.describe()
    dfx_desc.loc["min", :] = dfx.min(axis=0)
    res_dfs.append(dfx_desc)

    #### Concatenating resulting dataframes into one final result
    print(display(pd.concat(res_dfs, axis=0)))
    print("-"*75)
    print("-"*75)
    print("\n\n".format())


    ## Pipeline to obtain top repeated variables per column
    print("****************************")
    print("** Top repeated variables **")
    print("****************************")

    #### Initial variables
    tops = 5 #### Number of tops that will be selected
    i = 0 #### Counter to start joining dataframes

    #### Loop through all variables that will be processed
    for col_sel in dfx:

        #### Creating dataframe with top entries and count
        dfxx = dfx[col_sel].value_counts().iloc[:tops].to_frame()
        dfxx.reset_index(drop=False, inplace=True)
        dfxx["part"] = round(dfxx[col_sel]/dfx[col_sel].count()*100, 2)
        dfxx.columns = pd.MultiIndex.from_tuples([(col_sel, tag) for tag in ["value", "count", "part_notnull"]])

        #### Joining all the variables in one final dataframe
        if i == 0:
            df_tops = dfxx
            i += 1
        else:
            df_tops = df_tops.join(dfxx)

    ## Fill empty spaces of resulting dataframe and renaming index entries
    df_tops.fillna("-", inplace=True)
    df_tops.index = ["top_" + str(i) for i in range(1, df_tops.shape[0] + 1)]
    print(display(df_tops))
    print("-"*75)
    print("-"*75)
    print()
    return



## Create the data profiling of categorical variables.
def data_profiling_categ(data, cat_vars):
    """
    Create the data profiling of categorical variables.
        args:
            data (Data Frame): data set into Dataframe.
            cat_vars (list): list with categorical variables names.
        returns:
           display(): display the Dataframes with info.
    """

    for val in cat_vars:
        print("*********************************")
        print("Variable Categorica {}".format(val))
        print("*********************************")

        catego  = data[val].value_counts()
        totalOb = len(data[val])
        can_Cat = len(catego)
        moda    = data[val].mode().values[0]
        valFal  = data[val].isnull().sum()
        top1    = [catego[0:1].index[0],catego[0:1].values[0]] if can_Cat >= 1 else 0
        top2    = [catego[1:2].index[0],catego[1:2].values[0]] if can_Cat >= 2 else 0
        top3    = [catego[2:3].index[0],catego[2:3].values[0]] if can_Cat >= 3 else 0

        elemVarCat = {
            "Info":val,
            "Num_Registros":[totalOb],
            "Num_de_categorias":[can_Cat],
            "Moda":[moda],
            "Valores_faltantes":[valFal],
            "Top1":[top1],
            "Top2":[top2],
            "Top3":[top3]
            }

        #primerdataframe
        df_catVar = pd.DataFrame(elemVarCat).set_index("Info").T

        #mostrar primer data frame
        print(display(df_catVar))

        print("Valores de las categorias y sus proporciones")
        #segundodataframe donde se muestra los valores de las categorias su cantidad y su proporción.
        pro = proporcion(catego,totalOb)
        dfProp = pd.DataFrame(pro,columns=['Categoría', 'Observaciones', 'proporción']).set_index("Categoría")
        #mostrar primer data frame
        print(display(dfProp))
        print("\n\n".format())
    return





"------------------------------------------------------------------------------"
################################
## Data preparation functions ##
################################


## Cleaning and preparing dataset
def clean_data(data):
    """
    Cleaning and preparing dataset
        args:
            data (dataframe): raw data for the model.
        returns:
            data_clean (dataframe): processed and cleaned data for the model.
    """


    ## Copy of raw data
    data_clean = data.copy()


    ## Eliminating houses with "Gr Liv Area" larger than 4,000
    data_clean = data_clean[data_clean["Gr Liv Area"] < 4_000]


    ## Maintain "Sale Condition" with tag "Normal" only
    data_clean = data_clean[data_clean["Sale Condition"] == "Normal"]


    ## Simplifying tags based on rule
    data_clean["MS Zoning"] = np.where(data_clean["MS Zoning"] == "RL", 1, 0) #solo ahí se ven diferencias


    ## Selecting only the columns marked as relevant == True
    rc = [key for key in features_dict if features_dict[key]["relevant"] == True]
    data_clean = data_clean.loc[:, rc]


    ## Convert columns to objective data type
    for col in data_clean:
        data_clean[col] = data_clean[col].astype(features_dict[col]["data_obj_type"])


    return data_clean
