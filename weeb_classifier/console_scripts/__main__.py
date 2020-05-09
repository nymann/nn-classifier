import logging

from weeb_classifier.console_scripts import argument_parser
from weeb_classifier.neural_net.neural_network import NeuralNetwork

NEURAL_NETWORK = NeuralNetwork()
LOGGER = logging.getLogger(__name__)


def train():
    if not NEURAL_NETWORK.trained:
        NEURAL_NETWORK.train(epochs=10)
    else:
        print("Neural network is already trained.")


def solve():
    args = argument_parser.default()
    images = args.images
    for img in images:
        result = NEURAL_NETWORK.solve(img)
        print(f"{img}: {result}")


if __name__ == '__main__':
    solve()
