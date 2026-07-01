from sklearn.base import BaseEstimator, TransformerMixin

class PassengerTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.age_median = None

    def fit(self, X, y=None):
        self.age_median = X["Age"].median()
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X["Age"] = X["Age"].fillna(self.age_median)
        X["Sex"] = X["Sex"].map({"male": 0, "female": 1})
        X["Embarked"] = X["Embarked"].fillna("S").map({
            "S": 0,
            "C": 1,
            "Q": 2
        })
        return X
        