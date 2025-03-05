import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import os
import random
import gc
import time
from sklearn.compose import make_column_transformer

def get_outliers(df, col, tipo="leve"):
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  if tipo == "leve":
    k = 1.5
  else:
    k = 3
  return df[(df[col] >= Q3 + k*IQR) | (df[col] <= Q1 - k*IQR)]

seed_value = 42
os.environ['PYTHONHASHSEED'] = str(seed_value)
random.seed(seed_value)
np.random.seed(seed_value)

source_path = "./dataset/"
dest_path = "./model/"

df_asteroids = pd.read_csv(source_path+"asteroid_dataset.csv", engine='c', low_memory=False, index_col="id")
df_asteroids = df_asteroids[["pha", "moid", "n", "e", "H", "diametro", "ma", "tp", "rms", "i", "spkid", "om", "epoch", "w"]]

df_asteroids = df_asteroids[~df_asteroids["pha"].isna()]

cantidad = df_asteroids.isna().sum()
cantidad = cantidad[cantidad.values > 0]
porcentaje = cantidad * 100 / df_asteroids.shape[0]
df_nulls = pd.DataFrame(data={"Number of missing values":cantidad, "Percentage of missing values":porcentaje}, index=cantidad.index).sort_values(by=["Percentage of missing values"], ascending=False)
columns_nan = df_nulls[df_nulls["Percentage of missing values"] > 3].index
df_asteroids.drop(columns_nan, axis=1, inplace=True)

H_outliers = get_outliers(df_asteroids, "H", "extremos")
df_asteroids.drop(H_outliers.index, axis=0, inplace=True)

moid_outliers = get_outliers(df_asteroids, "moid", "extremos")
df_asteroids.drop(moid_outliers.index, axis=0, inplace=True)

albedo = 0.0615
df_asteroids["diametro"] = (1329/albedo)*np.power(10, -0.4*df_asteroids["H"])
df_asteroids[["diametro"]]

X = df_asteroids_.drop(["pha"], axis=1)
y = df_asteroids_["pha"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, stratify=y, random_state=seed_value)
X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size=0.25, stratify=y_val, random_state=seed_value)

numerical_cols = X_train.select_dtypes(["uint8", "float64"]).columns
categorical_cols = X_train.select_dtypes(["object"]).columns

le = LabelEncoder()
y_train = le.fit_transform(y_train).astype("uint8")
y_val = le.transform(y_val).astype("uint8")
y_test = le.transform(y_test).astype("uint8")

column_transformer = make_column_transformer(
    # Numerical columns
    (
        StandardScaler().set_output(transform='pandas'),
        numerical_cols
    ),
    # Categorical columns
    (
        OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform='pandas'),
        categorical_cols
    ),
    remainder='passthrough',
    verbose_feature_names_out=False
).set_output(transform='pandas')

X_train = column_transformer.fit_transform(X_train)
X_val = column_transformer.transform(X_val)
X_test = column_transformer.transform(X_test)

oversample = SMOTE(sampling_strategy=0.25, random_state=seed_value, k_neighbors=5)
X_train, y_train = oversample.fit_resample(X_train, y_train)

undersample = RandomUnderSampler(random_state=42)
X_train, y_train = undersample.fit_resample(X_train, y_train)

sfs_forward = SequentialFeatureSelector(estimator=LogisticRegression(),
                                        n_features_to_select=12,
                                        direction="forward",
                                        scoring='roc_auc',
                                        cv=5).set_output(transform='pandas')

sfs_forward.fit(X_train, y_train)

X_train = sfs_forward.transform(X_train)
X_val = sfs_forward.transform(X_val)
X_test = sfs_forward.transform(X_test)

X_train_min, _, y_train_min, _ = train_test_split(X_train, y_train, test_size=0.55, stratify=y_train, random_state=seed_value)

rf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=seed_value, n_jobs=-1, verbose=2).fit(X_train_min, y_train_min)

with open(dest_path+'HAP_model.bin', 'wb') as f_out:
    cloudpickle.dump((column_transformer, le, sfs_forward, rf), f_out)