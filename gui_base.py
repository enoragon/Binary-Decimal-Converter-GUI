import pygame

class TextElement(pygame.font.Font):

    def __init__(self, text='Default', size='12', position=(0,0)):

        self.text = text
        self.size = size
        self.position = position
        

class VisualElement(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.text = TextElement()

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def highlight(self):
        highlighted = [x + 30 for x in self.color if x < 225]
        self.image.fill(highlighted)

    def lowlight(self):
        lowlighted = [x - 30 for x in self.color if x > 30]
        self.image.fill(lowlighted)

    def render_text(self, text, position = False):
        if position:
            self.text.position = position
        else:
            self.text.position = (0,0)

        self.text.text = text
        font_object = pygame.font.Font(None, 22)
        rendered_text = font_object.render(self.text.text,False,(0,0,0))
        self.image.blit(rendered_text, self.text.position)



class ClickableElement(VisualElement):

    def __init__(self, x, y, width, height, color):
        VisualElement.__init__(self, x, y, width, height, color)

    def on_hover(self, function, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)
        else:
            self.image.fill(self.color)

    def on_click(self, function):
        pass
