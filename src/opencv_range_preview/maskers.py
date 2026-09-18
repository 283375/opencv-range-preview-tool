from abc import ABC, abstractmethod

import cv2
import numpy as np
from typing_extensions import override


class Masker(ABC):
    CHANNELS: tuple[str, ...]

    data: dict[str, list[int]]

    @abstractmethod
    def __init__(self): ...
    @abstractmethod
    def mask(self, roiBgr: np.ndarray) -> np.ndarray: ...


class HsvMasker(Masker):
    CHANNELS = ("h", "s", "v")

    def __init__(self):
        self.data = {"h": [0, 0], "s": [0, 0], "v": [0, 0]}

    @property
    def lower(self):
        return np.array([self.data["h"][0], self.data["s"][0], self.data["v"][0]])

    @property
    def upper(self):
        return np.array([self.data["h"][1], self.data["s"][1], self.data["v"][1]])

    @override
    def mask(self, roiBgr: np.ndarray):
        hsv = cv2.cvtColor(roiBgr, cv2.COLOR_BGR2HSV)
        return cv2.inRange(hsv, self.lower, self.upper)


class RgbMasker(Masker):
    CHANNELS = ("r", "g", "b")

    def __init__(self):
        self.data = {"r": [0, 0], "g": [0, 0], "b": [0, 0]}

    @property
    def lower(self):
        # cv2.inRange compares channelwise against BGR
        return np.array([self.data["b"][0], self.data["g"][0], self.data["r"][0]])

    @property
    def upper(self):
        return np.array([self.data["b"][1], self.data["g"][1], self.data["r"][1]])

    @override
    def mask(self, roiBgr: np.ndarray):
        return cv2.inRange(roiBgr, self.lower, self.upper)
