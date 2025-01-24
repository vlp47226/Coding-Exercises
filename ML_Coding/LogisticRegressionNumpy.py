import numpy as np
import time
def sigmoid(x): #Sigmoid function
    return 1 / (1 + np.exp(-x))

def loss_function(theta, X, y): #Loss function, includes using np.dot instead of @
    m = len(y)
    h = sigmoid(X @ theta)
    return -1/m * (y.T @ np.log(h) + (1 - y).T @ np.log(1 - h)) #function for Logistic Regression
    #Or return -1/m * (np.dot(y.T, np.log(h)) + np.dot((1 - y).T, np.log(1 - h)))

def gradient(theta, X, y): #Calculating the gradient
    m = len(y)
    h = sigmoid(X @ theta)
    grad = 1/m * X.T @ (h - y)
    return grad

def gradient_descent(theta, X, y, lr, iters): #Gradient Descent Optimization based on number of iterations and learning rate
    loss_history = np.zeros(iters)
    print("Training the Logstic Regression Model...")
    for i in range(iters):
        grad = gradient(theta, X, y) #Calculate the gradient
        theta -= lr * grad #Update theta based on the gradient
        loss = loss_function(theta, X, y)
        loss_history[i] = loss #Calculate the loss function based on the updated theta and add it to the loss history
        print("Iteration: {}, Loss: {}".format(i, round(loss[0][0], 4)))
        time.sleep(0.25)

    return theta, loss_history

def predict(theta, X): #Predicting the output based on the sigmoid function
    return np.round(sigmoid(X @ theta))

if __name__ == '__main__':
    np.random.seed(0)
    X = np.random.randn(1000, 2)
    y = np.random.randint(0, 2, (1000, 1))

    X = np.hstack((np.ones((X.shape[0], 1)), X)) #Adding the bias term

    theta = np.zeros((X.shape[1], 1)) #Initial theta

    theta, loss_history = gradient_descent(theta, X, y, lr=0.1, iters=50)

    predictions = predict(theta, X)

    print("Training Accuracy: {}%".format(100 - np.mean(np.abs(predictions - y)) * 100)) #Printing the training accuracy
    print("Final loss: {}".format(loss_history[-1])) #Printing the final loss
    