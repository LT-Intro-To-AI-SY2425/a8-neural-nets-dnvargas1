from neural import *

print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")
xor_training_data = [([1, 1], [0]), ([1, 0], [1]), ([0, 1], [1]), ([0, 0], [0])]

xortest = NeuralNet(2, 2, 1)
xortest.train(xor_training_data)
print(xortest.test_with_expected(xor_training_data))



