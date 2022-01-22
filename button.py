
class Button():
    def __init__(self,name,x,y,image,font,font_size,color,rect_color,pygame,surface):
        self.name=name
        self.font_size=int((surface.get_width() / surface.get_height()) * font_size)
        self.font=pygame.font.Font(font,font_size)
        if x=='center':
            self.center=True
            self.text = self.font.render(str(name), True, color)
            self.rect = pygame.Rect(self.text.get_rect(center=(surface.get_width() //2, surface.get_height()))[0],y, self.text.get_width()+50,self.text.get_height()+50)
            self.x = self.rect.x
        else:
            self.center=False
            self.x=x
        self.y = y
        self.pygame=pygame
        self.image=image
        self.color=color
        self.rect_color=rect_color
        self.surface=surface
        
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def draw(self):
        if self.center:
            self.pygame.draw.rect(self.surface, self.rect_color, self.rect)
            self.surface.blit(self.text,  self.text.get_rect(center=(self.rect.x-self.text.get_width()//2+self.rect.width-25, self.rect.y-self.text.get_height()//2+self.rect.height-25)))
            self.width, self.height = self.rect.width, self.rect.height

        else:
            text = self.font.render(str(self.name),True,self.color)
            self.x-=text.get_width()//3
            self.y-=text.get_height()//3
            rect = self.pygame.Rect(self.x,self.y,text.get_width()*2, text.get_height()*2)
            self.pygame.draw.rect(self.surface, self.rect_color, rect)
            self.surface.blit(text, (self.x+text.get_width()//2, self.y+text.get_height()//2))
            self.width, self.height = rect.width, rect.height
