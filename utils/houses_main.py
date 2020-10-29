## MAIN MODULE THAT WILL PROCESS ALL COMPLETE ML PIPELINE.
#### Arguments to execute this script:
###### model_sel (string): model to be used.
###### predict_test (boolean): wheter the script will create a '.csv' file with the predictions on the test data.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import pandas as pd
pd.set_option('display.max_columns', 50)

import numpy as np

import sys

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.preprocessing import (
    OrdinalEncoder,
    StandardScaler,
    OneHotEncoder
)

from sklearn.compose import ColumnTransformer

from sklearn.metrics import (
    mean_squared_error,
    mean_squared_log_error
)

from sklearn.model_selection import GridSearchCV


## Ancillary modules

sys.path.append("../utils")

#### Functions module
from houses_funcs import (
    json_dump_dict,
    features_dictrionary,
    clean_col_names,
    data_profiling_numeric,
    data_profiling_categ,
    display_scores,
    clean_data,
    format_predicts,
    lists_by_type_of_var
)

##@@ Parameters module
from houses_params import (
    features_dict,
    data_path_from_main,
    train_data,
    test_data
)

##@@ ML module
from houses_ml import(
    num_pipeline,
    cat_pipeline,
    select_model
)





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################


## Function to execute developed ML pipeline
def main_exec_func(model_sel="lr", predict_test=False):
    """
    Function to execute developed ML pipeline
        args:
            model_sel (string): model to be used.
            predict_test (boolean): wheter the script will create a '.csv' file with the predictions on the test data.
        returns:
            -
    """


    ".............................................................................."
    ## Importing data ##


    #### Test data
    df_test = pd.read_csv(data_path_from_main + test_data)

    #### Train data
    df_train = pd.read_csv(data_path_from_main + train_data)

    #### Name of feature that will be predicted
    for feat in features_dict:
        if features_dict[feat]["ml_label"] == True:
            predict_feature = feat



    ".............................................................................."
    ## Initial data preparation ##


    #### Clean data based on definitions dictionary
    housingc = clean_data(df_train)

    #### Adding training labels to cleaned data.
    housingc = housingc.join(df_train[predict_feature])

    #### Training labels
    housingc_labs = housingc[predict_feature]

    #### Training data
    housingc.drop(predict_feature, axis=1, inplace=True)

    #### Specifying numerical and categorical columns
    housingc_num, housingc_cat = lists_by_type_of_var(features_dict)



    ".............................................................................."
    ## Secondary data preparation ##


    ## Creating full pipeline
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, housingc_num),
        ("cat", cat_pipeline, housingc_cat),
    ])

    ## Transforming data with pipeline
    housingc_prp = full_pipeline.fit_transform(housingc)



    ".............................................................................."
    ## Selecting and training model ##


    #### Defining the model that will be used
    model = select_model(model_sel)

    #### Training the model
    model.fit(housingc_prp, housingc_labs)



    ".............................................................................."
    ## Applying cross validation ##


    ## Applying cv and displaying result scores
    cv_scores = cross_val_score(
        model,
        abs(housingc_prp),
        housingc_labs,
        scoring="neg_mean_squared_log_error",
        cv=10
    )

    display_scores(-cv_scores)



    ".............................................................................."
    ## Making predictions with the test data ##


    if predict_test == True:

        #### Initial data preparation
        housingc_test = clean_data(df_test)

        #### Secondary data preparation
        housingc_test_prp = full_pipeline.fit_transform(housingc_test)

        #### Making predictions with constructed model
        housingc_test_predicts = model.predict(housingc_test_prp)

        #### Formatting and printing predictions in '.csv' file
        housingc_test_pred_form = format_predicts(housingc_test_predicts)
        housingc_test_pred_form.to_csv("automated_predict.csv")



"------------------------------------------------------------------------------"
##################
## Execute main ##
##################


## Lines to execute main module from the command line
if __name__ == "__main__":
    main_exec_func()
