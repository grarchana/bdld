"""Dual Channel Double-Well Potential 

Described in Eq. 7 of Solomon Asghar, Qing-Xiang Pei, Giorgio Volpe, and Ran Ni. "Efficient Rare Event Sampling with Unsupervised Normalising Flows". 

https://arxiv.org/abs/2401.01072

"""
from typing import List, Optional, Union
import numpy as np

from bdld.potential.potential import Potential


class DualChannelDoubleWellPotential(Potential):
    """Dual-channel double-well potential

    This potential consists of two wells connected by two distinct cahneels: a top channel and a bottom channel. A peak of   variable separates the two.
    U(x, y) = 9 * (x**4 - 2 * y**2 + y**4 + 78/37 * x**2 * (y**2 - 1) + 1/90 * y + 1.11097 + k_BH * np.exp(-(x**2 + y**2)))
 
    where k_BH is a parameter. The height of the peak between the two channels can be modulated by changing k_BH. k_BH=0 for peak height of 10k_BT_eff.

    The force components for x and y are given by:

    Fx = -9 * (4 * x**3 + 156/37 * x * (y**2 - 1) - 2 * x * k_BH * np.exp(-(x**2 + y**2)))

    Fy = -9 * (-4 * y + 4 * y**3 + 156/37 * x**2 * y + 1/90 - 2 * y * k_BH * np.exp(-(x**2 + y**2)))

    :param k_BH: parameter in the potential
    """

    def __init__(
        self,
        k_BH: Optional[float] = None,
        scaling_factor: Optional[float] = None,
    ) -> None:
         
        """Initialize dual-channel double-well potential

        :param k_BH: parameter in the potential, optional
        """
        super().__init__()
        self.n_dim = 2
        self.ranges = [(-2.0, 2.0), (-2.0, 2.0)]
        self.k_BH = k_BH or 0.0
        self.b = scaling_factor or 1.0

    def __str__(self) -> str:
        """Give out coefficients"""
        text = (
            "Dual-channel double-well potential\n"
            + f"  k_BH: {self.k_BH}"
        )
        return text

    def energy(self, pos: Union[List[float], np.ndarray]) -> float:
        """ Calculate the potential energy at a given position

        :param pos: position to be evaluated (given as list or array even in 1d)
        :return: energy
        """
        x = pos[0]
        y = pos[1]
        potential_energy = 9 * (
            x**4 - 2 * y**2 + y**4 + 78/37 * x**2 * (y**2 - 1) + 1/90 * y + 1.11097 + self.k_BH * np.exp(-(x**2 + y**2))
        )
        return potential_energy

    def force(self, pos: Union[List[float], np.ndarray]) -> np.ndarray:
        """Get force at position

        :param pos: position to be evaluated [x, y](given as list or array even in 1d)
        :return force: array with force per direction [Fx, Fy]
        """
        x = pos[0]
        y = pos[1]
         # Calculate the forces
        force_x = -9 * (4 * x**3 + 156/37 * x * (y**2 - 1) - 2 * x * self.k_BH * np.exp(-(x**2 + y**2)))
        force_y = -9 * (-4 * y + 4 * y**3 + 156/37 * x**2 * y + 1/90 - 2 * y * self.k_BH * np.exp(-(x**2 + y**2)))
        return np.array([force_x, force_y])

    def __str__(self) -> str:
        """Return a description string for the Dual-channel double-well potential"""
        return (
            f"Dual-channel double-well potential:\n"
            f"  k_BH: {self.k_BH}\n"
            f"  Range: x [-2.0, 2.0], y [-2.0, 2.0]"
        )
