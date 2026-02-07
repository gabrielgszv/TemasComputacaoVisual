from src.base import BaseScene, Color
from src.shapes import ImplicitFunction

# class name should be Scene
class Scene(BaseScene):
    def __init__(self):
        super().__init__("Triangle Scene")
        self.background = Color(1, 1, 1)

        def function(point):
            x, y = point
            return (0.004 + 0.110*x- 0.177 * y - 0.174 * x**2+ 0.224 * x * y- 0.303 * y**2- 0.168 * x**3+ 0.327 * x**2 * y- 0.087 * x * y**2- 0.013 * y**3+ 0.235 * x**4- 0.667 * x**3 * y+ 0.745 * x**2 * y**2- 0.029 * x * y**3+ 0.072 * y**4)
        
        # Add some triangles to the scene
        self.add(ImplicitFunction(function), Color(0.0, 0.6, 0.0))  # Function green
        