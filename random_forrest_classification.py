from sklearn.ensemble import RandomForrestClassifier

forest_cls = RandomForrestClassifier( random_state=42 )
y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3, method="predict_proba")
y_proba_forest[:2]
