from network_backend.Module import ModuleI
import ast


class SequentialNetwork(ModuleI):
    def __init__(self, layers):
        super(SequentialNetwork, self).__init__()
        for layer in layers:
            assert isinstance(layer, ModuleI)
        self.layers = layers

    def feed_forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def backprop(self, delta_out):
        delta = delta_out
        for layer in reversed(self.layers):
            delta = layer.backprop(delta)
        return delta

    def noFeatures(self):
        return sum([len(layer) for layer in self.layers])

    def getGradients(self):
        return [grad for layer in self.layers for grad in layer.getGradients()]

    def update(self, delta):
        for layer in self.layers:
            layer.update(delta[:len(layer)])
            delta = delta[len(layer):]

    def toString(self):
        string = "["
        for layer in self.layers:
            string += str(layer) + ","
        string = string[:-1] + "]"
        return string

    def fromString(self, string):
        list = ast.literal_eval(string)
        self.layers = [layer.fromString(str(l)) for l, layer in self.layers]

class FullyConnectedNet(ModuleI):
    def __init__(self, ):
        super(FullyConnectedNet, self).__init__()