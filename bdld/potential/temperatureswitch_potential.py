"""Entropic double-well potential

Described in Eq. 17 of Banisch, R; Trstanova, Z; Bittracher, A; 
Klus, S; Koltai, P. "Diffusion maps tailored to arbitrary non-degenerate
Ito Processes". Applied and Computational Harmonic Analysis (2020), 48, 242-265

https://doi.org/10.1016/j.acha.2018.05.001

"""

from typing import List, Optional, Union
import numpy as np

from bdld.potential.potential import Potential


class EntropicDoubleWellPotential(Potential):
    """Entropic double-well potential

    This is a 2D potential of four-well system whose slowest sdynamics changes
    from crossing a predominately entropic barier to crossing a predominately
    entropic barier to crossing a predominately energetic barrier given by the 
    equation

    f(x,y) =  h_x * (x**2 - 1)**2 + (h_y + a (x,delta)) * (y**2-1)**2
    
    in N=2 dimensions with 
   
    a(x,delta)=(1/5)*(1 + 5 * exp(-(x-x_0)**2 /delta))**2

    where h_x=0.5, h_y=1.0, describe the well width in the x- and y- directions,
    respectively.x_0=0

    Initial condition X_0=(-1,-1)

    delta=1/20 or 0.05 describes how much the barrier-crossing pathway along 
    the x-direction is squeezed relative to the pathway along the barrier in
    the y-direction.

    :param hx: Scaling factor for the x-direction
    :param hy: Scaling factor for the y-direction
    :param x0: Center of the function a(x, δ)
    :param delta: Parameter controlling the width of a(x, δ)

    Described in Eq. 17 of Banisch, R; Trstanova, Z; Bittracher, A; 
    Klus, S; Koltai, P. "Diffusion maps tailored to arbitrary non-degenerate
    Ito Processes". Applied and Computational Harmonic Analysis(2020), 48, 242-265
    
    https://doi.org/10.1016/j.acha.2018.05.001


    The range of the potential is currently assumed to be [-2.0, 2.0] in both
    directions. 

    """

    def __init__(self, hx: float, hy: float, x0: float, delta: float) -> None:
        """Initialize entropic double-well potential

        :param hx: Scaling factor for the x-direction
        :param hy: Scaling factor for the y-direction
        :param x0: Center of the function a(x, δ)
        :param delta: Parameter controlling the width of a(x, δ)
        """
        self.n_dim = 2
        self.ranges = [(-2.0,2.0),(-2.0,2.0)]
        self.hx = hx or 0.5
        self.hy = hy or 1.0 
        self.x0 = x0 or 0.0
        self.delta = delta or 0.05

    def a(self, x: float) -> float:
        """Calculate a(x, δ) component of the potential

        :param x: Position along the x-axis
        :return: The value of a(x, δ)
        """
        term = (1 + 5 * np.exp(-((x - self.x0) ** 2) / self.delta))**2
        return (1/5) * term

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
        term1 = self.hx * (x**2 - 1)**2
        term2 = (self.hy + a_x) * (y**2 - 1)**2
        
        potential_energy = term1 + term2
        return potential_energy

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
    def force(self, x, y):
        a_x = self.a(x)
        d_a_dx = -(self.delta**4) * (x - self.x0) * np.exp(-((x - self.x0) ** 2) / self.delta) / self.delta

        force_x = -4 * self.hx * x * (x ** 2 - 1) - 2 * (self.hy + a_x) * (y ** 2 - 1) ** 2 * d_a_dx 
        force_y = -8 * (self.hy + a_x) * (y ** 2 - 1) * y
        return np.array([force_x, force_y])



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

