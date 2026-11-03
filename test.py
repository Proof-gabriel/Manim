from manim import *

class TestePreview(Scene):
    def construct(self):
        circulo = Circle()
        circulo.set_fill(BLUE, opacity=0.5)
        self.play(Create(circulo))
        self.wait(1)