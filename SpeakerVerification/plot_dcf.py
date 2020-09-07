import os
import fire
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from score_utils import compute_pmiss_pfa_rbst



def get_fnr_fpr(scorefile):
    scores = []
    labels = []
    with open(scorefile) as readlines:
        for line in readlines:
            tokens = line.strip().split()
            scores.append(float(tokens[-1]))
            labels.append(tokens[0][:7] == tokens[1][:7])

    scores = np.hstack(scores)
    labels = np.hstack(labels)
    fnr, fpr = compute_pmiss_pfa_rbst(scores, labels)

    return fnr, fpr


def plot(save_path='here', *scorefiles):

    xytick = [0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02,
              0.05, 0.1, 0.2, 0.4]
    xytick_labels = map(str, [x * 100 for x in xytick])

    plt.xticks(norm.ppf(xytick), xytick_labels)
    plt.yticks(norm.ppf(xytick), xytick_labels)
    plt.xlim(norm.ppf([0.00051, 0.5]))
    plt.ylim(norm.ppf([0.00051, 0.5]))
    plt.xlabel("false-alarm rate [%]", fontsize=12)
    plt.ylabel("false-reject rate [%]", fontsize=12)

    for scorefile in scorefiles:
        fnr, fpr = get_fnr_fpr(scorefile)
        p_miss = norm.ppf(fnr)
        p_fa = norm.ppf(fpr)
        # plt.plot(p_fa, p_miss, 'r')
        plt.plot(p_fa, p_miss, label=os.path.basename(scorefile))
        plt.legend(loc='best')

    plt.grid()
    # plt.show()

    plt.savefig(save_path, dpi=200)


if __name__ == '__main__':
    fire.Fire(plot)