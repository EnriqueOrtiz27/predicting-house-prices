## MODULE WITH ML RELATED PARAMETERS AND FUNCTIONALITIES.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


from sklearn.preprocessing import (
    OrdinalEncoder,
    StandardScaler,
    OneHotEncoder
)

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor





"------------------------------------------------------------------------------"
##############
## Pipeline ##
##############


## Numerical pipeline.
num_pipeline = Pipeline([
        ("std_scaler", StandardScaler()),
    ])

## Categorical pipeline
cat_pipeline = Pipeline([
        ("one_hot_encoder", OneHotEncoder()),
    ])





"------------------------------------------------------------------------------"
############
## Models ##
############


## Function to select model that will predict results.
def select_model(model_sel="linear_regression"):
    """
    Function to select model that will predict results.
        args:
            model_sel (string): model to be used.
                Options:
                    - linear_regression
                    - decision_tree
                    - random_forest
        returns:
            model (transformer)
    """


    ## Selecting the correct model.
    if model_sel == "linear_regression":
        model = LinearRegression()

    elif model_sel == "decision_tree":
        model = DecisionTreeRegressor()

    elif model_sel == "random_forest":
        model = RandomForestRegressor()

    return model
