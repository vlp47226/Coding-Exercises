import numpy as np

def euclid_dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def cos_dist(x,y):
    return 1 - ((x @ y) / (np.linalg.norm(x) * np.linalg.norm(y)))

def city_block_dist(x,y):
    return np.sum(np.abs(x-y))

def bray_curtis_dist(x,y):
    return np.sum(np.abs(x-y)) / np.sum(np.abs(x+y))

class KNN:
    def __init__(self, k, dist_func = "euclid_dist"):
        self.k = k
        self.dist_func  = dist_func
    
    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        y_pred = []
        for x in X:
            if self.dist_func == "euclid_dist":
                dists = [euclid_dist(x, x_train) for x_train in self.X]
            elif self.dist_func == "cos_dist":
                dists = [cos_dist(x, x_train) for x_train in self.X]
            elif self.dist_func == "city_block_dist":
                dists = [city_block_dist(x, x_train) for x_train in self.X]
            elif self.dist_func == "bray_curtis_dist":
                dists = [bray_curtis_dist(x, x_train) for x_train in self.X]
            else:
                raise ValueError("Invalid distance function")
            
            k_nearest = np.argsort(dists)[:self.k]
            k_nearest_labels = [self.y[i] for i in k_nearest]
            y_pred.append(np.bincount(k_nearest_labels).argmax())
        return y_pred

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print("Testing KNN with different distance functions")
    print("-------------------")
    print("Euclidean Distance")
    knn = KNN(3, dist_func="euclid_dist")
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("Accuracy of: ",accuracy_score(y_test, y_pred))

    print("-------------------")

    print("Cosine Distance")
    knn = KNN(3, dist_func="cos_dist")
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("Accuracy of: ",accuracy_score(y_test, y_pred))

    print("-------------------")

    print("City Block Distance")
    knn = KNN(3, dist_func="city_block_dist")
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("Accuracy of: ",accuracy_score(y_test, y_pred))

    print("-------------------")
    
    print("Bray-Curtis Distance")
    knn = KNN(3, dist_func="bray_curtis_dist")
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("Accuracy of: ",accuracy_score(y_test, y_pred))