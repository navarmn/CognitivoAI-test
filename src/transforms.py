import numpy as np 
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler


FEATURES_TO_DROP = ['type']


class DataCleaning(BaseEstimator, TransformerMixin):
    ''' 
    Clean data according the procedures studied in the notebook analyses-02. In short: 
    (i) Drops Nan; (ii) split data in categorical and numerical features; 
    (iii) 1-hot-enconding of categorical features; (iv) Get a unique categorical features
    of an user in a period of 16 weeks; (v)  Get a unique numerical features of an user 
    in a period of 16 weeks; (vi) Average the numerical features in a period of 16-week;
    (vii) contat both feature set;
    -----
    Methods
    ------------------------
    > fit(df)
    Parameters:
    df: dataframe of the dataset, in which the user name must be set as index; 
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    - df: dataframe of the dataset, in which the user name must be set as index; 
    -----
    Returns:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''
    
    def fit(self, df):
        return self

    def transform(self, df):
        # Remove NaN:
        df_clean = df.dropna(how='any', inplace=False)

        # Map the wine type
        df_clean['type'] = df_clean['type'].map({'Red': 1, 'White': 2})

        # Transform str to float from the alcohol table
        df_clean['alcohol'] = df_clean['alcohol'].map(self._str_to_float)

        # Drop NaN
        data_raw_dropped = df_clean.dropna()

        # TODO check if dataframe haw only one row

        return data_raw_dropped

    def _str_to_float(self, s, len_max=5):
        # check string lenght
        if len(s) > len_max:
            return np.NaN
        return float(s)

class RemoveFeatures(BaseEstimator, TransformerMixin):
    ''' 
    Remove unwanted features from the dataframes;
    -----
    Initialized parameters:
    - features: str or list cointaining the field that ought to be removed. Default: 'week'.

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----
    Returns:
    self
    
    > transform(df)

    Parameters:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----
    Returns:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''

    def __init__(self, features='type'):
        self.features = features

    def fit(self, df):
        return self

    def transform(self, df):
        return df.drop(columns=self.features)

class FeatureScaling(BaseEstimator, TransformerMixin):
    ''' 
    Scale features by standardization;
    -----
    Initialized parameters:
    - type: str cointaining the scaling method. Default: 'std'.
        - 'std': StandardScaler()

    Methods
    ------------------------
    > fit(df)
    Parameters:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----
    Returns:
    self

    Atrributes:
    self._scaler: saved object that sould be used along with the trained model.
    
    > transform(df)

    Parameters:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----
    Returns:
    - dict: a dictonary variable of dataframes: {'numerical': DataFrame, 'categorical': DataFrame}
    -----------------
    OBS.: fit_transform method is available, inherited from TransformerMixin class.
    '''

    def __init__(self, type='std'):
        self.type = type

    def fit(self, df):
        self._scaler = StandardScaler().fit(df)
        
        return self

    def transform(self, df):
        if self.type == 'std':
            df_std = self._scaler.transform(df)
            df_std = pd.DataFrame(data=df_std, 
                                  columns=df.columns, 
                                  index=df.index)
        
        return df_std


class FeatureSelection(TransformerMixin):
    ''' 
    Select the relevant features.
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
    def __init__(self, features=None):
        self.features = features

    def fit(self, df):
        return self

    def transform(self, df):
        return df[self.features]


class DropNaN(TransformerMixin):
    ''' 
    Drop any row from the dataframe that contains a NaN.
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

    def fit(self, df):
        return self

    def transform(self, df):
        return df.dropna()