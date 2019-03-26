from transforms import *

from sklearn.pipeline import Pipeline
import pandas as pd 
import os
import sys
sys.path.append('..')

import joblib

# Global variables
DATA_FOLDER = os.path.join('..', 'data', 'raw')
USER_DATA = 'winequality_90.csv'

def read_test_data():
    return pd.read_json('test_input.json', orient='records')


# Load dataset
data = pd.read_csv(os.path.join(DATA_FOLDER, USER_DATA))
# data = read_test_data()
# Drop the label
features=data.drop(['quality'], axis=1)
# features = data

# Preprocessing:
## You can user the transformers functions in the following order:
### Data cleaning
feat_clean = DataCleaning().fit_transform(features)

### Remove unecessary features
feat_removed = RemoveFeatures().fit_transform(feat_clean)

### Feature scaling
feat_std = FeatureScaling().fit_transform(feat_removed)

### Drop NaN at the end, again.
feat_dropped = DropNaN().fit_transform(feat_std)

print(feat_dropped.shape)

## Or, by building a pipeline with sk-learn
pipeline = Pipeline([('cleaner', DataCleaning()),
                     ('remover', RemoveFeatures()),
                     ('scaler', FeatureScaling()),
                     ('droper', DropNaN())])

feat_pipe = pipeline.fit_transform(features)

# Get the labels for classification. It should ne be part of the pipeline
print('Feature set without pipeline: \n {}'.format(feat_dropped.head()))
print('Feature set with pipeline: \n {}'.format(feat_pipe.head()))

print('Shape of Feature set without pipeline: \n {}'.format(feat_dropped.shape))
print('Shape of Feature set with pipeline: \n {}'.format(feat_pipe.shape))


# Dump this transformer
joblib.dump(pipeline, os.path.join('..', 'models', 'pipeline.pkl'))


labels = GetLables().fit_transform(data)
print(labels)
print(np.unique(labels))