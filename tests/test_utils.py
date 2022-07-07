
from miceforest.utils import (
    stratified_subset
)
import numpy as np

def test_subset():

    strat_std_closer = []
    strat_mean_closer = []
    for i in range(1000):
        y = np.random.normal(size=1000)
        size = 100
        y_strat_sub = y[
            stratified_subset(
                y,
                size,
                groups=10,
                cat=False,
                seed=i
            )
        ]
        y_rand_sub = np.random.choice(y, size, replace=False)

        # See which random sample has a closer stdev
        y_strat_std_diff = abs(y.std() - y_strat_sub.std())
        y_rand_std_diff = abs(y.std() - y_rand_sub.std())
        strat_std_closer.append(y_strat_std_diff < y_rand_std_diff)

        # See which random sample has a closer stdev
        y_strat_mean_diff = abs(y.mean() - y_strat_sub.mean())
        y_rand_mean_diff = abs(y.mean() - y_rand_sub.mean())
        strat_mean_closer.append(y_strat_mean_diff < y_rand_mean_diff)

    assert np.array(strat_std_closer).mean() > 0.5
    assert np.array(strat_mean_closer).mean() > 0.5