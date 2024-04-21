import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Models 
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import neighbors # knn
from sklearn import cluster # k-means clustering
from sklearn.linear_model import LogisticRegression 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

from matplotlib.pylab import RandomState
from sklearn.calibration import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from numpy import array
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import LabelBinarizer
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


def getModel(draft):
    file_path = "e7_data/drafts_dataset.csv"
    df = pd.read_csv(file_path)
    draft.append("0")
    colNames  =['enemy1',"main1",'enemy2', 'main2', 'enemy3','main3', 'enemy4', 'main4', 'enemy5','main5', 'main_pre_b1', 'enemy_pre_b1','main_pre_b2', 'enemy_pre_b2', 'main_post_b','enemy_post_b' ,'is_first']
    draft_df = pd.DataFrame(np.array(draft).reshape(1,17),columns=colNames )

    y = df.iloc[:, -1]
    X = df.iloc[:, :-1]
    label_encoders = {}

    print(X.iloc[12])
    
    X_draft = draft_df

    X = pd.concat([X_draft, X], ignore_index=True)
    for column in X.select_dtypes(include=['object']).columns:
        label_encoders[column] = LabelEncoder()
        X[column] = X[column].astype(str)
        # To remove zero from the categories
        X[column] = label_encoders[column].fit_transform(X[column]) + 1
    first_row = X.iloc[0]
    X = X[1:]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(y_pred)

    accuracy = accuracy_score(y_test, y_pred)
    # print(f"Accuracy: {accuracy}")

    conf_matrix = confusion_matrix(y_test, y_pred)
    # print(f"Confusion Matrix:\n{conf_matrix}")

    X_sample = array(first_row).reshape(1, -1)
    
    # model prediction 
    win_prob = model.predict(X_sample)
    np.set_printoptions(threshold=np.inf)
    print(win_prob)
    return win_prob