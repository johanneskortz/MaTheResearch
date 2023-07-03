import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import morlet2
from scipy.signal import cwt


def main():
    # z = x + i * y
    x_ = np.sin(np.random.randint(0, 5, 1000))
    y_ = np.sin(np.random.randint(0, 5, 1000))
    z = np.array([complex(x, y) for x, y in zip(x_, y_)])

    # morlet_signal = morlet2(100, 5, 1, complete=True)
    morlet_signal = morlet2(100, 10, 5)

    cwt_result = cwt(z, morlet2, np.arange(1, 10), dtype=np.complex128)

    fig, ax = plt.subplots(1, 3, figsize=(30, 20))
    ax[0].imshow(np.abs(cwt_result))
    # ax[0].set(xlabel="time", ylabel="Amplitude")
    ax[1].imshow(np.abs(cwt_result))
    # ax[1].set(xlabel="time", ylabel="Amplitude")
    ax[2].imshow(np.abs(cwt_result) * np.cos(np.angle(cwt_result)))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
