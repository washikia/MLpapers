This is relatively simple paper but I implemented it in a modularized manner, as one would do in a big project.
It was not very simple either; I had to define three custom layers while making the model.
I have left some issues that I intend to address in the future. This includes:
1- creating a custom loss function (the one used in the paper) to replace the cross entropy loss
2- initializing the parameter vectors in the RBF layer in a meaningful way
3- letting them update slowly, perhaps slower than the other weights and biases
4- consider difference transforms and generating more data by transforming the current ones and observe effect on test accuracy
5- implement the rest of the paper