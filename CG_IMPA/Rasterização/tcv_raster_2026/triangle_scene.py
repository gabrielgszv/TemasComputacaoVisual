from src.base import BaseScene, Color
from src.shapes import Triangle

# class name should be Scene
class Scene(BaseScene):
    def __init__(self):
        super().__init__("Triangle Scene")
        self.background = Color(1, 1, 1)

        # Add some triangles to the scene
        self.add(Triangle((1.0, 1.0), (3.0, 1.0), (2.0, 3.0)), Color(1.0, 0.0, 0.0))  # Red triangle

        #Triangulo junto
        #self.add(Triangle((4.0, 3.0), (3.0, 1.0), (2.0, 3.0)), Color(0.0, 0.0, 1.0))  # Blue triangle

        #Triangulo separado
        self.add(Triangle((4.5, 1.5), (2.5, 3.0), (3.0, 4.5)), Color(0.0, 0.0, 1.0))  # Green triangle
