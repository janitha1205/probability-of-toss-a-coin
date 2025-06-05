import numpy as np


def pdf(z, std, mu):

    return (1 / (std * np.sqrt(2 * np.pi))) * (np.exp(-((z - mu) ** 2) / (2 * std**2)))


def area_pdf(stp, ub, lb, mu, std):
    cum = lb + stp
    area = 0
    while ub >= cum:
        area += ((pdf(lb, std, mu) + pdf(cum, std, mu)) / 2) * stp
        cum += stp
    return area


def prob(z, mu, std):
    stp = 0.01
    lb = mu - 25 * std
    ub = mu + 25 * std
    arp = area_pdf(stp, z, lb, mu, std) / area_pdf(stp, ub, 0, mu, std)
    print("prob of p(z < 0): ", arp)
    print("prob of p(z > 0): ", 1 - arp)
    return arp


prob(155, 125, 5.8)
