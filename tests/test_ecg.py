import numpy as np
from pathlib import Path

from physio import compute_ecg, compute_ecg_metrics

# read signals
test_folder = Path(__file__).parent
raw_ecg = np.load(test_folder / 'ecg1.npy')
srate = 1000.



def test_ecg():
    ecg, ecg_peaks = compute_ecg(raw_ecg, srate)




    compute_ecg_metrics(ecg_peaks, srate, min_interval_ms=500.,
                        max_interval_ms=2000., verbose = False)


if __name__ == '__main__':
    test_ecg()

