import pandas as pd


EPS = 1e-10


def read_and_standardize(path):
    adj_matrices = pd.read_pickle(path)

    norm_adj_matrices = []

    for mat_i, mat in enumerate(adj_matrices):
        mat = _row_standardize(mat)
        norm_adj_matrices.append(mat)

    return norm_adj_matrices


def _row_standardize(adj_mat):
    # Adding EPSilon In case the row sum is 0
    return adj_mat / (adj_mat.sum(axis=1)[:,None] + EPS)


def produce_triples(adj_mat, k):
    graph_size = len(adj_mat)
    triples = [[] for _ in range(graph_size)]
    for i in range(graph_size):
        triples[i] += [(-adj_mat[i,j], i, j) for j in range(graph_size)]
        triples[i] += [( adj_mat[j,i], j, i) for j in range(graph_size)]

        # We're leaving the `k` most relevant edges
        triples[i] = sorted(triples[i], key=lambda trip: -abs(trip[0]))
        triples[i] = triples[i][:k]

    return triples


def extract_features(adj_mat, k):
    triples = produce_triples(adj_mat, k)
    graph_size = len(triples)
    feat_vectors = [[] for _ in range(graph_size)]
    for i in range(graph_size):
        feat_vec = [w for (w, _, _) in triples[i]]

        for (w, id_1, id_2) in triples[i]:
            sign = pd.np.sign(w)
            this_id, neighbor_id = (id_2, id_1) if sign == 1 else (id_1, id_2)
            assert this_id == i, (
                '({:.2f}, {}, {}), i={}'.format(sign, id_1, id_2, i)
            )
            feat_vec += [sign * v for (v, _, _) in triples[neighbor_id]]

        assert len(feat_vec) == k * (k + 1)
        feat_vectors[i] = feat_vec

    return pd.np.r_[feat_vectors]
