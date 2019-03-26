The source code documentation
===

The most important parts here are the [`transforms.py`](transforms.py), in which the objects for construction of the pipeline are defined; the [`experiment.py`](experiment.py) contains a set of functions to provide an easier way to cross-validate the models results; the [`app.py`](app.py) is pretty straightfoward and contains only the wrapper to deploy the model as web service using flask.

# The transforms (`transforms.py`)

To see how it works, take a look into the [example-01.py](example-01.py). It demonstrates how to use the classes of transformers and how to wrap everything into a **Pipeline** for `sklearn`. By the way, all the transformers developed here are based on the [scikit-learn structure](https://scikit-learn.org/stable/modules/classes.html), using the base classe to construct our models. If you are familiar with sklearn, we incorporate the functionality of the `.fit()`, `.transform()` and `.fit_transform()` methods to ensure easiliy operation with advanced functionality of the `Pipeline` class or even the `set_params()` or `get_params()`.

**class DataCleaning(BaseEstimator, TransformerMixin):**
 
    > Clean data according the procedures studied in the notebook analyses-02.
    -----
    Methods
    ------------------------
    > fit(df)
    Parameters:
    df: dataframe of the dataset
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    df: dataframe of the dataset
    -----
    Returns:
    - dataframe
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.

**class RemoveFeatures(BaseEstimator, TransformerMixin):**
    
    > Remove unwanted features from the dataframes;
    -----
    Initialized parameters:
    - features: str or list cointaining the field that ought to be removed.

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - dataframe
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    - dataframe
    -----
    Returns:
    - dataframe
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.


**class FeatureScaling(BaseEstimator, TransformerMixin):**
    
    > Scale features by standardization;
    -----
    Initialized parameters:
    - type: str cointaining the scaling method. Default: 'std'.
        - 'std': StandardScaler()

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - df: a dataframe
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    - df: a dataframe
    -----
    Returns:
    - dataframe: a daframe withou NaN.
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''

**class DropNaN(TransformerMixin):**

    > Drop any row from the dataframe that contains a NaN.
    -----

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - df: a dataframe
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    - df: a dataframe
    -----
    Returns:
    - dataframe: a daframe withou NaN.
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''

**class FeatureSelection(TransformerMixin):**

    > Select the relevant features.
    -----
    Initialized parameters:
    - features: str or list of str containing the fields the should be kept

    Atrributes:
    self.features: feature names.

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - df: a dataframe.
    -----
    Returns:
    self

    > transform(df)

    Parameters:
    - df: a dataframe.
    -----
    Returns:
    - df: a dataframe.
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''

**class GetLables(TransformerMixin):**  
    
    > Get the labels following the index in the feature dataframe.
    -----
    Methods
    ------------------------
    > fit(df, df_features)
    Parameters:
    - df: dataframe containing the data
    - df_features: dataframe the outta be used as the feature set.
    -----
    Returns:
    self

    > transform(df, df_features)
    
    Parameters:
    - df: dataframe containing the data
    - df_features: dataframe the outta be used as the feature set.
    -----
    Returns:
    - df: a dataframe.
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''