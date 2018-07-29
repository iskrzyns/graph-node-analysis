import numpy as np


class SwapNoiseGenerator:
    def __init__(self, prob_swap=0.15):
        self.prob_swap = prob_swap

    def batch_generator(self, X, y=None, batch_size=32):
        n_rows, n_feats = X.shape
        while True:
            batch_indices = np.random.choice(n_rows, batch_size, replace=False)
            X_batch_output = X[batch_indices, :]

            replacement_mask = np.random.random(size=X_batch_output.shape) < self.prob_swap
            replacement_row_indices = np.random.choice(n_rows, (batch_size, n_feats), replace=True)
            replacement_col_indices = [np.arange(n_feats)] * batch_size
            replacement_matrix = X[replacement_row_indices, replacement_col_indices]

            X_batch_input = np.where(replacement_mask, replacement_matrix, X_batch_output)
            yield X_batch_input, X_batch_output
