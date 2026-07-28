import random
from knn import *
from csv import reader
import sys


# Load the dataset from csv file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


if __name__ == "__main__":
    # Example dataset for testing
    dataset = [
        [1, 2, 0], [2, 3, 0], [3, 4, 1], [5, 6, 1], [8, 8, 1],
        [2, 2, 0], [4, 4, 1], [6, 6, 1], [7, 7, 1], [5, 5, 0]
    ]

    ########################
    # Test get_distances
    ########################
    print("\nTest get_distances")
    point = [1, 2]
    data_points = [[2, 3], [3, 4], [4, 5]]
    distances = get_distances(point, data_points)
    print("Distances:", distances, "\n")

    ########################
    # Test run_knn
    ########################
    print("\nTest run_knn")
    train_set = [[1, 2, 0], [2, 3, 0], [3, 4, 1], [5, 6, 1]]
    test_set = [[2, 2, 0], [4, 4, 1]]
    k = 3
    y_pred, y_test = run_knn(train_set, test_set, k)
    print("Predicted classes:", y_pred)
    print("True classes:", y_test, "\n")


    ########################
    # Run KNN on iris dataset
    ########################
    print("\nRun KNN on Iris dataset")
    filename = 'iris.csv'
    dataset = load_csv(filename)
    for i in range(len(dataset[0])-1):
        str_column_to_float(dataset, i)

    # split dataset into train and test
    random.seed(13)
    random.shuffle(dataset)
    train_set = dataset[:101]
    test_set = dataset[101:]

    # run knn
    k = 5
    preds, acts = run_knn(train_set, test_set, k)
    accuracy = compute_accuracy(preds, acts)
    print("Accuracy:", accuracy, "\n")