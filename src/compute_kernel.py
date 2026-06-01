"""Fourier seasonality features for hourly demand."""

from __future__ import annotations

import math

import numpy as np


def fourier_seasonality(t: np.ndarray, period: float, n_harmonics: int) -> np.ndarray:
    ts = np.asarray(t, dtype=float)
    n = len(ts)
    n_feats = n_harmonics * 2
    out = np.zeros(n * n_feats, dtype=float)
    for i, ti in enumerate(ts):
        for h in range(n_harmonics):
            k = h + 1
            angle = 2.0 * math.pi * k * ti / period
            out[i * n_feats + 2 * h] = math.sin(angle)
            out[i * n_feats + 2 * h + 1] = math.cos(angle)
    return out
