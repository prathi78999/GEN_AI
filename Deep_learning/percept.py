import numpy as np
from sklearn.linear_model import Perceptron

X=np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])
#y=np.array([0,1,1,0])#linear output
y=np.array([0,0,0,1])#non-linear output
model =Perceptron(max_iter=1000)
model.fit(X,y)
pred_y=model.predict(X)
print("Actual",y)
print("predicted",pred_y)
accuracy=model.score(X,y)
print("Accuracy:",accuracy)