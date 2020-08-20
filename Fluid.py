import pygame
from pygame.locals import *
import Eq_fluid as fluid_equation

class Particle:
    def __init__(self, List_pos, _R_len=10, _R_hei=10):
        self.List_pos = list(List_pos)
        self._R_len = _R_len
        self._R_hei = _R_hei
        self.Particle = pygame.rect.Rect(self.List_pos, (_R_len, _R_hei))

    def Move(self, new_pos):
        self.List_pos = new_pos
        self.Particle = pygame.rect.Rect(self.List_pos, (self._R_len, self._R_hei))

class Grass(Particle):
    def __init__(self, color, *args):
        self.color_grass = color
        super().__init__(*args)
        
    def Plot_screen(self, Display):
        pygame.draw.rect(Display, self.color_grass, self.Particle)

class Water(Particle):
    def __init__(self, color, *args):
        self.color_water = color
        self.velocity_vertex = [0,0]
        self.aceleration_vertex = [0,0]
        super().__init__(*args)
        
    def Plot_screen(self, Display):
        pygame.draw.rect(Display, self.color_water, self.Particle)
        
    def Gravity_implementation(self, gravity):
        component_gravity = [0,gravity]
        self.Velocity_sum_vertex(component_gravity)
        
    def Velocity_sum_vertex(self, component):
        for i in range(2):
            self.velocity_vertex[i] += component[i]
            
    def Velocity_implmentation(self):
        for i in range(2):
            self.List_pos[i] += self.velocity_vertex[i]

#vou implementar as configurações em um txt por enquanto fica aqui
_Size_display_x = 600
_Size_display_y = 600
green = (153,76,0)
blue = (0,0,255)
water_len_and_hei = 2
Gravity = 0.005

def Check_mouse(List_obj_1, List_obj_2):
    mouse_bool = pygame.mouse.get_pressed()
    List_posi = []
    if(mouse_bool[0]):
        List_posi = pygame.mouse.get_pos()
        List_obj_1.append(Grass(green, List_posi))
    elif(mouse_bool[2]):
        List_posi = pygame.mouse.get_pos()
        List_obj_2.append(Water(blue, List_posi, water_len_and_hei, water_len_and_hei))

def Check_is_runnning(Is_running=True):
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                Is_running = False

def Plot_particle(list_obj, Display):
    for i in list_obj:
        i.Plot_screen(Display)

def Gravity_range(List_obj):
    for i in List_obj:
        i.Gravity_implementation(Gravity)
        i.Velocity_implmentation()

def New_pos_implementation(List_obj):
    for i in List_obj:
        i.Move(i.List_pos)

def Initial():
    #creating an object of display class
    Display = pygame.display.set_mode((_Size_display_x, _Size_display_y))
    pygame.display.set_caption("Teste1")

    Is_running = True
    List_objParticle_grass = []
    List_objParticle_water = []

    while(Is_running):
        #check if the display was closed
        Check_is_runnning(Is_running)
        Display.fill((0,0,0))
        #check_if Mouse was clicked
        Check_mouse(List_objParticle_grass, List_objParticle_water)
        #plot the particles
        Plot_particle(List_objParticle_grass ,Display)
        Plot_particle(List_objParticle_water ,Display)
        #gravity water implementation
        Gravity_range(List_objParticle_water)
        New_pos_implementation(List_objParticle_water)
        #screen update
        pygame.display.update()

if __name__ == "__main__":
    Initial()
