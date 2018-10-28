"""
k-Nearest Neighbors
See: http://andrew.gibiansky.com/blog/machine-learning/k-nearest-neighbors-simplest-machine-learning/
See: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
See: http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
"""

import uuid
import random
from A_Classes.cardinalityestimator import HLL

if __name__ == '__main__':

    h = HLL()
    n = 10000

    for _ in range(n):
        u = str(uuid.uuid4())
        for _ in range(random.randint(1, 5)):
            h.add(u)

    print('Actual: {}, Estimated: {}'.format(n, h.count()))
