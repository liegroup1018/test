import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CSV_COLUMN_NAMES = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
TEST_FETURE = CSV_COLUMN_NAMES.copy()

def load_data_csv(train_path, test_path):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
    test = pd.read_csv(train_path, names=TEST_FETURE.remove("Survived"), header=0)
    return train, test


