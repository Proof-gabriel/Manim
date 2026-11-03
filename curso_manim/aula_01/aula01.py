from manim import *

class basic(Scene):
    def construct(self):
        # ==========================================
        # BLOCO 1: CONFIGURAÇÃO DA CENA E CORES
        # ==========================================
        self.camera.background_color = "#F4F0E6"
        BYRNE_RED = "#D9381E"
        BYRNE_BLACK = "#1A1A1A"

        # ==========================================
        # BLOCO 2: DECLARAÇÃO DOS ELEMENTOS (Mobjects)
        # ==========================================
        quadrado_1 = Square(side_length=2, color=BLACK)
        quadrado_1.set_fill(BLUE, opacity=0.3)
        #quadrado_1.move_to(2 * RIGHT)

        # ==========================================
        # BLOCO 3: CRONOGRAMA DE ANIMAÇÕES
        # ==========================================
        self.play(Create(quadrado_1), run_time=1)
        self.wait(4)