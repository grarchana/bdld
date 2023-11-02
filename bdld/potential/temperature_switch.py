"""Temperature Switch potential

Described in Eq. 17 of Banisch, R; Trstanova, Z; Bittracher, A; 
Klus, S; Koltai, P. "Diffusion maps tailored to arbitrary non-degenerate
Ito Processes". Applied and Computational Harmonic Analysis (2020), 48, 242-265

https://doi.org/10.1016/j.acha.2018.05.001

"""

from typing import List, Optional, Union
import numpy as np
from bdld.potential.potential import Potential

class TemperatureSwitchPotential(Potential):
    """Temperature Switch potential

    This is a 2D potential of a four-well system whose slowest dynamics change
    from crossing a predominately entropic barrier to crossing a predominately energetic barrier given by the equation:

    f(x, y) = h_x * (x**2 - 1)**2 + (h_y + a(x, delta)) * (y**2 - 1)**2

    in N=2 dimensions with a(x, delta) = (1/5) * (1 + 5 * exp(-(x - x_0)**2 / delta))**2

    where h_x = 0.5, h_y = 1.0, describe the well width in the x- and y-directions, respectively. x_0 = 0

    Initial condition X_0 = (-1, -1)

    delta = 1/20 or 0.05 describes how much the barrier-crossing pathway along the x-direction is squeezed relative to the pathway along the barrier in the y-direction.

    :param hx: Scaling factor for the x-direction
    :param hy: Scaling factor for the y-direction
    :param x0: Center of the function a(x, δ)
    :param delta: Parameter controlling the width of a(x, δ)

    Described in Eq. 17 of Banisch, R; Trstanova, Z; Bittracher, A; Klus, S; Koltai, P. "Diffusion maps tailored to arbitrary non-degenerate Ito Processes". Applied and Computational Harmonic Analysis (2020), 48, 242-265

    https://doi.org/10.1016/j.acha.2018.05.001

    The range of the potential is currently assumed to be [-2.0, 2.0] in both directions.
    """
    
    def __init__(
        self,
        hx: Optional[float] = None,
        hy: Optional[float] = None,
        x0: Optional[float] = None,
        delta: Optional[float] = None,
    ) -> None:
        """Initialize temperature-switch potential

        :param hx: Scaling factor for the x-direction
        :param hy: Scaling factor for the y-direction
        :param x0: Center of the function a(x, δ)
        :param delta: Parameter controlling the width of a(x, δ)
        """
        super().__init()
        self.n_dim = 2
        self.ranges = [(-2.0, 2.0), (-2.0, 2.0)]
        self.hx = hx or 0.5
        self.hy = hy or 1.0
        self.x0 = x0 or 0.0
        self.delta = delta or 0.05

    def a(self, x: float) -> float:
        """Calculate a(x, δ) component of the potential

        :return: The value of a(x, δ)
        """
        term = (1 + 5 * np.exp(-((x - self.x0) ** 2) / self.delta)) ** 2
        return (1 / 5) * term

    def energy(self, pos: Union[List[float], np.ndarray]) -> float:
        """Calculate the potential energy at a given position

        :param pos: position to be evaluated [x, y]
        :return: The potential energy at (x, y)
        """
        x = pos[0]
        y = pos[1]
        
        # Calculate the a(x, δ) component
        a_x = self.a(x)
        
        # Calculate the potential energy U(x, y)
        term1 = self.hx * (x ** 2 - 1) ** 2
        term2 = (self.hy + a_x) * (y ** 2 - 1) ** 2
        return term1 + term2

    def force(self, pos: Union[List[float], np.ndarray]) -> np.ndarray:
        """Calculate the force vector at a given position

        :param pos: position to be evaluated [x, y]
        :return: The force vector [Fx, Fy]
        """
        x = pos[0]
        y = pos[1]
        
        # Calculate the a(x, δ) component
        a_x = self.a(x)
        
        # Calculate the forces
        d_a_dx = -(4 / self.delta) * np.exp(-((x - self.x0) ** 2) / self.delta) * (1 + 5 * np.exp(-((x - self.x0) ** 2) / self.delta)) * (x - self.x0)

        force_x = -4 * self.hx * x * (x ** 2 - 1) + d_a_dx * (y ** 2 - 1) ** 2
        force_y = -4 * (self.hy + a_x) * y * (y ** 2 - 1)
        return np.array([force_x, force_y])

    def __str__(self) -> str:
        """Return a description string for the Temperature Switch potential"""
        return (
            f"Temperature Switch Potential:\n"
            f"  hx = {self.hx}\n"
            f"  hy = {self.hy}\n"
            f"  x0 = {self.x0}\n"
            f"  delta = {self.delta}\n"
            f"  Range: x [-2.0, 2.0], y [-2.0, 2.0]\n"
        )
  
    
    
    
    
    
    
    
    
    
    
    
    

