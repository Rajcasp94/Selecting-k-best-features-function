# Selecting-k-best-features-function
This function selects k best features for classification and regression. The function takes 4 arguments: (i) training feature set, (ii) test feature set, (iii) training labels and (iv) (k) number of feature to be selected 
The train_data and train_label should be of the type dataframe.
score_method refers to the scoring criteria, for example score_method=f_classif for classification and score_method=f_regression for regression.
The function returns indices of the top k features based on their importance
This function also removes features with high multicolinearity. Features with high multicolinearity are scored the same and the duplicate scores are removed thereby removing the features with high multicolinearity.
