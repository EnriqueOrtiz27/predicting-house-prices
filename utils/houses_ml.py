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

from sklearn.model_selection import GridSearchCV





"------------------------------------------------------------------------------"
###################
## ML Parameters ##
###################


## Number of cross validations
cv_rounds = 10

## Grid Search CV - Parameters grid
param_grid = [
    {
        "n_estimators": [50, 100, 150, 500],
        "max_features": [2, 4, 6, 8]
    },
    {
        "bootstrap": [False],
        "n_estimators": [3, 10],
        "max_features": [2, 3, 4]
    }
]

## Model parameters
#### Random forest regressor
max_features = 6
n_estimators = 100





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
def select_model(model_sel="lr"):
    """
    Function to select model that will predict results.
        args:
            model_sel (string): model to be used.
                Options:
                    - linear_regression (lr)
                    - decision_tree (dt)
                    - random_forest (rf)
        returns:
            model (transformer)
    """


    ## Selecting the correct model.
    if model_sel == "lr":
        model = LinearRegression()

    elif model_sel == "dt":
        model = DecisionTreeRegressor()

    elif model_sel == "rf":
        model = RandomForestRegressor(max_features=max_features, n_estimators=n_estimators)

    else:
        raise NameError("RobError: Invalid model selected.")

    print("The model that will be used is: ", model)

    return model
