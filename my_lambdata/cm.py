# my_lambdata/confusion_matrix
import numpy as np
import pandas as pd
import autopep8

class c_matrix():
    # define initialize function for class
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
    # define function of function that creates the main array we will use for the rest of our class.methods()
    def confusion_matrix(self, y_true, y_pred):
        '''
        Prints Confusion Matrix of true and predicted arrays.

        Params:
        y-true: ndarray of true labels
        y-pred: ndarray of predicted labels

        Output:
        dataframe of confusion matrix with actual / predicted labels
        '''
        # defines X, the shape of true_label_array
        X = len(np.unique(y_true)) # Number of classes 
        # creates zeroes array with shape length X above
        result = np.zeros((X, X))
        # creates labels list with unique values of true_label_array
        labels = np.unique(y_true)
        # using list comprehension to create a columns_list from labels
        columns = [f'Predicted {label}' for label in labels]
        # using list comp. to create an index_list from labels
        index = [f'Actual {label}' for label in labels]
        # create the confusion matrix array by indexing into the arrays
        for i in range(len(y_true)):
            result[y_true[i]][y_pred[i]] += 1
        # change type of result to a DF
        result = pd.DataFrame((result), index=index, columns=columns)

        return result

if __name__ == "__main__":
    y_actual = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    y_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    cm = c_matrix(y_true=y_actual, y_pred=y_predicted)
    cm2 = cm.confusion_matrix(y_true=y_actual, y_pred=y_predicted)
    print(cm2)