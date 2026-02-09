from src.base import BaseScene, Color
from src.shapes import Mandelbrot

class Scene(BaseScene):
    def __init__(self):
        super().__init__("Mandelbrot Scene")
        self.background = Color(0.5, 0.5, 0.5)

        self.add(Mandelbrot(max_iter=100), Color(0, 0, 0))
