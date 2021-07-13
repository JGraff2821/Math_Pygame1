from homework.hw7.Letters import *
from homework.hw7.Action import *



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


if __name__ == '__main__':
    # Making My Picture Objects****************Only Needs to Be done once **********************

    # define the RGB value for colors that I may use throughout the Game
    white = (255, 255, 255)
    green = (0, 255, 255)
    orange = (255, 100, 0)
    black = (0,0,0)

    # activate the pygame library .
    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    # assigning values for the length and width of the screen
    X = 1200
    Y = 900

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Golden Numbers')

    #List of Basic Pictures*******************
    list_of_pictures = []
    # Making the Mad Scientist
    rel_path = "images\Mad_scientist_transparent_background.svg.png"
    mad_scientist = Picture(rel_path, 900, 600)
    mad_scientist.scale_image(300, 300)
    list_of_pictures.append(mad_scientist)

    #Making Magic Potion
    rel_path ="images\magic-potion.png"
    magic_potion = ActionPicture(rel_path,600,700,1)
    magic_potion.scale_image(150,150)
    list_of_pictures.append(magic_potion)

    #making subtraction Potion
    rel_path = "images\sub_potion.png"
    sub_potion = ActionPicture(rel_path, 425,725,2)
    sub_potion.scale_image(100,100)
    list_of_pictures.append(sub_potion)

    #making mult potioin
    rel_path= "images\mult_potion.png"
    mult_potion = ActionPicture(rel_path, 225, 700,3)
    mult_potion.scale_image(150,150)
    list_of_pictures.append(mult_potion)

    #making mod potion
    rel_path = "images\magic_mod.jpg"
    mod_potion = ActionPicture(rel_path,25,700,4)
    mod_potion.scale_image(150,150)
    list_of_pictures.append(mod_potion)



    # List of Effects ******************

    # List of Basic Text ******************
    Letters1 = Letters('timesnewroman', 100, "Magic Numbers", black, white, 0, 0)
    Letters2 = Letters('timesnewroman', 30, "MagicAdd ("+str(magic_potion.EffectNumber)+")", orange, white, 600, 840)
    Letters3 = Letters('timesnewroman', 30, "MagicSub (" + str(sub_potion.EffectNumber) + ")", orange, white, 400,
                       840)
    Letters4 = Letters('timesnewroman', 30, "MagicMult (" + str(mult_potion.EffectNumber) + ")", orange, white, 200,840)
    Letters5 = Letters('timesnewroman', 30, "MagicMod (" + str(mod_potion.EffectNumber) + ")", orange, white, 25,
                       840)
    Letters6 = Letters('timesnewroman',30, "Target Number:", orange,white,500,250)
    Letters7 = Letters('timesnewroman', 30, "Your Number:", orange, white, 200, 250)
    Letters8 = Letters('timesnewroman', 30, "Bottles Used:", orange, white, 800, 250)


    # List of Compliments ******************
    list_of_compliments = []
    first = NumberLetter('timesnewroman', 150, "", green, orange, 200, 300)
    second = NumberLetter('timesnewroman', 150, "", green, orange, 500, 300)
    Third = NumberLetter('timesnewroman',150,"",green, orange, 800,300)
    second.__int__()
    second.is_target_number()
    first.__int__()
    Third.__int__()
    list_of_pictures.append(first)
    list_of_compliments.append(first)




    # infinite loop that will keep the game open for me
    x = 50
    bottle_counter = 0
    while True:
        Third.number =bottle_counter
        Third.message = " " + str(Third.number) + " "
        Third.refresh()
        # Make sure all objects are printed to the screen.
        display_surface.blit(mad_scientist.image, (mad_scientist.x_cord, mad_scientist.y_cord))
        display_surface.blit(Letters1.MessageSurface, (Letters1.x, Letters1.y))
        display_surface.blit(first.MessageSurface, (first.x, first.y))

        # Little Counter that deals with the decompression of the mouse.
        x-=1

        # display the mouse coordinates:
        if x <= 0:

            buttonStates = pygame.mouse.get_pressed(3)
            if buttonStates[0] is True:
                position_touched = pygame.mouse.get_pos()
                print("Mouse Clicked", position_touched)
                x = 50
                for pictures in list_of_pictures:
                    if pictures.coordInArea(position_touched):
                        print("Picture Clicked")
                        bottle_counter+=1
                        if pictures.EffectID == 1:
                            first.add_number(pictures.EffectNumber)
                        if pictures.EffectID ==2:
                            first.sub_number(pictures.EffectNumber)
                        if pictures.EffectID == 3:
                            first.mult_number(pictures.EffectNumber)
                        if pictures.EffectID == 4:
                            first.mod_number(pictures.EffectNumber)

                        # for each Effect, if selected, do the exchange, deselect.

        # completely fill the display surface object
        # with white colour
        display_surface.fill(white)

        # copying all Image Surfaces to Respective Postions:
        display_surface.blit(mad_scientist.image, (mad_scientist.x_cord, mad_scientist.y_cord))
        display_surface.blit(magic_potion.image, (magic_potion.x_cord, magic_potion.y_cord))
        display_surface.blit(sub_potion.image, (sub_potion.x_cord,sub_potion.y_cord))
        display_surface.blit(mult_potion.image,(mult_potion.x_cord,mult_potion.y_cord))
        display_surface.blit(mod_potion.image,(mod_potion.x_cord,mod_potion.y_cord))

        display_surface.blit(Letters1.MessageSurface, (Letters1.x,Letters1.y))
        display_surface.blit(Letters2.MessageSurface, (Letters2.x, Letters2.y))
        display_surface.blit(Letters3.MessageSurface, (Letters3.x, Letters3.y))
        display_surface.blit(Letters4.MessageSurface, (Letters4.x, Letters4.y))
        display_surface.blit(Letters5.MessageSurface, (Letters5.x, Letters5.y))
        display_surface.blit(Letters6.MessageSurface, (Letters6.x, Letters6.y))
        display_surface.blit(Letters7.MessageSurface, (Letters7.x, Letters7.y))
        display_surface.blit(Letters8.MessageSurface, (Letters8.x, Letters8.y))

        display_surface.blit(first.MessageSurface, (first.x,first.y))
        display_surface.blit(second.MessageSurface, (second.x,second.y))
        display_surface.blit(Third.MessageSurface, (Third.x, Third.y))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
            pygame.display.update()

            Letters1.refresh()