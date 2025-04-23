import numpy as np
import csv
import random
import pandas as pd

# def load_data(file):
#     X_raw = []
#     y = []

#     with open(file, 'rt', encoding='utf8') as f:
#         dict_reader = csv.DictReader(f)

#         for observation in dict_reader:
#             y.append(observation['gross_profit'])
#             observation.pop('gross_profit', None)

#             for key in ['store', 'longitude', 'latitude', 'city', 'county', 'liter', 'bottles', 'pop_city', 'fips', 'pop_county']:
#                 observation.pop(key, None)

#             X_raw.append(observation)

#     return X_raw, y

def convert_X_raw_to_array(X_raw):
    feature_keys = list(X_raw[0].keys())
    X = []

    for obs in X_raw:
        row = []

        for key in feature_keys:
            value = obs[key]
            row.append(value)

        X.append(row)

    return np.array(X)

def train_valid_test_split(X, y):
    random.seed(32)

    X_train = []
    X_valid = []
    X_test = []
    y_train = []
    y_valid = []
    y_test = []
   
    for index in range(len(X)):
        z = random.uniform(0, 1)

        if z < 0.7:
          X_train.append(X[index])
          y_train.append(y[index])

        elif z < 0.85:
            X_valid.append(X[index])
            y_valid.append(y[index])
            
        else:
            X_test.append(X[index])
            y_test.append(y[index])
                
    X_train = np.array(X_train, dtype=float)
    y_train = np.array(y_train, dtype=float)
    X_valid = np.array(X_valid, dtype=float)
    y_valid = np.array(y_valid, dtype=float)
    X_test = np.array(X_test, dtype=float)
    y_test = np.array(y_test, dtype=float)
    

    return X_train, X_valid, X_test, y_train, y_valid, y_test

def add_ones(X):
  beta_zero_column = np.ones((X.shape[0], 1))
  X_ones = np.hstack((beta_zero_column, X))

  return X_ones

def ols(X, y):
    X = X.astype(float)
    y = y.astype(float)

    # delete zero rows
    X = X[~np.all(X == 0, axis=1)]

    # delete zero columns
    X = X[:, ~np.all(X == 0, axis=0)]

    # ols
    Xt = X.transpose()
    Xt_X = np.dot(Xt, X)
    Xt_X_inv = np.linalg.pinv(Xt_X)
    Xt_X_inv_Xt = np.dot(Xt_X_inv, Xt)
    beta_hat = np.dot(Xt_X_inv_Xt, y)

    return beta_hat

def recenter(X, y):
    X = X - np.mean(X, 0)
    y = y - np.mean(y)

    return X, y

def ridge(X, y, fLambda):
    X = np.array(X)
    y = np.array(y)
    
    # delete zero rows
    # X = X[~np.all(X == 0, axis=1)]
    
    # # delete zero columns
    # X = X[:, ~np.all(X == 0, axis=0)]
    
    # ridge
    Xt = X.transpose()
    Xt_X = np.dot(Xt, X)
    lambda_I = fLambda * np.identity(X.shape[1])
    Xt_X_lambda_I_inv = np.linalg.inv(Xt_X + lambda_I)
    Xt_X_lambda_I_inv_Xt = np.dot(Xt_X_lambda_I_inv, Xt)
    beta_hat = np.dot(Xt_X_lambda_I_inv_Xt, y)

    return beta_hat

# new function to get the cols removed, got code from ols
def get_removed_col_indices(X):
    X = np.array(X)
    original_cols = np.arange(X.shape[1])
    non_zero_cols = ~np.all(X  == 0, axis=0)
    removed_cols = original_cols[~non_zero_cols]
    return removed_cols, original_cols

# new function to remove features
def remove_features(feat_list, removed_cols):
  return [feature for i, feature in enumerate(feat_list) if i not in removed_cols]

# prediction
def predict(X, beta):
  X = np.array(X)
  # X = X[:, ~np.all(X==0, axis=0)]
  beta = np.array(beta)
  y_hat = np.dot(X, beta)

  return y_hat

# calculate mse
def mean_squared_error(y_hat, y):
  mse = np.mean((y.flatten() - y_hat) ** 2)

  return mse