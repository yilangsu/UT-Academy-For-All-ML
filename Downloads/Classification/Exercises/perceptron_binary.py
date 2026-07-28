from random import uniform


# Make a prediction with weights
def classify(row, weights):
    sum = 0
    for i in range(len(row)-1):
        sum += row[i]*weights[i]
    sum += weights[-1]
    if (sum >= 0):
        return 1
    return 0
 
#Estimate Perceptron weights using stochastic gradient descent
def train(train_data, n_epoch, l_rate=1):
    # read in train_data
    # for each, row
    # create a list of 60 weights
    weights = []

    for i in range(61):
        weights.append(uniform(-1,1))
    
    for i in range(n_epoch):
        correct = 0
        total = 0
        for j in range(len(train_data)):
            val = classify(train_data[j], weights)
            actual = train_data[j][-1]
            if (val == actual):
                correct += 1
            else:
                for k in range(len(weights)):
                    weights[k] = weights[k] + l_rate*((actual - val) * train_data[j][k])
            total += 1
        #print("epoch", i, "accuracy: ", correct/total)

    return weights

def cross_validate(dataset, n_folds, n_epoch):

    #create partitions, do that by creating a list of lists

    list_partitions = []
    start = 0
    end = 0

    for i in range(n_folds):
        end = start + len(dataset)/n_folds
        list_partitions.append(dataset[int(start):int(end)])
        start = end

    folds = []
    
    for fold in range(n_folds):
        test_partition = list_partitions[fold]
        train_partition = list_partitions[round((fold/2 + 1))]
        for build in range(len(list_partitions)):
            if (build != fold):
                train_partition += list_partitions[build]

        # issue, train_partition is list of 2d arrays, since it appends
        # how to create a single 2d array by splicing together mutliple 2d arrays python
        train_weights = train(train_partition, n_epoch)

        correct = 0
        total = 0
        for row in test_partition:
            predict = classify(row, train_weights)
            if (predict == row[-1]):
                correct += 1
            total += 1
        
        folds.append(correct/total*100)
    
    print(folds)
    avg = sum(folds)/n_folds

    print("mean accuracy:", avg)
        
        


        
        

            
            
            
            
            
            
    
  
        
