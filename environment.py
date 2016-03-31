import pygame
import graphics
import gui_base
from CONSTANTS import *



class SceneBase():

    def __init__(self):
        self.next = self

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def terminate(self):
        pygame.quit()

class Environment(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.surface = graphics.SCREEN
        self.surface.fill((GRAY))
        self.gui_group = pygame.sprite.Group()

        self.question = gui_base.VisualElement(40, 100, 300, 40, (BLUE))
        self.square = gui_base.VisualElement(40,40,420,40,(BLUE))
        self.red_square = gui_base.ClickableElement(360,100,40,40,(BLUE))
        self.low_square = gui_base.ClickableElement(420,100,40,40,(BLUE))
        self.convert = gui_base.ClickableElement(200, 220, 100, 40, (BLUE))
        self.output = gui_base.VisualElement(40, 280, 420, 40, (WHITE))
        self.input = gui_base.VisualElement(40, 160, 420, 40, (WHITE))
        
        self.gui_group.add(self.square,
                           self.red_square,
                           self.low_square,
                           self.question,
                           self.convert,
                           self.output,
                           self.input)



    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')
            if event.type == pygame.QUIT:
                self.terminate()

    def upedate(self):
        pass


    def render(self):
        self.gui_group.draw(self.surface)
        self.red_square.on_hover(self.red_square.highlight)
        self.low_square.on_hover(self.low_square.highlight)
        self.convert.on_hover(self.convert.highlight)
        self.square.render_text('Binary/Decimal Converter', (138,13))
        self.question.render_text('Binary to Decimal or Decimal to Binary?', (6,13))
        self.red_square.render_text('B-D', (6,13))
        self.low_square.render_text('D-B', (6,13))
        self.convert.render_text('Convert', (22,13))
        self.output.render_text('010110', (22,13))
        self.input.render_text('enter numbers', (6,13))
        pygame.display.flip()


