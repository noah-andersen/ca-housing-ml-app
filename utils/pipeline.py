import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing

def load_model(model_path:str) -> any:
    """
    Loads a pickle model.

    Parameters
    ----------
    model_path : str
        File path to the saved .pkl file

    Returns
    -------
    any
        Sklearn .pkl model
    """

    with open (model_path, 'rb') as f:
        model = pickle.load(f)

    return model

def preprocessing(features:list) -> list:
    """
    Standardizes the user inputs for inference based on the training data 
    that was provided.

    Parameters
    ----------
    features : list
        The input features from the user

    Returns
    -------
    list
        The scaled input features
    """

    # Load the california housing dataset
    cali_data = fetch_california_housing(as_frame=True)
    cali_df = cali_data.frame
    X = cali_df.iloc[:, :6]

    # Create the standard scaler
    scaler = StandardScaler()
    scaler.fit(X.values)

    # Scale the input features
    features_scaled = scaler.transform(features)

    return features_scaled

