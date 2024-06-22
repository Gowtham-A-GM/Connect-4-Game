import pygame                       # Created on Monday, May 1, 2023
import random                       # Modified on Friday, April 26, 2024
                                    # Created By : Hidden Blade

pygame.font.init()                  # To initate PYGAME Font library
pygame.mixer.init()                 # To initate PYGAME Sound aspect of pygame

class game:
    
    def __init__(self):     # self : placeholder that refers to the instance of the class itself
        self.WIDTH, self.HEIGTH = 1266,668
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGTH))       # (self.WIDTH, self.HEIGTH),pygame.FULLSCREEN
        pygame.display.set_caption("CONNECT 4 GAME")

        # COLOURS
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0
        self.RED = 255, 0, 0
        self.GREEN = 0, 255, 0
        self.BLUE = 0, 0, 255
        self.YELLOW = 255, 255, 0
        self.VIOLET = 127, 0, 255
        self.PINK = 255, 51, 255
        self.GREY = 90, 85, 85
        
       # LOGO
        self.IMPORT_LOGO_HIDDEN_BLADE = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Logo_Hidden_Blade.jpg')

        # ICONS
        self.IMPORT_ICONS_THEME_NEON = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Theme_Neon.png')
        self.IMPORT_ICONS_THEME_DARK = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Theme_Dark.png')
        self.IMPORT_ICONS_MUSIC_ON = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Music_ON.png')
        self.IMPORT_ICONS_MUSIC_OFF = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Music_OFF.png')
        self.IMPORT_ICONS_SOUND_ON = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Sound_Effect_ON.png')
        self.IMPORT_ICONS_SOUND_OFF = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Sound_Effect_OFF.png')
        

        # BACKGROUNDS
        self.IMPORT_BACKGROUND_MENU_NEON = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Menu_Neon.jpg')
        self.IMPORT_BACKGROUND_MENU_DARK = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Menu_Dark.jpg')
        self.IMPORT_BACKGROUND_GAME_NEON = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Game Background.jpg')
        self.IMPORT_BACKGROUND_GAME_DARK = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Game Mode Background-3.jpg')
        self.IMPORT_BACKGROUND_GAME_MODE = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Game Mode.jpg')
        self.IMPORT_BACKGROUND_RESULT = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Background Images\Result Background.jpg')
        self.IMPORT_CREDITS = pygame.image.load(r"Python\Games\Connet 4\Asset Connect 4\credits.png")

        # PLAYERS IMAGES
        self.IMPORT_IMAGE_PLAYER_X = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Player X.png')
        self.IMPORT_IMAGE_PLAYER_O = pygame.image.load(r'Python\Games\Connet 4\Asset Connect 4\Player O.png')
 
        # AUDIOS
        self.AUDIO_BGM_Menu = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\BGM_Menu.mp3')
        self.AUDIO_BGM_Mode_Simple = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\BGM_Mode_Simple.mp3')
        self.AUDIO_BGM_Mode_Complex = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\BGM_Mode_Complex.mp3')
        self.AUDIO_SEFX_BUTTON_CLICK = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\SEFX_Button_Click.wav')
        self.AUDIO_SEFX_XO_INSERT = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\SEFX_XO_Insert.wav')
        self.AUDIO_SEFX_WIN = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\SEFX_Win.wav')
        # self.AUDIO_SEFX_GRAVITY = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Sounds_&_Effects\SEFX_Gravity.wav')
        
        self.IMPORT_SOUND_DRAW_PLAYER = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\Draw Player.mp3')
        self.IMPORT_SOUND_END = pygame.mixer.Sound(r'Python\Games\Connet 4\Asset Connect 4\End Sound.mp3')

        # FONTS
        self.FONT_EXIT_BOX = pygame.font.SysFont('Fredoka One', 40)      # SysFont("FontName, FontSize")
        self.FONT_EXIT_BOX_OPTONS = pygame.font.SysFont('Fredoka One', 35)      # SysFont("FontName, FontSize")
        self.FONT_RESTART_WIN = self.FONT_EXIT_BOX
        self.FONT_RESTART_WIN_OPTIONS = self.FONT_EXIT_BOX_OPTONS
        self.FONT_RESTART_BOX = pygame.font.SysFont('Fredoka One', 40)
        self.FONT_PLAYER_MOVE_BOX = pygame.font.SysFont('Fredoka One', 30)
        self.FONT_GRAVITY_BOX = pygame.font.SysFont('Fredoka One', 55)
        self.FONT_CERDITS_Title_BOX = pygame.font.SysFont('Fredoka One', 25)
        self.FONT_CERDITS_Name_BOX = pygame.font.SysFont('Fredoka One', 15)
        self.FONT_GAME_MODE = pygame.font.SysFont('Fredoka One', 40)
        self.FONT_GAME_MODE_OPTIONS = pygame.font.SysFont('Fredoka One', 30)
        self.FONT_RESULT = pygame.font.SysFont('Fredoka One', 40)
        self.FONT_RESULT_OPTIONS = pygame.font.SysFont('Fredoka One', 30)
        self.FONT_MENU_CONNECT_4= pygame.font.Font(r"Python\Games\Connet 4\Asset Connect 4\Fonts\neuropolitical rg.otf",50)   # pygame.font.Font(font_path, font_size)
        self.FONT_MENU_OPTIONS = pygame.font.SysFont('Fredoka One', 40)
        self.FONT_MENU_SETTINGS = pygame.font.SysFont('Fredoka One', 40)
        self.FONT_MENU_SETTINGS_OPTIONS = pygame.font.SysFont('Fredoka One', 30)

       
        # GAME REQUIREMENTS
        self.board = {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ',
                      6 : ' ', 7 : ' ', 8 : ' ', 9 : ' ', 10: ' ',
                      11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
                      16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
                      21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' '}

        self.PLAYER_X = 'X'
        self.PLAYER_O = 'O'
        self.PLAYER = self.PLAYER_X         # First Move is Player X
        
        self.FPS = 30
        self.GRAVITY = None
        self.RESTART = False
        self.THEME = 'NEON'
        self.MUSIC = 'ON'
        self.SOUND = 'ON'

        self.GAME_BORDER_EACH_DIMENSIION = self.border('GAME_BORDER_EACH_DIMENSIION', border_value = True )
        self.LOGO_HIDDEN_BLADE = pygame.transform.scale(self.IMPORT_LOGO_HIDDEN_BLADE, (self.WIDTH/5,self.HEIGTH/7))

        self.ICONS_MUSIC_ON = pygame.transform.scale(self.IMPORT_ICONS_MUSIC_ON, (50, 50))
        self.ICONS_MUSIC_OFF = pygame.transform.scale(self.IMPORT_ICONS_MUSIC_OFF, (50, 50))
        self.ICONS_SOUND_ON = pygame.transform.scale(self.IMPORT_ICONS_SOUND_ON, (50, 50))
        self.ICONS_SOUND_OFF = pygame.transform.scale(self.IMPORT_ICONS_SOUND_OFF, (50, 50))

        self.IMAGE_PLAYER_X = pygame.transform.scale(self.IMPORT_IMAGE_PLAYER_X, self.GAME_BORDER_EACH_DIMENSIION)
        self.IMAGE_PLAYER_O = pygame.transform.scale(self.IMPORT_IMAGE_PLAYER_O, self.GAME_BORDER_EACH_DIMENSIION)

        self.BACKGROUND_MENU_NEON = pygame.transform.scale(self.IMPORT_BACKGROUND_MENU_NEON, (self.WIDTH, self.HEIGTH))
        self.BACKGROUND_MENU_DARK = pygame.transform.scale(self.IMPORT_BACKGROUND_MENU_DARK, (self.WIDTH, self.HEIGTH))
        self.BACKGROUND_GAME_NEON = pygame.transform.scale(self.IMPORT_BACKGROUND_GAME_NEON, (self.WIDTH, self.HEIGTH))
        self.BACKGROUND_GAME_DARK = pygame.transform.scale(self.IMPORT_BACKGROUND_GAME_DARK, (self.WIDTH, self.HEIGTH))
        self.BACKGROUND_GAME_MODE = pygame.transform.scale(self.IMPORT_BACKGROUND_GAME_MODE, (self.WIDTH, self.HEIGTH))
        self.BACKGROUND_RESULT = pygame.transform.scale(self.IMPORT_BACKGROUND_RESULT, (self.WIDTH, self.HEIGTH))
        self.IMG_CREDITS = pygame.transform.scale(self.IMPORT_CREDITS, (self.WIDTH, self.HEIGTH))

        

        self.COLOUR_LINES_GAME_BOARD = self.WHITE

        #AUDIO CONTROLLER
        self.PLAY_BGM_MENU = True
        self.PLAY_BGM_Mode_Simple = False
        self.PLAY_BGM_Mode_Complex = False

        self.DRAW_IMAGE_DATA = {}     # Data related DRAWING PLAYER IMAGE
        self.PYGAME_BOARD = {11: 1, 21: 2, 31: 3, 41: 4, 51: 5, 12: 6, 22: 7, 32: 8, 42: 9, 52: 10, 13: 11, 23: 12, 33: 13, 43: 14, 53: 15, 14: 16, 24: 17, 34: 18, 44: 19, 54: 20, 15: 21, 25: 22, 35: 23, 45: 24, 55: 25}

        # if self.MUSIC == 'ON': self.AUDIO_BGM_Menu.play(-1)
        self.audio()        # Play - PLAY_BGM_MENU 
        self.menu()
        self.GAME_MODE_VALUE = self.game_mode()

        self.PLAY_BGM_MENU = False
        self.audio()        # Stop - PLAY_BGM_MENU


    def audio(self,PLAY_SEFX_BUTTON_CLICK = False, PLAY_SEFX_XO_INSERT = False, PLAY_SEFX_WIN = False, SOUND_UPDATE = False):

        if (self.SOUND == 'ON' or SOUND_UPDATE):
            print('SOUND')

            if self.SOUND == 'OFF': return None
            if PLAY_SEFX_BUTTON_CLICK: 
                self.AUDIO_SEFX_BUTTON_CLICK.play()
                return None
            if PLAY_SEFX_XO_INSERT: 
                self.AUDIO_SEFX_XO_INSERT.play()
                return None
            if PLAY_SEFX_WIN: 
                self.AUDIO_SEFX_WIN.play()
                return None  
            if SOUND_UPDATE:
                return None

        if self.MUSIC == 'ON'and not any([PLAY_SEFX_BUTTON_CLICK, PLAY_SEFX_XO_INSERT, PLAY_SEFX_WIN]) :
            print("MUSIC")
            
            if self.PLAY_BGM_MENU:   self.AUDIO_BGM_Menu.play(-1)
            else:   self.AUDIO_BGM_Menu.stop()

            if self.PLAY_BGM_Mode_Simple:   self.AUDIO_BGM_Mode_Simple.play(-1)
            else: self.AUDIO_BGM_Mode_Simple.stop()

            if self.PLAY_BGM_Mode_Complex:   self.AUDIO_BGM_Mode_Complex.play(-1)
            else: self.AUDIO_BGM_Mode_Complex.stop()
            
        if self.MUSIC == 'OFF':
            self.AUDIO_BGM_Menu.stop()
            self.AUDIO_BGM_Mode_Simple.stop()
            self.AUDIO_BGM_Mode_Complex.stop()


    def border(self, border_type, time = 1, border_value = False): # BORDERS
        
        GAME_BORDER_SEP_THICK = 5                # Game Border Seperator Thickness
        BORDER = pygame.Rect((3*self.WIDTH)//4, 0, 2, self.HEIGTH)        # (x - 3/4th of WIDTH, y - 0 )
    
        GAME_BORDER = pygame.Rect(BORDER.x//4, self.HEIGTH//8, self.HEIGTH - (self.HEIGTH//4), self.HEIGTH - (self.HEIGTH//4) )      # (x - 1/4th of BORDER.x, y - 1/8th of WINDOW)
        
        GAME_BORDER_SEP_VER = pygame.Rect(GAME_BORDER.x + (time*GAME_BORDER.width)//5, GAME_BORDER.y , GAME_BORDER_SEP_THICK, GAME_BORDER.height)
        GAME_BORDER_SEP_HORI = pygame.Rect(GAME_BORDER.x, GAME_BORDER.y + (time*GAME_BORDER.height)//5 , GAME_BORDER.width, GAME_BORDER_SEP_THICK)
        
        GAME_BORDER_UP = pygame.Rect(GAME_BORDER.x, GAME_BORDER.y, GAME_BORDER.width, GAME_BORDER_SEP_THICK)
        GAME_BORDER_LEFT = pygame.Rect(GAME_BORDER.x, GAME_BORDER.y, GAME_BORDER_SEP_THICK, GAME_BORDER.width)
        GAME_BORDER_DOWN = pygame.Rect(GAME_BORDER.x, GAME_BORDER.y + GAME_BORDER.height - GAME_BORDER_SEP_THICK, GAME_BORDER.width, GAME_BORDER_SEP_THICK)
        GAME_BORDER_RIGHT = pygame.Rect(GAME_BORDER.x + GAME_BORDER.width - GAME_BORDER_SEP_THICK, GAME_BORDER.y, GAME_BORDER_SEP_THICK, GAME_BORDER.height)
        
        if border_value == True:        # For Returning Values
            if border_type == 'BORDER':
                return BORDER

            elif border_type == 'GAME_BORDER':
                return GAME_BORDER

            elif border_type == 'GAME_BORDER_SEP_VER':
                return GAME_BORDER_SEP_VER

            elif border_type == 'GAME_BORDER_SEP_HORI':
                return GAME_BORDER_SEP_HORI

            elif border_type == 'GAME_BORDER_SEP_THICK':
                return GAME_BORDER_SEP_THICK
            
            elif border_type == 'GAME_BORDER_EACH_DIMENSIION':
                VALUE = (GAME_BORDER.width/5) - GAME_BORDER_SEP_THICK
                GAME_BORDER_EACH_DIMENSIION = (VALUE, VALUE)
                return GAME_BORDER_EACH_DIMENSIION
        
        # For Drawing
        if border_type == 'BORDER':
            return BORDER

        elif border_type == 'GAME_BORDER':
            return GAME_BORDER

        elif border_type == 'GAME_BORDER_SEP_VER':      # Vertical Border
            if time <= 4:
                pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, GAME_BORDER_SEP_VER)
                self.border('GAME_BORDER_SEP_VER', time+1)

        elif border_type == 'GAME_BORDER_SEP_HORI':     # Horizontal Border
            if time <= 4:
                pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, GAME_BORDER_SEP_HORI)
                self.border('GAME_BORDER_SEP_HORI', time+1)

        elif border_type == 'GAME_BORDER_UP':
            return GAME_BORDER_UP

        elif border_type == 'GAME_BORDER_LEFT':
            return GAME_BORDER_LEFT

        elif border_type == 'GAME_BORDER_DOWN':
            return GAME_BORDER_DOWN

        elif border_type == 'GAME_BORDER_RIGHT':
            return GAME_BORDER_RIGHT


    def mouse_input(self, MOUSE_INPUT_TYPE):
        MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
        if MOUSE_INPUT_TYPE == 'MOUSE POSITION':
            return MOUSE_POSITION
        
        if MOUSE_INPUT_TYPE == 'MOUSE PRESSED':
            LEFT_KEY_PRESSED, MIDDLE_KEY_PRESSED, RIGHT_KEY_PRESSED = pygame.mouse.get_pressed()
            return LEFT_KEY_PRESSED

        if MOUSE_INPUT_TYPE == 'GET BLOCK':
            GAME_BORDER_SEP_THICK =self. border('GAME_BORDER_SEP_THICK', border_value = True)
            GAME_BORDER_EDGE_VALUES = []
            for time_VER in range(6) :
                GAME_BORDER_SEP_VER = self.border('GAME_BORDER_SEP_VER', time_VER, True)
                X_CORRDINATE = GAME_BORDER_SEP_VER.x + GAME_BORDER_SEP_THICK      # X Corrinate of GAME_BORDER_SEP END
                
                for time_HORI in range(6):
                    GAME_BORDER_SEP_HORI = self.border('GAME_BORDER_SEP_HORI', time_HORI, True)
                    Y_CORRDINATE = GAME_BORDER_SEP_HORI.y + GAME_BORDER_SEP_THICK      # Y Corrinate of GAME_BORDER_SEP END
                    VALUE_XY = (X_CORRDINATE, Y_CORRDINATE)
                    GAME_BORDER_EDGE_VALUES.append(VALUE_XY)
                
            if MOUSE_POSITION[0] > GAME_BORDER_EDGE_VALUES[0][0] and MOUSE_POSITION[0] < GAME_BORDER_EDGE_VALUES[-1][0] - 2*GAME_BORDER_SEP_THICK and MOUSE_POSITION[1] > GAME_BORDER_EDGE_VALUES[0][1] and MOUSE_POSITION[1] < GAME_BORDER_EDGE_VALUES[-1][1] - 2*GAME_BORDER_SEP_THICK :      # x > START x POSITION, x < END x POSITION, y > START y POSITION, y < END y POSITION   
                
                MOUSE_Y_CORRDINATE = None
                MOUSE_X_CORRDINATE = None

                for row_count in range(1,6):            # Checking the X Corrdinate of Player belongs to which X block
                    if MOUSE_POSITION[0] < GAME_BORDER_EDGE_VALUES[6 * row_count][0] - GAME_BORDER_SEP_THICK and MOUSE_POSITION[0] > GAME_BORDER_EDGE_VALUES[6 * (row_count-1)][0]:
                            MOUSE_X_CORRDINATE = row_count
                            break

                for column_count in range(1,6):         # Checking the Y Corrdinate of Player belongs to which Y block
                    if MOUSE_POSITION[1] < GAME_BORDER_EDGE_VALUES[column_count][1] - GAME_BORDER_SEP_THICK and MOUSE_POSITION[1] > GAME_BORDER_EDGE_VALUES[column_count-1][1]:
                            MOUSE_Y_CORRDINATE = column_count
                            break

                for X_CORRDINATE in range(1,6):
                    if MOUSE_X_CORRDINATE == X_CORRDINATE:
                        for Y_CORRIDATE in range(1,6):
                            if MOUSE_Y_CORRDINATE == Y_CORRIDATE:
                                
                                BLOCK_X_CORRIDATE = GAME_BORDER_EDGE_VALUES[6 * (MOUSE_X_CORRDINATE-1)][0]       # Corridate of Block for drawing the input IMAGE
                                BLOCK_Y_CORRIDATE = GAME_BORDER_EDGE_VALUES[MOUSE_Y_CORRDINATE-1][1]
                                POSITION_BLOCK_CORRIDATE = (BLOCK_X_CORRIDATE,BLOCK_Y_CORRIDATE)
                                Final_Position = int(str(X_CORRDINATE)+str(Y_CORRIDATE))

                                return(Final_Position, POSITION_BLOCK_CORRIDATE)

            pygame.display.update()


    def draw_WIN(self, DRAW_PLAYER_IMAGE = (False, None, None), DRAW_EXIT_WIN = False, DRAW_RESTART_WIN = False, DRAW_MENU = False, DRAW_MENU_SETTINGS = False, DRAW_CREDITS = False, DRAW_GAME_MODE = False, DRAW_GAME_MODE_SPECIAL = False, DRAW_RESULT=(False, None), DRAW_RESTART_BOX = {'DRAW': False, 'RETURN_VALUE': False}, DRAW_PLAYER_MOVE_BOX = {'DRAW': False, 'RETURN_VALUE': False}, DRAW_GRAVITY_BOX =  {'DRAW': False, 'RETURN_VALUE': False}, DRAW_CREDITS_BOX =  {'DRAW': False, 'RETURN_VALUE': False}) :
        # self.WIN.fill(self.BLACK)     # Drawing Window
        if DRAW_EXIT_WIN:
            self.WIN.blit(self.BACKGROUND_GAME_MODE, (0,0))

            EXIT_BOX_TEXT = self.FONT_EXIT_BOX.render('Are  You  Sure  Want  To  Exit  The  Game ?', 1, self.WHITE)
            EXIT_BOX_X_CORRIDINATE = (self.WIDTH - EXIT_BOX_TEXT.get_width())/2      
            EXIT_BOX_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)
            EXIT_BOX_X_CORRIDINATE_SPECIAL = EXIT_BOX_X_CORRIDINATE + EXIT_BOX_TEXT.get_width()     

            EXIT_BOX_EXIT_TEXT = self.FONT_EXIT_BOX_OPTONS.render(' EXIT ', 1, self.WHITE)
            EXIT_BOX_STAY_TEXT = self.FONT_EXIT_BOX_OPTONS.render(' STAY ',1 ,self.WHITE)   
            
            EXIT_BOX_EXIT_X_CORRIDINATE = EXIT_BOX_X_CORRIDINATE + 200      # 200 is the distance between initial point and EXIT BOX
            EXIT_BOX_EXIT_Y_CORRIDINATE = EXIT_BOX_Y_CORRIDINATE + EXIT_BOX_TEXT.get_height() + 50   # 50 is distance between Them
            EXIT_BOX_EXIT = pygame.Rect(EXIT_BOX_EXIT_X_CORRIDINATE, EXIT_BOX_EXIT_Y_CORRIDINATE, EXIT_BOX_EXIT_TEXT.get_width(), EXIT_BOX_EXIT_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.RED, EXIT_BOX_EXIT)   

            EXIT_BOX_STAY_X_CORRIDINATE = EXIT_BOX_X_CORRIDINATE_SPECIAL - EXIT_BOX_STAY_TEXT.get_width() - 200    # 200 is the distance between EXIT and STAY Box
            EXIT_BOX_STAY_Y_CORRIDINATE = EXIT_BOX_EXIT_Y_CORRIDINATE
            EXIT_BOX_STAY = pygame.Rect(EXIT_BOX_STAY_X_CORRIDINATE, EXIT_BOX_STAY_Y_CORRIDINATE, EXIT_BOX_STAY_TEXT.get_width(), EXIT_BOX_STAY_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.GREEN, EXIT_BOX_STAY)

            self.WIN.blit(EXIT_BOX_TEXT, (EXIT_BOX_X_CORRIDINATE, EXIT_BOX_Y_CORRIDINATE)) 
            self.WIN.blit(EXIT_BOX_EXIT_TEXT,(EXIT_BOX_EXIT_X_CORRIDINATE, EXIT_BOX_EXIT_Y_CORRIDINATE)) 
            self.WIN.blit(EXIT_BOX_STAY_TEXT, (EXIT_BOX_STAY_X_CORRIDINATE, EXIT_BOX_STAY_Y_CORRIDINATE)) 
            
            pygame.display.update()
            
            EXIT_BOX_EXIT_DETAILS = {'x':EXIT_BOX_EXIT.x, 'y':EXIT_BOX_EXIT.y, 'width':EXIT_BOX_EXIT.width, 'height':EXIT_BOX_EXIT.height}
            EXIT_BOX_STAY_DETAILS = {'x':EXIT_BOX_STAY.x, 'y':EXIT_BOX_STAY.y, 'width':EXIT_BOX_STAY.width, 'height':EXIT_BOX_STAY.height}

            return (EXIT_BOX_EXIT_DETAILS, EXIT_BOX_STAY_DETAILS)
        
        if DRAW_RESTART_WIN:
            self.WIN.blit(self.BACKGROUND_GAME_MODE, (0,0))

            RESTART_TEXT = self.FONT_RESTART_WIN.render('Are  You  Sure  Want  To  Restart The  Game ?', 1, self.WHITE)
            RESTART_X_CORRIDINATE = (self.WIDTH - RESTART_TEXT.get_width())/2      
            RESTART_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)
            RESTART_X_CORRIDINATE_SPECIAL = RESTART_X_CORRIDINATE + RESTART_TEXT.get_width()     

            RESTART_NO_TEXT = self.FONT_RESTART_WIN_OPTIONS.render(' NO ', 1, self.WHITE)
            RESTART_YES_TEXT = self.FONT_RESTART_WIN_OPTIONS.render(' YES ',1 ,self.WHITE)   
            
            RESTART_NO_X_CORRIDINATE = RESTART_X_CORRIDINATE + 200      
            RESTART_NO_Y_CORRIDINATE = RESTART_Y_CORRIDINATE + RESTART_TEXT.get_height() + 50   # 50 is distance between Them
            RESTART_NO_BOX = pygame.Rect(RESTART_NO_X_CORRIDINATE, RESTART_NO_Y_CORRIDINATE, RESTART_NO_TEXT.get_width(), RESTART_NO_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.RED, RESTART_NO_BOX)   

            RESTART_YES_X_CORRIDINATE = RESTART_X_CORRIDINATE_SPECIAL - RESTART_YES_TEXT.get_width() - 200    
            RESTART_YES_Y_CORRIDINATE = RESTART_NO_Y_CORRIDINATE
            RESTART_YES_BOX = pygame.Rect(RESTART_YES_X_CORRIDINATE, RESTART_YES_Y_CORRIDINATE, RESTART_YES_TEXT.get_width(), RESTART_YES_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.GREEN, RESTART_YES_BOX)

            self.WIN.blit(RESTART_TEXT, (RESTART_X_CORRIDINATE, RESTART_Y_CORRIDINATE)) 
            self.WIN.blit(RESTART_NO_TEXT,(RESTART_NO_X_CORRIDINATE, RESTART_NO_Y_CORRIDINATE)) 
            self.WIN.blit(RESTART_YES_TEXT, (RESTART_YES_X_CORRIDINATE, RESTART_YES_Y_CORRIDINATE)) 
            
            pygame.display.update()
            
            RESTART_NO_DETAILS = {'x':RESTART_NO_BOX.x, 'y':RESTART_NO_BOX.y, 'width':RESTART_NO_BOX.width, 'height':RESTART_NO_BOX.height}
            RESTART_YES_DETAILS = {'x':RESTART_YES_BOX.x, 'y':RESTART_YES_BOX.y, 'width':RESTART_YES_BOX.width, 'height':RESTART_YES_BOX.height}

            return (RESTART_NO_DETAILS, RESTART_YES_DETAILS)

        if DRAW_MENU:
            if self.THEME == 'NEON':
                self.WIN.blit(self.BACKGROUND_MENU_NEON, (0,0))
            else:
                self.WIN.blit(self.BACKGROUND_MENU_DARK, (0,0))


            MENU_CONNECT_4_TEXT = self.FONT_MENU_CONNECT_4.render('CONNECT 4',1, self.YELLOW)
            MENU_CONNECT_4_X_CORRIDINATE = (self.WIDTH - MENU_CONNECT_4_TEXT.get_width())/2   
            MENU_CONNECT_4_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)

            MENU_PLAY_TEXT = self.FONT_MENU_OPTIONS.render(' PLAY ', 1, self.BLUE)
            MENU_PLAY_X_CORRIDINATE = MENU_CONNECT_4_X_CORRIDINATE + ( MENU_CONNECT_4_TEXT.get_width() - MENU_PLAY_TEXT.get_width() ) /2
            MENU_PLAY_Y_CORRIDINATE = MENU_CONNECT_4_Y_CORRIDINATE + MENU_PLAY_TEXT.get_height() + 50
            MENU_PLAY_BOX = pygame.Rect(MENU_PLAY_X_CORRIDINATE, MENU_PLAY_Y_CORRIDINATE, MENU_PLAY_TEXT.get_width(), MENU_PLAY_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_PLAY_BOX)

            MENU_SETTINGS_TEXT = self.FONT_MENU_OPTIONS.render(' SETTINGS ', 1, self.BLUE)
            MENU_SETTINGS_X_CORRIDINATE = MENU_CONNECT_4_X_CORRIDINATE + ( MENU_CONNECT_4_TEXT.get_width() - MENU_SETTINGS_TEXT.get_width() ) /2
            MENU_SETTINGS_Y_CORRIDINATE = MENU_PLAY_Y_CORRIDINATE + MENU_SETTINGS_TEXT.get_height() + 25
            MENU_SETTINGS_BOX = pygame.Rect(MENU_SETTINGS_X_CORRIDINATE, MENU_SETTINGS_Y_CORRIDINATE, MENU_SETTINGS_TEXT.get_width(), MENU_SETTINGS_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_SETTINGS_BOX)

            MENU_CREDITS_TEXT = self.FONT_MENU_OPTIONS.render(' CREDITS ', 1, self.BLUE)
            MENU_CREDITS_X_CORRIDINATE = MENU_CONNECT_4_X_CORRIDINATE + ( MENU_CONNECT_4_TEXT.get_width() - MENU_CREDITS_TEXT.get_width() ) /2
            MENU_CREDITS_Y_CORRIDINATE = MENU_SETTINGS_Y_CORRIDINATE + MENU_CREDITS_TEXT.get_height() + 25
            MENU_CREDITS_BOX = pygame.Rect(MENU_CREDITS_X_CORRIDINATE, MENU_CREDITS_Y_CORRIDINATE, MENU_CREDITS_TEXT.get_width(), MENU_CREDITS_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_CREDITS_BOX)  

            MENU_LOGO_X_CORRIDINATE = (self.WIDTH - self.LOGO_HIDDEN_BLADE.get_width())/2   
            MENU_LOGO_Y_CORRIDINATE = MENU_CONNECT_4_Y_CORRIDINATE - MENU_CONNECT_4_TEXT.get_height() - 50

            self.WIN.blit(self.LOGO_HIDDEN_BLADE, (MENU_LOGO_X_CORRIDINATE, MENU_LOGO_Y_CORRIDINATE))            
            self.WIN.blit(MENU_CONNECT_4_TEXT, (MENU_CONNECT_4_X_CORRIDINATE, MENU_CONNECT_4_Y_CORRIDINATE))
            self.WIN.blit(MENU_PLAY_TEXT, (MENU_PLAY_X_CORRIDINATE, MENU_PLAY_Y_CORRIDINATE))
            self.WIN.blit(MENU_SETTINGS_TEXT, (MENU_SETTINGS_X_CORRIDINATE, MENU_SETTINGS_Y_CORRIDINATE))
            self.WIN.blit(MENU_CREDITS_TEXT, (MENU_CREDITS_X_CORRIDINATE, MENU_CREDITS_Y_CORRIDINATE))


            pygame.display.update()
            
            MENU_PLAY_DETAILS = {'x':MENU_PLAY_BOX.x, 'y':MENU_PLAY_BOX.y, 'width':MENU_PLAY_BOX.width, 'height':MENU_PLAY_BOX.height}
            MENU_SETTINGS_DETAILS = {'x':MENU_SETTINGS_BOX.x, 'y':MENU_SETTINGS_BOX.y, 'width':MENU_SETTINGS_BOX.width, 'height':MENU_SETTINGS_BOX.height}
            MENU_CREDITS_DETAILS = {'x':MENU_CREDITS_BOX.x, 'y':MENU_CREDITS_BOX.y, 'width':MENU_CREDITS_BOX.width, 'height':MENU_CREDITS_BOX.height}

            return (MENU_PLAY_DETAILS, MENU_SETTINGS_DETAILS, MENU_CREDITS_DETAILS)

        if DRAW_MENU_SETTINGS:
            if self.THEME == 'NEON':
                self.WIN.blit(self.BACKGROUND_MENU_NEON, (0,0))
            else:
                self.WIN.blit(self.BACKGROUND_MENU_DARK, (0,0))

            MENU_SETTINGS_TEXT = self.FONT_MENU_SETTINGS.render('SETTINGS',1, self.YELLOW)
            MENU_SETTINGS_X_CORRIDINATE = (self.WIDTH - MENU_SETTINGS_TEXT.get_width())/2   
            MENU_SETTINGS_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)

            MENU_SETTINGS_THEME_TEXT = self.FONT_MENU_SETTINGS_OPTIONS.render(' THEME ', 1, self.BLUE)
            MENU_SETTINGS_THEME_X_CORRIDINATE = MENU_SETTINGS_X_CORRIDINATE + ( MENU_SETTINGS_TEXT.get_width() - MENU_SETTINGS_THEME_TEXT.get_width() ) /2
            MENU_SETTINGS_THEME_Y_CORRIDINATE = MENU_SETTINGS_Y_CORRIDINATE + MENU_SETTINGS_TEXT.get_height() + 50
            MENU_SETTINGS_THEME_BOX = pygame.Rect(MENU_SETTINGS_THEME_X_CORRIDINATE, MENU_SETTINGS_THEME_Y_CORRIDINATE, MENU_SETTINGS_THEME_TEXT.get_width(), MENU_SETTINGS_THEME_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_SETTINGS_THEME_BOX)

            MENU_SETTINGS_MUSIC_TEXT = self.FONT_MENU_SETTINGS_OPTIONS.render(' MUSIC ', 1, self.BLUE)
            MENU_SETTINGS_MUSIC_X_CORRIDINATE = MENU_SETTINGS_X_CORRIDINATE + ( MENU_SETTINGS_TEXT.get_width() - MENU_SETTINGS_MUSIC_TEXT.get_width() ) /2
            MENU_SETTINGS_MUSIC_Y_CORRIDINATE = MENU_SETTINGS_THEME_Y_CORRIDINATE + MENU_SETTINGS_THEME_TEXT.get_height() + 25
            MENU_SETTINGS_MUSIC_BOX = pygame.Rect(MENU_SETTINGS_MUSIC_X_CORRIDINATE, MENU_SETTINGS_MUSIC_Y_CORRIDINATE, MENU_SETTINGS_MUSIC_TEXT.get_width(), MENU_SETTINGS_MUSIC_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_SETTINGS_MUSIC_BOX)

            MENU_SETTINGS_SOUND_EFFECTS_TEXT = self.FONT_MENU_SETTINGS_OPTIONS.render(' SOUND EFFECTS ', 1, self.BLUE)
            MENU_SETTINGS_SOUND_EFFECTS_X_CORRIDINATE = MENU_SETTINGS_X_CORRIDINATE + ( MENU_SETTINGS_TEXT.get_width() - MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_width() ) /2
            MENU_SETTINGS_SOUND_EFFECTS_Y_CORRIDINATE = MENU_SETTINGS_MUSIC_Y_CORRIDINATE + MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height() + 25
            MENU_SETTINGS_SOUND_EFFECTS_BOX = pygame.Rect(MENU_SETTINGS_SOUND_EFFECTS_X_CORRIDINATE, MENU_SETTINGS_SOUND_EFFECTS_Y_CORRIDINATE, MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_width(), MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_SETTINGS_SOUND_EFFECTS_BOX)

            MENU_SETTINGS_BACK_TEXT = self.FONT_MENU_SETTINGS_OPTIONS.render(' BACK ', 1, self.BLUE)
            MENU_SETTINGS_BACK_X_CORRIDINATE = 50
            MENU_SETTINGS_BACK_Y_CORRIDINATE = self.HEIGTH - MENU_SETTINGS_BACK_TEXT.get_height() - 50
            MENU_SETTINGS_BACK_BOX = pygame.Rect(MENU_SETTINGS_BACK_X_CORRIDINATE, MENU_SETTINGS_BACK_Y_CORRIDINATE, MENU_SETTINGS_BACK_TEXT.get_width(), MENU_SETTINGS_BACK_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, MENU_SETTINGS_BACK_BOX)  

            #ICONS
            ICONS_IMG_THEME_NEON = pygame.transform.scale(self.IMPORT_ICONS_THEME_NEON, (MENU_SETTINGS_THEME_TEXT.get_height(), MENU_SETTINGS_THEME_TEXT.get_height()))
            ICONS_IMG_THEME_DARK = pygame.transform.scale(self.IMPORT_ICONS_THEME_DARK, (MENU_SETTINGS_THEME_TEXT.get_height(), MENU_SETTINGS_THEME_TEXT.get_height()))
            ICONS_IMG_MUSIC_ON = pygame.transform.scale(self.IMPORT_ICONS_MUSIC_ON, (MENU_SETTINGS_MUSIC_TEXT.get_height(), MENU_SETTINGS_MUSIC_TEXT.get_height()))
            ICONS_IMG_MUSIC_OFF = pygame.transform.scale(self.IMPORT_ICONS_MUSIC_OFF, (MENU_SETTINGS_MUSIC_TEXT.get_height(), MENU_SETTINGS_MUSIC_TEXT.get_height()))
            ICONS_IMG_SOUND_ON = pygame.transform.scale(self.IMPORT_ICONS_SOUND_ON, (MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height(), MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height()))
            ICONS_IMG_SOUND_OFF = pygame.transform.scale(self.IMPORT_ICONS_SOUND_OFF, (MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height(), MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_height()))
            

            MENU_SETTINGS_IMG_THEME_X_CORRIDINATE = MENU_SETTINGS_THEME_BOX.x + MENU_SETTINGS_THEME_TEXT.get_width() + 10
            MENU_SETTINGS_IMG_THEME_Y_CORRIDINATE = MENU_SETTINGS_THEME_BOX.y
            MENU_SETTINGS_IMG_THEME_BOX = pygame.Rect(MENU_SETTINGS_IMG_THEME_X_CORRIDINATE, MENU_SETTINGS_IMG_THEME_Y_CORRIDINATE, ICONS_IMG_THEME_NEON.get_width(), ICONS_IMG_THEME_NEON.get_height())
            pygame.draw.rect(self.WIN, self.BLUE, MENU_SETTINGS_IMG_THEME_BOX)

            MENU_SETTINGS_IMG_MUSIC_X_CORRIDINATE = MENU_SETTINGS_MUSIC_BOX.x + MENU_SETTINGS_MUSIC_TEXT.get_width() + 10
            MENU_SETTINGS_IMG_MUSIC_Y_CORRIDINATE = MENU_SETTINGS_MUSIC_BOX.y
            MENU_SETTINGS_IMG_MUSIC_BOX = pygame.Rect(MENU_SETTINGS_IMG_MUSIC_X_CORRIDINATE, MENU_SETTINGS_IMG_MUSIC_Y_CORRIDINATE, ICONS_IMG_MUSIC_ON.get_width(), ICONS_IMG_MUSIC_ON.get_height())
            pygame.draw.rect(self.WIN, self.BLUE, MENU_SETTINGS_IMG_MUSIC_BOX)

            MENU_SETTINGS_IMG_SOUND_X_CORRIDINATE = MENU_SETTINGS_SOUND_EFFECTS_BOX.x + MENU_SETTINGS_SOUND_EFFECTS_TEXT.get_width() + 10
            MENU_SETTINGS_IMG_SOUND_Y_CORRIDINATE = MENU_SETTINGS_SOUND_EFFECTS_BOX.y
            MENU_SETTINGS_IMG_SOUND_BOX = pygame.Rect(MENU_SETTINGS_IMG_SOUND_X_CORRIDINATE, MENU_SETTINGS_IMG_SOUND_Y_CORRIDINATE, ICONS_IMG_SOUND_ON.get_width(), ICONS_IMG_SOUND_ON.get_height())
            pygame.draw.rect(self.WIN, self.BLUE, MENU_SETTINGS_IMG_SOUND_BOX)
             
            self.WIN.blit(MENU_SETTINGS_TEXT, (MENU_SETTINGS_X_CORRIDINATE, MENU_SETTINGS_Y_CORRIDINATE))
            self.WIN.blit(MENU_SETTINGS_THEME_TEXT, (MENU_SETTINGS_THEME_X_CORRIDINATE, MENU_SETTINGS_THEME_Y_CORRIDINATE))
            self.WIN.blit(MENU_SETTINGS_MUSIC_TEXT, (MENU_SETTINGS_MUSIC_X_CORRIDINATE, MENU_SETTINGS_MUSIC_Y_CORRIDINATE))
            self.WIN.blit(MENU_SETTINGS_SOUND_EFFECTS_TEXT, (MENU_SETTINGS_SOUND_EFFECTS_X_CORRIDINATE, MENU_SETTINGS_SOUND_EFFECTS_Y_CORRIDINATE))
            self.WIN.blit(MENU_SETTINGS_BACK_TEXT, (MENU_SETTINGS_BACK_X_CORRIDINATE, MENU_SETTINGS_BACK_Y_CORRIDINATE))

            if self.THEME == 'NEON':    
                self.WIN.blit(ICONS_IMG_THEME_NEON, (MENU_SETTINGS_IMG_THEME_X_CORRIDINATE, MENU_SETTINGS_IMG_THEME_Y_CORRIDINATE))
            else:   
                self.WIN.blit(ICONS_IMG_THEME_DARK, (MENU_SETTINGS_IMG_THEME_X_CORRIDINATE, MENU_SETTINGS_IMG_THEME_Y_CORRIDINATE))
             
            if self.MUSIC == 'ON':    
                self.WIN.blit(ICONS_IMG_MUSIC_ON, (MENU_SETTINGS_IMG_MUSIC_X_CORRIDINATE, MENU_SETTINGS_IMG_MUSIC_Y_CORRIDINATE))
            else:   
                self.WIN.blit(ICONS_IMG_MUSIC_OFF, (MENU_SETTINGS_IMG_MUSIC_X_CORRIDINATE, MENU_SETTINGS_IMG_MUSIC_Y_CORRIDINATE))
            
            if self.SOUND == 'ON':    
                self.WIN.blit(ICONS_IMG_SOUND_ON, (MENU_SETTINGS_IMG_SOUND_X_CORRIDINATE, MENU_SETTINGS_IMG_SOUND_Y_CORRIDINATE))
            else:   
                self.WIN.blit(ICONS_IMG_SOUND_OFF, (MENU_SETTINGS_IMG_SOUND_X_CORRIDINATE, MENU_SETTINGS_IMG_SOUND_Y_CORRIDINATE))

            pygame.display.update()
            
        
            MENU_SETTINGS_THEME_DETAILS = {'x':MENU_SETTINGS_IMG_THEME_BOX.x, 'y':MENU_SETTINGS_IMG_THEME_BOX.y, 'width':MENU_SETTINGS_IMG_THEME_BOX.width, 'height':MENU_SETTINGS_IMG_THEME_BOX.height}
            MENU_SETTINGS_MUSIC_DETAILS = {'x':MENU_SETTINGS_IMG_MUSIC_BOX.x, 'y':MENU_SETTINGS_IMG_MUSIC_BOX.y, 'width':MENU_SETTINGS_IMG_MUSIC_BOX.width, 'height':MENU_SETTINGS_IMG_MUSIC_BOX.height}
            MENU_SETTINGS_SOUND_DETAILS = {'x':MENU_SETTINGS_IMG_SOUND_BOX.x, 'y':MENU_SETTINGS_SOUND_EFFECTS_BOX.y, 'width':MENU_SETTINGS_SOUND_EFFECTS_BOX.width, 'height':MENU_SETTINGS_SOUND_EFFECTS_BOX.height}
            MENU_BACK_DETAILS = {'x':MENU_SETTINGS_BACK_BOX.x, 'y':MENU_SETTINGS_BACK_BOX.y, 'width':MENU_SETTINGS_BACK_BOX.width, 'height':MENU_SETTINGS_BACK_BOX.height}
        
            return (MENU_SETTINGS_THEME_DETAILS, MENU_SETTINGS_MUSIC_DETAILS, MENU_SETTINGS_SOUND_DETAILS,MENU_BACK_DETAILS)
            
        if DRAW_CREDITS:
            if self.THEME == 'NEON':
                self.WIN.blit(self.BACKGROUND_MENU_NEON, (0,0))
            else:
                self.WIN.blit(self.BACKGROUND_MENU_DARK, (0,0))

            CREDITS_BACK_TEXT = self.FONT_MENU_SETTINGS_OPTIONS.render(' BACK ', 1, self.BLUE)
            CREDITS_BACK_X_CORRIDINATE = 50
            CREDITS_BACK_Y_CORRIDINATE = self.HEIGTH - CREDITS_BACK_TEXT.get_height() - 50
            CREDITS_BACK_BOX = pygame.Rect(CREDITS_BACK_X_CORRIDINATE, CREDITS_BACK_Y_CORRIDINATE, CREDITS_BACK_TEXT.get_width(), CREDITS_BACK_TEXT.get_height())

            CREDITS_IMG_X_CORRIDINATE = 0  
            CREDITS_IMG_Y_CORRIDINATE = 0  


            self.WIN.blit(self.IMG_CREDITS, (CREDITS_IMG_X_CORRIDINATE, CREDITS_IMG_Y_CORRIDINATE))      
            pygame.draw.rect(self.WIN, self.YELLOW, CREDITS_BACK_BOX) 

            self.WIN.blit(CREDITS_BACK_TEXT, (CREDITS_BACK_X_CORRIDINATE, CREDITS_BACK_Y_CORRIDINATE))
            pygame.display.update()

            MENU_BACK_DETAILS = {'x':CREDITS_BACK_BOX.x, 'y':CREDITS_BACK_BOX.y, 'width':CREDITS_BACK_BOX.width, 'height':CREDITS_BACK_BOX.height}

            return MENU_BACK_DETAILS


        if DRAW_GAME_MODE:
            self.WIN.blit(self.BACKGROUND_GAME_MODE, (0,0))

            GAME_MODE_TEXT = self.FONT_GAME_MODE.render('SELECT  THE  GAME  MODE',1, self.YELLOW)
            GAME_MODE_X_CORRIDINATE = (self.WIDTH - GAME_MODE_TEXT.get_width())/2   
            GAME_MODE_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)

            GAME_MODE_SIMPLE_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' SIMPLE ', 1, self.BLUE)
            GAME_MODE_SIMPLE_X_CORRIDINATE = GAME_MODE_X_CORRIDINATE
            GAME_MODE_SIMPLE_Y_CORRIDINATE = GAME_MODE_Y_CORRIDINATE + GAME_MODE_TEXT.get_height() + 50
            GAME_MODE_SIMPLE_BOX = pygame.Rect(GAME_MODE_SIMPLE_X_CORRIDINATE, GAME_MODE_SIMPLE_Y_CORRIDINATE, GAME_MODE_SIMPLE_TEXT.get_width(), GAME_MODE_SIMPLE_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_SIMPLE_BOX)  

            GAME_MODE_COMPLEX_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' COMPLEX ', 1, self.BLUE)
            GAME_MODE_COMPLEX_X_CORRIDINATE = GAME_MODE_X_CORRIDINATE + GAME_MODE_TEXT.get_width() - GAME_MODE_COMPLEX_TEXT.get_width()
            GAME_MODE_COMPLEX_Y_CORRIDINATE = GAME_MODE_SIMPLE_Y_CORRIDINATE
            GAME_MODE_COMPLEX_BOX = pygame.Rect(GAME_MODE_COMPLEX_X_CORRIDINATE, GAME_MODE_COMPLEX_Y_CORRIDINATE, GAME_MODE_COMPLEX_TEXT.get_width(), GAME_MODE_COMPLEX_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_COMPLEX_BOX)         

            self.WIN.blit(GAME_MODE_TEXT, (GAME_MODE_X_CORRIDINATE, GAME_MODE_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_SIMPLE_TEXT, (GAME_MODE_SIMPLE_X_CORRIDINATE, GAME_MODE_SIMPLE_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_COMPLEX_TEXT, (GAME_MODE_COMPLEX_X_CORRIDINATE, GAME_MODE_COMPLEX_Y_CORRIDINATE))

            pygame.display.update()
            
            GAME_MODE_SIMPLE_DETAILS = {'x':GAME_MODE_SIMPLE_BOX.x, 'y':GAME_MODE_SIMPLE_BOX.y, 'width':GAME_MODE_SIMPLE_BOX.width, 'height':GAME_MODE_SIMPLE_BOX.height}
            GAME_MODE_COMPLEX_DETAILS = {'x':GAME_MODE_COMPLEX_BOX.x, 'y':GAME_MODE_COMPLEX_BOX.y, 'width':GAME_MODE_COMPLEX_BOX.width, 'height':GAME_MODE_COMPLEX_BOX.height}

            return (GAME_MODE_SIMPLE_DETAILS, GAME_MODE_COMPLEX_DETAILS)
        
        if DRAW_GAME_MODE_SPECIAL:
            self.WIN.blit(self.BACKGROUND_GAME_MODE, (0,0))

            GAME_MODE_SPECIAL_TEXT = self.FONT_GAME_MODE.render("Select The Gravity Region",1, self.YELLOW) 
            GAME_MODE_SPECIAL_X_CORRIDINATE = (self.WIDTH - GAME_MODE_SPECIAL_TEXT.get_width())/2      
            GAME_MODE_SPECIAL_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)

            GAME_MODE_UP_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' UP ', 1, self.BLUE)
            GAME_MODE_LEFT_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' LEFT ', 1, self.BLUE)
            GAME_MODE_DOWN_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' DOWN ', 1, self.BLUE)
            GAME_MODE_RIGHT_TEXT = self.FONT_GAME_MODE_OPTIONS.render(' RIGHT ', 1, self.BLUE)

            GAP =  (GAME_MODE_SPECIAL_TEXT.get_width() - (GAME_MODE_UP_TEXT.get_width() + GAME_MODE_LEFT_TEXT.get_width() + GAME_MODE_DOWN_TEXT.get_width() + GAME_MODE_RIGHT_TEXT.get_width()))/3

            GAME_MODE_UP_X_CORRIDINATE = GAME_MODE_SPECIAL_X_CORRIDINATE
            GAME_MODE_UP_Y_CORRIDINATE = GAME_MODE_SPECIAL_Y_CORRIDINATE + GAME_MODE_SPECIAL_TEXT.get_height() + 50
            GAME_MODE_UP_BOX = pygame.Rect(GAME_MODE_UP_X_CORRIDINATE, GAME_MODE_UP_Y_CORRIDINATE, GAME_MODE_UP_TEXT.get_width(), GAME_MODE_UP_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_UP_BOX)

            GAME_MODE_DOWN_X_CORRIDINATE = GAME_MODE_UP_X_CORRIDINATE + GAME_MODE_UP_TEXT.get_width() + GAP
            GAME_MODE_DOWN_Y_CORRIDINATE = GAME_MODE_UP_Y_CORRIDINATE
            GAME_MODE_DOWN_BOX = pygame.Rect(GAME_MODE_DOWN_X_CORRIDINATE, GAME_MODE_DOWN_Y_CORRIDINATE, GAME_MODE_DOWN_TEXT.get_width(), GAME_MODE_DOWN_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_DOWN_BOX)

            GAME_MODE_RIGHT_X_CORRIDINATE = GAME_MODE_DOWN_X_CORRIDINATE + GAME_MODE_DOWN_TEXT.get_width() + GAP
            GAME_MODE_RIGHT_Y_CORRIDINATE = GAME_MODE_DOWN_Y_CORRIDINATE
            GAME_MODE_RIGHT_BOX = pygame.Rect(GAME_MODE_RIGHT_X_CORRIDINATE, GAME_MODE_RIGHT_Y_CORRIDINATE, GAME_MODE_RIGHT_TEXT.get_width(), GAME_MODE_RIGHT_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_RIGHT_BOX)

            GAME_MODE_LEFT_X_CORRIDINATE = GAME_MODE_RIGHT_X_CORRIDINATE + GAME_MODE_RIGHT_TEXT.get_width() + GAP
            GAME_MODE_LEFT_Y_CORRIDINATE = GAME_MODE_UP_Y_CORRIDINATE
            GAME_MODE_LEFT_BOX = pygame.Rect(GAME_MODE_LEFT_X_CORRIDINATE, GAME_MODE_LEFT_Y_CORRIDINATE, GAME_MODE_LEFT_TEXT.get_width(), GAME_MODE_LEFT_TEXT.get_height())
            pygame.draw.rect(self.WIN, self.YELLOW, GAME_MODE_LEFT_BOX)  

            self.WIN.blit(GAME_MODE_SPECIAL_TEXT, (GAME_MODE_SPECIAL_X_CORRIDINATE, GAME_MODE_SPECIAL_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_UP_TEXT, (GAME_MODE_UP_X_CORRIDINATE, GAME_MODE_UP_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_DOWN_TEXT, (GAME_MODE_DOWN_X_CORRIDINATE, GAME_MODE_DOWN_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_RIGHT_TEXT, (GAME_MODE_RIGHT_X_CORRIDINATE, GAME_MODE_RIGHT_Y_CORRIDINATE))
            self.WIN.blit(GAME_MODE_LEFT_TEXT, (GAME_MODE_LEFT_X_CORRIDINATE, GAME_MODE_LEFT_Y_CORRIDINATE))
            
            pygame.display.update()

            GAME_MODE_UP_DETAILS = {'x':GAME_MODE_UP_BOX.x, 'y':GAME_MODE_UP_BOX.y, 'width':GAME_MODE_UP_BOX.width, 'height':GAME_MODE_UP_BOX.h}
            GAME_MODE_DOWN_DETAILS = {'x':GAME_MODE_DOWN_BOX.x, 'y':GAME_MODE_DOWN_BOX.y, 'width':GAME_MODE_DOWN_BOX.width, 'height':GAME_MODE_DOWN_BOX.h}
            GAME_MODE_RIGHT_DETAILS = {'x':GAME_MODE_RIGHT_BOX.x, 'y':GAME_MODE_RIGHT_BOX.y, 'width':GAME_MODE_RIGHT_BOX.width, 'height':GAME_MODE_RIGHT_BOX.h}
            GAME_MODE_LEFT_DETAILS = {'x':GAME_MODE_LEFT_BOX.x, 'y':GAME_MODE_LEFT_BOX.y, 'width':GAME_MODE_LEFT_BOX.width, 'height':GAME_MODE_LEFT_BOX.h}
            

            return (GAME_MODE_UP_DETAILS, GAME_MODE_DOWN_DETAILS, GAME_MODE_RIGHT_DETAILS, GAME_MODE_LEFT_DETAILS)

        if DRAW_RESULT[0]:
            self.WIN.blit(self.BACKGROUND_RESULT, (0,0))
            if DRAW_RESULT[1] == 'DRAW':
                RESULT_TEXT = self.FONT_RESULT.render('      GAME  DRAW !      ', 1, self.WHITE)
            else:
                RESULT_TEXT = self.FONT_RESULT.render(DRAW_RESULT[1]+' WON THE GAME ', 1, self.WHITE)
            RESULT_X_CORRIDINATE = (self.WIDTH - RESULT_TEXT.get_width())/2
            RESULT_Y_CORRIDINATE = (self.HEIGTH/4) + (self.HEIGTH/12)

            RESULT_RESTART_TEXT = self.FONT_RESULT_OPTIONS.render(' RESTART ', 1, self.WHITE)
            RESULT_VIEW_GAME_TEXT = self.FONT_RESULT_OPTIONS.render(' BACK ', 1, self.WHITE)
            RESULT_EXIT_TEXT = self.FONT_RESULT_OPTIONS.render(' EXIT ', 1, self.WHITE)

            GAP = (RESULT_TEXT.get_width() - (RESULT_RESTART_TEXT.get_width() + RESULT_VIEW_GAME_TEXT.get_width() + RESULT_EXIT_TEXT.get_width()))/2

            RESULT_RESTART_X_CORRIDINATE = RESULT_X_CORRIDINATE
            RESULT_RESTART_Y_CORRIDINATE = RESULT_Y_CORRIDINATE + RESULT_TEXT.get_height() + 50
            RESULT_RESTART_BOX = pygame.Rect(RESULT_RESTART_X_CORRIDINATE, RESULT_RESTART_Y_CORRIDINATE, RESULT_RESTART_TEXT.get_width(), RESULT_RESTART_TEXT.get_height()+10)
            pygame.draw.rect(self.WIN, self.GREEN, RESULT_RESTART_BOX)

            RESULT_VIEW_GAME_X_CORRIDINATE = RESULT_RESTART_X_CORRIDINATE + RESULT_RESTART_TEXT.get_width() + GAP
            RESULT_VIEW_GAME_Y_CORRIDINATE = RESULT_RESTART_Y_CORRIDINATE
            RESULT_VIEW_GAME_BOX = pygame.Rect(RESULT_VIEW_GAME_X_CORRIDINATE, RESULT_VIEW_GAME_Y_CORRIDINATE, RESULT_VIEW_GAME_TEXT.get_width(), RESULT_VIEW_GAME_TEXT.get_height()+10)
            pygame.draw.rect(self.WIN, self.BLUE, RESULT_VIEW_GAME_BOX)

            RESULT_EXIT_X_CORRIDINATE = RESULT_VIEW_GAME_X_CORRIDINATE + RESULT_VIEW_GAME_TEXT.get_width() + GAP
            RESULT_EXIT_Y_CORRIDINATE = RESULT_VIEW_GAME_Y_CORRIDINATE
            RESULT_EXIT_BOX = pygame.Rect(RESULT_EXIT_X_CORRIDINATE, RESULT_EXIT_Y_CORRIDINATE, RESULT_EXIT_TEXT.get_width(), RESULT_EXIT_TEXT.get_height()+10)
            pygame.draw.rect(self.WIN, self.RED, RESULT_EXIT_BOX)

            self.WIN.blit(RESULT_TEXT, (RESULT_X_CORRIDINATE, RESULT_Y_CORRIDINATE))
            self.WIN.blit(RESULT_RESTART_TEXT, (RESULT_RESTART_X_CORRIDINATE, RESULT_RESTART_Y_CORRIDINATE))
            self.WIN.blit(RESULT_VIEW_GAME_TEXT, (RESULT_VIEW_GAME_X_CORRIDINATE, RESULT_VIEW_GAME_Y_CORRIDINATE))
            self.WIN.blit(RESULT_EXIT_TEXT, (RESULT_EXIT_X_CORRIDINATE, RESULT_EXIT_Y_CORRIDINATE))

            pygame.display.update()
            RESULT_RESTART_DETAILS = {'x': RESULT_RESTART_BOX.x, 'y': RESULT_RESTART_BOX.y, 'width': RESULT_RESTART_BOX.width, 'height': RESULT_RESTART_BOX.height}
            RESULT_VIEW_GAME_DETAILS = {'x': RESULT_VIEW_GAME_BOX.x, 'y': RESULT_VIEW_GAME_BOX.y, 'width': RESULT_VIEW_GAME_BOX.width, 'height': RESULT_VIEW_GAME_BOX.height}
            RESULT_EXIT_DETAILS = {'x': RESULT_EXIT_BOX.x, 'y': RESULT_EXIT_BOX.y, 'width': RESULT_EXIT_BOX.width, 'height': RESULT_EXIT_BOX.height}
            
            return (RESULT_RESTART_DETAILS, RESULT_VIEW_GAME_DETAILS, RESULT_EXIT_DETAILS)

        if DRAW_RESTART_BOX['DRAW'] or DRAW_RESTART_BOX['RETURN_VALUE']:
            BORDER = self.border('BORDER', border_value = True)
            RESTART_BOX_TEXT = self.FONT_RESTART_BOX.render(" RESTART ", 1, self.WHITE) 

            RESTART_BOX_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Restart Box
            RESTART_BOX_BG_WIDTH = self.WIDTH - RESTART_BOX_BG_X_CORRIDINATE - 20       # 20 is distance between Restart Box and Window End
            RESTART_BOX_X_CORRIDINATE = RESTART_BOX_BG_X_CORRIDINATE + (RESTART_BOX_BG_WIDTH - RESTART_BOX_TEXT.get_width())/2     
            RESTART_BOX_Y_CORRIDINATE = 100

            RESTART_BOX_BG = pygame.Rect(RESTART_BOX_BG_X_CORRIDINATE, RESTART_BOX_Y_CORRIDINATE, RESTART_BOX_BG_WIDTH, RESTART_BOX_TEXT.get_height())
            if DRAW_RESTART_BOX['RETURN_VALUE']:
                RESTART_BOX_DETAILS = {'x':RESTART_BOX_BG.x, 'y':RESTART_BOX_BG.y, 'width':RESTART_BOX_BG.width, 'height':RESTART_BOX_BG.height}
                return RESTART_BOX_DETAILS
            
            pygame.draw.rect(self.WIN, self.BLUE, RESTART_BOX_BG)
            self.WIN.blit(RESTART_BOX_TEXT, (RESTART_BOX_X_CORRIDINATE, RESTART_BOX_Y_CORRIDINATE))
            return None

        if DRAW_PLAYER_MOVE_BOX['DRAW'] or DRAW_PLAYER_MOVE_BOX['RETURN_VALUE']:
            PLAYER = self.PLAYER
            BORDER = self.border('BORDER', border_value = True)
            RESTART_BOX_DETAILS = self.draw_WIN(DRAW_RESTART_BOX = {'DRAW': False, 'RETURN_VALUE': True})
            PLAYER_MOVE_BOX_Ln1_TEXT = self.FONT_PLAYER_MOVE_BOX.render(" PLAYER " + PLAYER + "'s ", 1, self.YELLOW) 
            PLAYER_MOVE_BOX_Ln2_TEXT = self.FONT_PLAYER_MOVE_BOX.render(" MOVE ", 1, self.WHITE) 

            PLAYER_MOVE_BOX_Ln1_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Player Move Box
            PLAYER_MOVE_BOX_Ln1_BG_WIDTH = self.WIDTH - PLAYER_MOVE_BOX_Ln1_BG_X_CORRIDINATE - 20       # 20 is distance between Player Move Box and Window End
            PLAYER_MOVE_BOX_Ln1_X_CORRIDINATE = PLAYER_MOVE_BOX_Ln1_BG_X_CORRIDINATE + (PLAYER_MOVE_BOX_Ln1_BG_WIDTH - PLAYER_MOVE_BOX_Ln1_TEXT.get_width())/2     
            PLAYER_MOVE_BOX_Ln1_Y_CORRIDINATE = RESTART_BOX_DETAILS['y'] + RESTART_BOX_DETAILS['height'] + 30
            PLAYER_MOVE_Ln1_BOX_BG = pygame.Rect(PLAYER_MOVE_BOX_Ln1_BG_X_CORRIDINATE, PLAYER_MOVE_BOX_Ln1_Y_CORRIDINATE, PLAYER_MOVE_BOX_Ln1_BG_WIDTH, PLAYER_MOVE_BOX_Ln1_TEXT.get_height()+3)

            PLAYER_MOVE_BOX_Ln2_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Player Move Box
            PLAYER_MOVE_BOX_Ln2_BG_WIDTH = self.WIDTH - PLAYER_MOVE_BOX_Ln2_BG_X_CORRIDINATE - 20       # 20 is distance between Player Move Box and Window End
            PLAYER_MOVE_BOX_Ln2_X_CORRIDINATE = PLAYER_MOVE_BOX_Ln2_BG_X_CORRIDINATE + (PLAYER_MOVE_BOX_Ln2_BG_WIDTH - PLAYER_MOVE_BOX_Ln2_TEXT.get_width())/2     
            PLAYER_MOVE_BOX_Ln2_Y_CORRIDINATE = PLAYER_MOVE_Ln1_BOX_BG.y + PLAYER_MOVE_Ln1_BOX_BG.height
            PLAYER_MOVE_Ln2_BOX_BG = pygame.Rect(PLAYER_MOVE_BOX_Ln2_BG_X_CORRIDINATE, PLAYER_MOVE_BOX_Ln2_Y_CORRIDINATE, PLAYER_MOVE_BOX_Ln2_BG_WIDTH, PLAYER_MOVE_BOX_Ln2_TEXT.get_height()+3)

            
            if DRAW_PLAYER_MOVE_BOX['RETURN_VALUE']:
                PLAYER_MOVE_Ln1_BOX_DETAILS = {'x': PLAYER_MOVE_Ln1_BOX_BG.x, 'y': PLAYER_MOVE_Ln1_BOX_BG.y, 'width': PLAYER_MOVE_Ln1_BOX_BG.width, 'height': PLAYER_MOVE_Ln1_BOX_BG.height}
                PLAYER_MOVE_Ln2_BOX_DETAILS = {'x': PLAYER_MOVE_Ln2_BOX_BG.x, 'y': PLAYER_MOVE_Ln2_BOX_BG.y, 'width': PLAYER_MOVE_Ln2_BOX_BG.width, 'height': PLAYER_MOVE_Ln2_BOX_BG.height}
                PLAYER_MOVE_BOX_DETAILS = {"PLAYER_MOVE_Ln1_BOX_DETAILS": PLAYER_MOVE_Ln1_BOX_DETAILS, "PLAYER_MOVE_Ln2_BOX_DETAILS": PLAYER_MOVE_Ln2_BOX_DETAILS}
                return PLAYER_MOVE_BOX_DETAILS
            
            pygame.draw.rect(self.WIN, self.BLUE, PLAYER_MOVE_Ln1_BOX_BG)
            self.WIN.blit(PLAYER_MOVE_BOX_Ln1_TEXT, (PLAYER_MOVE_BOX_Ln1_X_CORRIDINATE, PLAYER_MOVE_BOX_Ln1_Y_CORRIDINATE))
            pygame.draw.rect(self.WIN, self.BLUE, PLAYER_MOVE_Ln2_BOX_BG)
            self.WIN.blit(PLAYER_MOVE_BOX_Ln2_TEXT, (PLAYER_MOVE_BOX_Ln2_X_CORRIDINATE, PLAYER_MOVE_BOX_Ln2_Y_CORRIDINATE))
            return None

        if DRAW_GRAVITY_BOX['DRAW'] or DRAW_GRAVITY_BOX['RETURN_VALUE']:
            GRAVITY = self.GRAVITY
            BORDER = self.border('BORDER', border_value = True)
            PLAYER_MOVE_BOX_DETAILS = self.draw_WIN(DRAW_PLAYER_MOVE_BOX = {'DRAW': False, 'RETURN_VALUE': True})
            GRAVITY_BOX_Ln1_TEXT = self.FONT_GRAVITY_BOX.render(" GRAVITY ", 1, self.WHITE) 
            GRAVITY_BOX_Ln2_TEXT = self.FONT_GRAVITY_BOX.render(" IS ON ", 1, self.WHITE) 
            GRAVITY_BOX_Ln3_TEXT = self.FONT_GRAVITY_BOX.render(GRAVITY, 1, self.GREEN) 

            GRAVITY_BOX_Ln1_BOX_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Gravity Line 1 Box
            GRAVITY_BOX_Ln1_BOX_BG_WIDTH = self.WIDTH - GRAVITY_BOX_Ln1_BOX_BG_X_CORRIDINATE - 20       # 20 is distance between Gravity Line 1 Box and Window End
            GRAVITY_BOX_Ln1_BOX_X_CORRIDINATE = GRAVITY_BOX_Ln1_BOX_BG_X_CORRIDINATE + (GRAVITY_BOX_Ln1_BOX_BG_WIDTH - GRAVITY_BOX_Ln1_TEXT.get_width())/2     
            GRAVITY_BOX_Ln1_BOX_Y_CORRIDINATE = PLAYER_MOVE_BOX_DETAILS['PLAYER_MOVE_Ln2_BOX_DETAILS']['y'] + PLAYER_MOVE_BOX_DETAILS['PLAYER_MOVE_Ln2_BOX_DETAILS']['height'] + 30
            GRAVITY_BOX_Ln1_BOX_BG = pygame.Rect(GRAVITY_BOX_Ln1_BOX_BG_X_CORRIDINATE, GRAVITY_BOX_Ln1_BOX_Y_CORRIDINATE, GRAVITY_BOX_Ln1_BOX_BG_WIDTH, GRAVITY_BOX_Ln1_TEXT.get_height())

            GRAVITY_BOX_Ln2_BOX_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Gravity Line 2 Box
            GRAVITY_BOX_Ln2_BOX_BG_WIDTH = self.WIDTH - GRAVITY_BOX_Ln2_BOX_BG_X_CORRIDINATE - 20       # 20 is distance between Gravity Line 2 Box and Window End
            GRAVITY_BOX_Ln2_BOX_X_CORRIDINATE = GRAVITY_BOX_Ln2_BOX_BG_X_CORRIDINATE + (GRAVITY_BOX_Ln2_BOX_BG_WIDTH - GRAVITY_BOX_Ln2_TEXT.get_width())/2     
            GRAVITY_BOX_Ln2_BOX_Y_CORRIDINATE = GRAVITY_BOX_Ln1_BOX_BG.y + GRAVITY_BOX_Ln1_BOX_BG.height
            GRAVITY_BOX_Ln2_BOX_BG = pygame.Rect(GRAVITY_BOX_Ln2_BOX_BG_X_CORRIDINATE, GRAVITY_BOX_Ln2_BOX_Y_CORRIDINATE, GRAVITY_BOX_Ln2_BOX_BG_WIDTH, GRAVITY_BOX_Ln2_TEXT.get_height())

            GRAVITY_BOX_Ln3_BOX_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Gravity Line 3 Box
            GRAVITY_BOX_Ln3_BOX_BG_WIDTH = self.WIDTH - GRAVITY_BOX_Ln3_BOX_BG_X_CORRIDINATE - 20       # 20 is distance between Gravity Line 3 Box and Window End
            GRAVITY_BOX_Ln3_BOX_X_CORRIDINATE = GRAVITY_BOX_Ln3_BOX_BG_X_CORRIDINATE + (GRAVITY_BOX_Ln3_BOX_BG_WIDTH - GRAVITY_BOX_Ln3_TEXT.get_width())/2     
            GRAVITY_BOX_Ln3_BOX_Y_CORRIDINATE = GRAVITY_BOX_Ln2_BOX_BG.y + GRAVITY_BOX_Ln2_BOX_BG.height
            GRAVITY_BOX_Ln3_BOX_BG = pygame.Rect(GRAVITY_BOX_Ln3_BOX_BG_X_CORRIDINATE, GRAVITY_BOX_Ln3_BOX_Y_CORRIDINATE, GRAVITY_BOX_Ln3_BOX_BG_WIDTH, GRAVITY_BOX_Ln3_TEXT.get_height())
            
            if DRAW_GRAVITY_BOX['RETURN_VALUE']:
                GRAVITY_BOX_Ln1_DETAILS = {'x': GRAVITY_BOX_Ln1_BOX_BG.x, 'y': GRAVITY_BOX_Ln1_BOX_BG.y, 'width': GRAVITY_BOX_Ln1_BOX_BG.width, 'height': GRAVITY_BOX_Ln1_BOX_BG.height}
                GRAVITY_BOX_Ln2_DETAILS = {'x': GRAVITY_BOX_Ln2_BOX_BG.x, 'y': GRAVITY_BOX_Ln2_BOX_BG.y, 'width': GRAVITY_BOX_Ln2_BOX_BG.width, 'height': GRAVITY_BOX_Ln2_BOX_BG.height}
                GRAVITY_BOX_Ln3_DETAILS = {'x': GRAVITY_BOX_Ln3_BOX_BG.x, 'y': GRAVITY_BOX_Ln3_BOX_BG.y, 'width': GRAVITY_BOX_Ln3_BOX_BG.width, 'height': GRAVITY_BOX_Ln3_BOX_BG.height}
                GRAVITY_BOX_DETAILS = {'GRAVITY_BOX_Ln1_DETAILS': GRAVITY_BOX_Ln1_DETAILS, 'GRAVITY_BOX_Ln2_DETAILS': GRAVITY_BOX_Ln2_DETAILS, 'GRAVITY_BOX_Ln3_DETAILS': GRAVITY_BOX_Ln3_DETAILS}
                return GRAVITY_BOX_DETAILS
            
            pygame.draw.rect(self.WIN, self.BLUE, GRAVITY_BOX_Ln1_BOX_BG)
            self.WIN.blit(GRAVITY_BOX_Ln1_TEXT, (GRAVITY_BOX_Ln1_BOX_X_CORRIDINATE, GRAVITY_BOX_Ln1_BOX_Y_CORRIDINATE))
            pygame.draw.rect(self.WIN, self.BLUE, GRAVITY_BOX_Ln2_BOX_BG)
            self.WIN.blit(GRAVITY_BOX_Ln2_TEXT, (GRAVITY_BOX_Ln2_BOX_X_CORRIDINATE, GRAVITY_BOX_Ln2_BOX_Y_CORRIDINATE))
            pygame.draw.rect(self.WIN, self.BLUE, GRAVITY_BOX_Ln3_BOX_BG)
            self.WIN.blit(GRAVITY_BOX_Ln3_TEXT, (GRAVITY_BOX_Ln3_BOX_X_CORRIDINATE, GRAVITY_BOX_Ln3_BOX_Y_CORRIDINATE))
            return None

        if DRAW_CREDITS_BOX['DRAW'] or DRAW_CREDITS_BOX['RETURN_VALUE']:
            BORDER = self.border('BORDER', border_value = True)
            GRAVITY_BOX_DETAILS = self.draw_WIN(DRAW_GRAVITY_BOX = {'DRAW': False, 'RETURN_VALUE': True})
            CREDITS_BOX_Ln1_TEXT = self.FONT_CERDITS_Title_BOX.render(" Powered By ", 1, self.BLACK)
            CREDITS_BOX_Ln2_TEXT = self.FONT_CERDITS_Name_BOX.render(" HIDDEN BLADE ", 1, self.BLACK) 

            CREDITS_BOX_Ln1_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Credits Box
            CREDITS_BOX_Ln1_BG_WIDTH = self.WIDTH - CREDITS_BOX_Ln1_BG_X_CORRIDINATE - 20       # 20 is distance between Credits Box and Window End
            CREDITS_BOX_Ln1_X_CORRIDINATE = CREDITS_BOX_Ln1_BG_X_CORRIDINATE + (CREDITS_BOX_Ln1_BG_WIDTH - CREDITS_BOX_Ln1_TEXT.get_width())/2     
            CREDITS_BOX_Ln1_Y_CORRIDINATE = GRAVITY_BOX_DETAILS['GRAVITY_BOX_Ln3_DETAILS']['y'] + GRAVITY_BOX_DETAILS['GRAVITY_BOX_Ln3_DETAILS']['height'] + 30
            CREDITS_BOX_Ln1_BG = pygame.Rect(CREDITS_BOX_Ln1_BG_X_CORRIDINATE, CREDITS_BOX_Ln1_Y_CORRIDINATE, CREDITS_BOX_Ln1_BG_WIDTH, CREDITS_BOX_Ln1_TEXT.get_height()+3)

            CREDITS_BOX_Ln2_BG_X_CORRIDINATE = BORDER.x + BORDER.width + 20     # 20 is distance between Border and Credits Box
            CREDITS_BOX_Ln2_BG_WIDTH = self.WIDTH - CREDITS_BOX_Ln2_BG_X_CORRIDINATE - 20       # 20 is distance between Credits Box and Window End
            CREDITS_BOX_Ln2_X_CORRIDINATE = CREDITS_BOX_Ln2_BG_X_CORRIDINATE + (CREDITS_BOX_Ln2_BG_WIDTH - CREDITS_BOX_Ln2_TEXT.get_width())/2     
            CREDITS_BOX_Ln2_Y_CORRIDINATE = CREDITS_BOX_Ln1_BG.y + CREDITS_BOX_Ln1_BG.height
            CREDITS_BOX_Ln2_BG = pygame.Rect(CREDITS_BOX_Ln2_BG_X_CORRIDINATE, CREDITS_BOX_Ln2_Y_CORRIDINATE, CREDITS_BOX_Ln2_BG_WIDTH, CREDITS_BOX_Ln2_TEXT.get_height()+3)
            
            if DRAW_CREDITS_BOX['RETURN_VALUE']:
                CREDITS_BOX_Ln1_DETAILS = {'x': CREDITS_BOX_Ln1_BG.x, 'y': CREDITS_BOX_Ln1_BG.y, 'width': CREDITS_BOX_Ln1_BG.width, 'height': CREDITS_BOX_Ln1_BG.height}
                CREDITS_BOX_Ln2_DETAILS = {'x': CREDITS_BOX_Ln2_BG.x, 'y': CREDITS_BOX_Ln2_BG.y, 'width': CREDITS_BOX_Ln2_BG.width, 'height': CREDITS_BOX_Ln2_BG.height}
                PLAYER_MOVE_BOX_DETAILS = {"CREDITS_BOX_Ln1_DETAILS": CREDITS_BOX_Ln1_DETAILS, "CREDITS_BOX_Ln2_DETAILS": CREDITS_BOX_Ln2_DETAILS}
                return PLAYER_MOVE_BOX_DETAILS
            
            pygame.draw.rect(self.WIN, self.GREY, CREDITS_BOX_Ln1_BG)
            self.WIN.blit(CREDITS_BOX_Ln1_TEXT, (CREDITS_BOX_Ln1_X_CORRIDINATE, CREDITS_BOX_Ln1_Y_CORRIDINATE))
            pygame.draw.rect(self.WIN, self.GREY, CREDITS_BOX_Ln2_BG)
            self.WIN.blit(CREDITS_BOX_Ln2_TEXT, (CREDITS_BOX_Ln2_X_CORRIDINATE, CREDITS_BOX_Ln2_Y_CORRIDINATE))
            return None            

        if self.THEME == 'NEON':
            self.WIN.blit(self.BACKGROUND_GAME_NEON, (0,0))
        else:
            self.WIN.blit(self.BACKGROUND_GAME_DARK, (0,0))

        # BORDERS   
        pygame.draw.rect(self.WIN, self.WHITE, self.border('BORDER'))        # Drawing Border between Game Surface & Game Info
        pygame.draw.rect(self.WIN, self.VIOLET, self.border('GAME_BORDER'))       # Drawing Border of Game
        self.border('GAME_BORDER_SEP_VER')        # Drawing Game Border Vertical Seperators
        self.border('GAME_BORDER_SEP_HORI')       # Drawing Game Border Horizontal Seperators
        pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, self.border('GAME_BORDER_UP'))       # Drawing Game Border UP
        pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, self.border('GAME_BORDER_LEFT'))       # Drawing Game Border LEFT
        pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, self.border('GAME_BORDER_DOWN'))       # Drawing Game Border DOWN
        pygame.draw.rect(self.WIN, self.COLOUR_LINES_GAME_BOARD, self.border('GAME_BORDER_RIGHT'))       # Drawing Game Border RIGHT

        self.draw_WIN(DRAW_RESTART_BOX = {'DRAW': True, 'RETURN_VALUE': False})         # Drawing Restart Box
        self.draw_WIN( DRAW_PLAYER_MOVE_BOX = {'DRAW': True, 'RETURN_VALUE': False})    # Drawing Player Move Box
        self.draw_WIN(DRAW_GRAVITY_BOX =  {'DRAW': True, 'RETURN_VALUE': False})        # Drawing Gravity Box
        self.draw_WIN(DRAW_CREDITS_BOX =  {'DRAW': True, 'RETURN_VALUE': False})        # Drawing Credits


        for DATA_KEY in self.DRAW_IMAGE_DATA:
            DATA = DATA_KEY.split()       #List
            DRAW_PLAYER = DATA[0]
            POSITION_BLOCK_CORRIDATE = self.DRAW_IMAGE_DATA[DATA_KEY]
            if DRAW_PLAYER == self.PLAYER_X:
                self.WIN.blit(self.IMAGE_PLAYER_X, POSITION_BLOCK_CORRIDATE)
            elif DRAW_PLAYER == self.PLAYER_O:
                self.WIN.blit(self.IMAGE_PLAYER_O, POSITION_BLOCK_CORRIDATE)

        if DRAW_PLAYER_IMAGE[0]:
        
            PLAYER = DRAW_PLAYER_IMAGE[1]
            POSITION = DRAW_PLAYER_IMAGE[2]
            DRAW_IMAGE_DATA_VALUE = DRAW_PLAYER_IMAGE[3]
            DRAW_IMAGE_DATA_KEY = PLAYER +' '+ str(POSITION)
            self.DRAW_IMAGE_DATA[DRAW_IMAGE_DATA_KEY] = DRAW_IMAGE_DATA_VALUE

            self.draw_WIN()   

        pygame.display.update()


    def restart_WIN(self):
        RESTART_NO_DETAILS, RESTART_YES_DETAILS = self.draw_WIN(DRAW_RESTART_WIN = True)
        RUN_RESTART = True
        while RUN_RESTART:
            for EVENT_RESTART in pygame.event.get():    
                if EVENT_RESTART.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= RESTART_YES_DETAILS['x'] and MOUSE_POSITION[0] <= RESTART_YES_DETAILS['x'] + RESTART_YES_DETAILS['width'] and MOUSE_POSITION[1] >= RESTART_YES_DETAILS['y'] and MOUSE_POSITION[1] <= RESTART_YES_DETAILS['y'] + RESTART_YES_DETAILS['height']:
                        RUN_RESTART = False    # To stop the EXIT WHILE LOOP    

                    elif MOUSE_POSITION[0] >= RESTART_NO_DETAILS['x'] and MOUSE_POSITION[0] <= RESTART_NO_DETAILS['x'] + RESTART_NO_DETAILS['width'] and MOUSE_POSITION[1] >= RESTART_NO_DETAILS['y'] and MOUSE_POSITION[1] <= RESTART_NO_DETAILS['y'] + RESTART_NO_DETAILS['height']:
                        run = True  # To Re-Display the Screen
                        return run
                    

    def Restart_Box_function(self, EVENT):
        if EVENT.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
            self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
            MOUSE_POSITION = self.mouse_input('MOUSE POSITION')     # Returns the current mouse CLICKED position
            RESTART_BOX_DETAILS = self.draw_WIN(DRAW_RESTART_BOX = {'DRAW': False, 'RETURN_VALUE': True})

            if MOUSE_POSITION[0] > RESTART_BOX_DETAILS['x'] and MOUSE_POSITION[0] < RESTART_BOX_DETAILS['x'] + RESTART_BOX_DETAILS['width'] and MOUSE_POSITION[1] > RESTART_BOX_DETAILS['y'] and MOUSE_POSITION[1] < RESTART_BOX_DETAILS['y'] + RESTART_BOX_DETAILS['height']:
                STATUS = {'MOUSE_CLICKED': False, 'INSERT_SUCCESS':False,'RESTART': True}
                return STATUS
            
            else:
                STATUS = {'MOUSE_CLICKED': False, 'INSERT_SUCCESS':False,'RESTART': False}
                return STATUS
            
        else:
            STATUS = {'MOUSE_CLICKED': False, 'INSERT_SUCCESS':False,'RESTART': False}
            return STATUS
        

    def exit_WIN(self):
        EXIT_BOX_EXIT_DETAILS, EXIT_BOX_STAY_DETAILS = self.draw_WIN(DRAW_EXIT_WIN = True)
        RUN_EXIT_BOX = True
        while RUN_EXIT_BOX:
            for EVENT_EXIT in pygame.event.get():    
                if EVENT_EXIT.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= EXIT_BOX_STAY_DETAILS['x'] and MOUSE_POSITION[0] <= EXIT_BOX_STAY_DETAILS['x'] + EXIT_BOX_STAY_DETAILS['width'] and MOUSE_POSITION[1] >= EXIT_BOX_STAY_DETAILS['y'] and MOUSE_POSITION[1] <= EXIT_BOX_STAY_DETAILS['y'] + EXIT_BOX_STAY_DETAILS['height']:
                        RUN_EXIT_BOX = False    # To stop the EXIT WHILE LOOP    

                    elif MOUSE_POSITION[0] >= EXIT_BOX_EXIT_DETAILS['x'] and MOUSE_POSITION[0] <= EXIT_BOX_EXIT_DETAILS['x'] + EXIT_BOX_EXIT_DETAILS['width'] and MOUSE_POSITION[1] >= EXIT_BOX_EXIT_DETAILS['y'] and MOUSE_POSITION[1] <= EXIT_BOX_EXIT_DETAILS['y'] + EXIT_BOX_EXIT_DETAILS['height']:
                        run = False  # To stop the WHILE LOOP
                        return run
                    

    def result_WIN(self, PLAYER_or_DRAW):
        RESULT_RESTART_DETAILS, RESULT_VIEW_GAME_DETAILS, RESULT_EXIT_DETAILS = self.draw_WIN(DRAW_RESULT=(True, PLAYER_or_DRAW))
        RUN_RESULT = True
        while RUN_RESULT:
            for EVENT_RESULT in pygame.event.get():
                if EVENT_RESULT.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                    else:
                        self.result_WIN(PLAYER_or_DRAW)

                if EVENT_RESULT.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= RESULT_RESTART_DETAILS['x'] and MOUSE_POSITION[0] <= RESULT_RESTART_DETAILS['x'] + RESULT_RESTART_DETAILS['width'] and MOUSE_POSITION[1] >= RESULT_RESTART_DETAILS['y'] and MOUSE_POSITION[1] <= RESULT_RESTART_DETAILS['y'] + RESULT_RESTART_DETAILS['height']:
                        RESTART = True    # To stop the EXIT WHILE LOOP  
                        return RESTART  

                    elif MOUSE_POSITION[0] >= RESULT_VIEW_GAME_DETAILS['x'] and MOUSE_POSITION[0] <= RESULT_VIEW_GAME_DETAILS['x'] + RESULT_VIEW_GAME_DETAILS['width'] and MOUSE_POSITION[1] >= RESULT_VIEW_GAME_DETAILS['y'] and MOUSE_POSITION[1] <= RESULT_VIEW_GAME_DETAILS['y'] + RESULT_VIEW_GAME_DETAILS['height']:
                        self.draw_WIN()
                        RUN_VIEW_GAME = True
                        while RUN_VIEW_GAME:
                            for EVENT in pygame.event.get():
                                if EVENT.type == pygame.QUIT:
                                    run = self.exit_WIN()
                                    if run is False:
                                        exit()      # To exit from all the loop and functions
                                    else:
                                        self.draw_WIN()
                                STATUS = self.Restart_Box_function(EVENT)
                                if STATUS['RESTART'] is True:
                                    run = self.restart_WIN()
                                    if run is not True:
                                        RUN_VIEW_GAME = False
                                        RUN_RESULT = False
                                        return True     # Equating RESTART value in init_func as True
                                    else:
                                        self.draw_WIN()
                                            
                                                


                    elif MOUSE_POSITION[0] >= RESULT_EXIT_DETAILS['x'] and MOUSE_POSITION[0] <= RESULT_EXIT_DETAILS['x'] + RESULT_EXIT_DETAILS['width'] and MOUSE_POSITION[1] >= RESULT_EXIT_DETAILS['y'] and MOUSE_POSITION[1] <= RESULT_EXIT_DETAILS['y'] + RESULT_EXIT_DETAILS['height']:
                        
                        exit() 

    def credits(self):
        CREDITS_BACK_DETAILS = self.draw_WIN(DRAW_CREDITS = True)
        MENU_CREDITS = True                       
        while MENU_CREDITS :
            for EVENT_GAME_MODE in pygame.event.get():
                if EVENT_GAME_MODE.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                    else:
                        self.draw_WIN(DRAW_CREDITS = True)
                    
                        if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                            self.audio(PLAY_SEFX_BUTTON_CLICK = True, SOUND_UPDATE = True)     # Mouse Click Button Sound Effect
                            MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                
                            if MOUSE_POSITION[0] >= CREDITS_BACK_DETAILS['x'] and MOUSE_POSITION[0] <= CREDITS_BACK_DETAILS['x'] + CREDITS_BACK_DETAILS['width'] and MOUSE_POSITION[1] >= CREDITS_BACK_DETAILS['y'] and MOUSE_POSITION[1] <= CREDITS_BACK_DETAILS['y'] + CREDITS_BACK_DETAILS['height']:
                                    print("BACK")
                                    MENU_CREDITS = False

    def settings(self):
        SETTINGS_THEME_DETAILS, SETTINGS_MUSIC_DETAILS, SETTINGS_SOUND_EFFECTS_DETAILS, SETTINGS_BACK = self.draw_WIN(DRAW_MENU_SETTINGS = True)
        MENU_SETTINGS = True                       
        while MENU_SETTINGS :
            for EVENT_GAME_MODE in pygame.event.get():
                if EVENT_GAME_MODE.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                    else:
                        self.draw_WIN(DRAW_MENU_SETTINGS = True)

                if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True, SOUND_UPDATE = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= SETTINGS_THEME_DETAILS['x'] and MOUSE_POSITION[0] <= SETTINGS_THEME_DETAILS['x'] + SETTINGS_THEME_DETAILS['width'] and MOUSE_POSITION[1] >= SETTINGS_THEME_DETAILS['y'] and MOUSE_POSITION[1] <= SETTINGS_THEME_DETAILS['y'] + SETTINGS_THEME_DETAILS['height']:
                        print("THEME")
                        if self.THEME == 'NEON':  self.THEME = 'DARK'
                        else:   self.THEME = 'NEON'
                        self.draw_WIN(DRAW_MENU_SETTINGS = True)

                
                    if MOUSE_POSITION[0] >= SETTINGS_MUSIC_DETAILS['x'] and MOUSE_POSITION[0] <= SETTINGS_MUSIC_DETAILS['x'] + SETTINGS_MUSIC_DETAILS['width'] and MOUSE_POSITION[1] >= SETTINGS_MUSIC_DETAILS['y'] and MOUSE_POSITION[1] <= SETTINGS_MUSIC_DETAILS['y'] + SETTINGS_MUSIC_DETAILS['height']:
                        print("MUSIC")
                        if self.MUSIC == 'ON': 
                            self.MUSIC = 'OFF'
                        else:   self.MUSIC = 'ON'
                        self.audio()
                        self.draw_WIN(DRAW_MENU_SETTINGS = True)

                
                    if MOUSE_POSITION[0] >= SETTINGS_SOUND_EFFECTS_DETAILS['x'] and MOUSE_POSITION[0] <= SETTINGS_SOUND_EFFECTS_DETAILS['x'] + SETTINGS_SOUND_EFFECTS_DETAILS['width'] and MOUSE_POSITION[1] >= SETTINGS_SOUND_EFFECTS_DETAILS['y'] and MOUSE_POSITION[1] <= SETTINGS_SOUND_EFFECTS_DETAILS['y'] + SETTINGS_SOUND_EFFECTS_DETAILS['height']:
                        print("SOUND EFFECTS")
                        if self.SOUND == 'ON':  
                            self.SOUND = 'OFF'

                        else:   self.SOUND = 'ON'
                        print(self.SOUND)
                        self.audio(SOUND_UPDATE = True)
                        self.draw_WIN(DRAW_MENU_SETTINGS = True)

                    if MOUSE_POSITION[0] >= SETTINGS_BACK['x'] and MOUSE_POSITION[0] <= SETTINGS_BACK['x'] + SETTINGS_BACK['width'] and MOUSE_POSITION[1] >= SETTINGS_BACK['y'] and MOUSE_POSITION[1] <= SETTINGS_BACK['y'] + SETTINGS_BACK['height']:
                        print("BACK")
                        MENU_SETTINGS = False
                       
    
    def menu(self):
        
        MENU_PLAY_DETAILS, MENU_SETTINGS_DETAILS, MENU_CREDITS_DETAILS = self.draw_WIN(DRAW_MENU = True)
        RUN_MENU = True                       
        while RUN_MENU :
            for EVENT_GAME_MODE in pygame.event.get():
                if EVENT_GAME_MODE.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                    else:
                        self.draw_WIN(DRAW_MENU = True)

                if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= MENU_PLAY_DETAILS['x'] and MOUSE_POSITION[0] <= MENU_PLAY_DETAILS['x'] + MENU_PLAY_DETAILS['width'] and MOUSE_POSITION[1] >= MENU_PLAY_DETAILS['y'] and MOUSE_POSITION[1] <= MENU_PLAY_DETAILS['y'] + MENU_PLAY_DETAILS['height']:
                        print("PLAY")
                        # self.game_mode()
                        RUN_MENU = False

                if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= MENU_SETTINGS_DETAILS['x'] and MOUSE_POSITION[0] <= MENU_SETTINGS_DETAILS['x'] + MENU_SETTINGS_DETAILS['width'] and MOUSE_POSITION[1] >= MENU_SETTINGS_DETAILS['y'] and MOUSE_POSITION[1] <= MENU_SETTINGS_DETAILS['y'] + MENU_SETTINGS_DETAILS['height']:
                        print("SETTINGS")
                        self.settings()
                        self.draw_WIN(DRAW_MENU = True)

                        # RUN_MENU = False
                        
                if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= MENU_CREDITS_DETAILS['x'] and MOUSE_POSITION[0] <= MENU_CREDITS_DETAILS['x'] + MENU_CREDITS_DETAILS['width'] and MOUSE_POSITION[1] >= MENU_CREDITS_DETAILS['y'] and MOUSE_POSITION[1] <= MENU_CREDITS_DETAILS['y'] + MENU_CREDITS_DETAILS['height']:
                        print("CREDITS")
                        self.credits()
                        RUN_MENU = False


    def game_mode(self): 

        GAME_MODE_SIMPLE_DETAILS, GAME_MODE_COMPLEX_DETAILS = self.draw_WIN(DRAW_GAME_MODE = True)    
        RUN_GAME_MODE = True                       
        while RUN_GAME_MODE :
            for EVENT_GAME_MODE in pygame.event.get():
                if EVENT_GAME_MODE.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                    else:
                        self.draw_WIN(DRAW_GAME_MODE = True)

                if EVENT_GAME_MODE.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                    if MOUSE_POSITION[0] >= GAME_MODE_SIMPLE_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_SIMPLE_DETAILS['x'] + GAME_MODE_SIMPLE_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_SIMPLE_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_SIMPLE_DETAILS['y'] + GAME_MODE_SIMPLE_DETAILS['height']:
                        print("SIMPLE")
                        GAME_MODE_UP_DETAILS, GAME_MODE_DOWN_DETAILS, GAME_MODE_RIGHT_DETAILS, GAME_MODE_LEFT_DETAILS = self.draw_WIN(DRAW_GAME_MODE_SPECIAL=True) 
                        RUN_GAME_MODE_SPECIAL = True                       
                        while RUN_GAME_MODE_SPECIAL :
                            
                            for EVENT_GAME_MODE_SPECIAL in pygame.event.get():
                                if EVENT_GAME_MODE_SPECIAL.type == pygame.QUIT:
                                    run = self.exit_WIN()
                                    if run is False:
                                        exit()      # To exit from all the loop and functions
                                    else:
                                        self.draw_WIN(DRAW_GAME_MODE_SPECIAL = True)

                                if EVENT_GAME_MODE_SPECIAL.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
                                    self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
                                    MOUSE_POSITION = pygame.mouse.get_pos()                 # Returns the current mouse CLICKED position
                                    
                                    if MOUSE_POSITION[0] >= GAME_MODE_UP_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_UP_DETAILS['x'] + GAME_MODE_UP_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_UP_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_UP_DETAILS['y'] + GAME_MODE_UP_DETAILS['height']:
                                        
                                        self.PLAY_BGM_Mode_Simple = True
                                        # self.AUDIO_BGM_Menu.stop()
                                        # self.AUDIO_BGM_Mode_Simple.play(-1)
                                        RUN_GAME_MODE_SPECIAL = False
                                        return 'UP'

                                    elif MOUSE_POSITION[0] >= GAME_MODE_DOWN_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_DOWN_DETAILS['x'] + GAME_MODE_DOWN_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_DOWN_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_DOWN_DETAILS['y'] + GAME_MODE_DOWN_DETAILS['height']:
                                        self.PLAY_BGM_Mode_Simple = True
                                        # self.AUDIO_BGM_Menu.stop()
                                        # self.AUDIO_BGM_Mode_Simple.play(-1)
                                        RUN_GAME_MODE_SPECIAL = False
                                        return 'DOWN'

                                    elif MOUSE_POSITION[0] >= GAME_MODE_RIGHT_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_RIGHT_DETAILS['x'] + GAME_MODE_RIGHT_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_RIGHT_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_RIGHT_DETAILS['y'] + GAME_MODE_RIGHT_DETAILS['height']:
                                        self.PLAY_BGM_Mode_Simple = True
                                        # self.AUDIO_BGM_Menu.stop()
                                        # self.AUDIO_BGM_Mode_Simple.play(-1)
                                        RUN_GAME_MODE_SPECIAL = False
                                        return 'RIGHT'

                                    elif MOUSE_POSITION[0] >= GAME_MODE_LEFT_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_LEFT_DETAILS['x'] + GAME_MODE_LEFT_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_LEFT_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_LEFT_DETAILS['y'] + GAME_MODE_LEFT_DETAILS['height']:
                                        self.PLAY_BGM_Mode_Simple = True
                                        # self.AUDIO_BGM_Menu.stop()
                                        # self.AUDIO_BGM_Mode_Simple.play(-1)
                                        RUN_GAME_MODE_SPECIAL = False
                                        return 'LEFT'

                        RUN_GAME_MODE = False
                    
                    elif MOUSE_POSITION[0] >= GAME_MODE_COMPLEX_DETAILS['x'] and MOUSE_POSITION[0] <= GAME_MODE_COMPLEX_DETAILS['x'] + GAME_MODE_COMPLEX_DETAILS['width'] and MOUSE_POSITION[1] >= GAME_MODE_COMPLEX_DETAILS['y'] and MOUSE_POSITION[1] <= GAME_MODE_COMPLEX_DETAILS['y'] + GAME_MODE_COMPLEX_DETAILS['height']:
                        print("COMPLEX")
                        self.PLAY_BGM_Mode_Complex = True
                        # self.AUDIO_BGM_Menu.stop()
                        # self.AUDIO_BGM_Mode_Complex.play(-1)
                        RUN_GAME_MODE = False
                        return 'COMPLEX'


    def Gravity_Value(self):
        GR_VALUE=random.randrange(1,5)
        if self.GAME_MODE_VALUE == "COMPLEX" :
            if GR_VALUE == 1:
                GRAVITY = 'DOWN'
                self.GRAVITY = GRAVITY

            elif GR_VALUE == 2:
                GRAVITY = 'RIGHT'
                self.GRAVITY = GRAVITY
            elif GR_VALUE == 3:
                GRAVITY = 'LEFT'
                self.GRAVITY = GRAVITY
            else :
                GRAVITY = 'UP'
                self.GRAVITY = GRAVITY
            self.draw_WIN(DRAW_GRAVITY_BOX =  {'DRAW': True, 'RETURN_VALUE': False})
            print("The Gravity is on",GRAVITY)
            # self.AUDIO_SEFX_GRAVITY.play(0,0,1)
            return GRAVITY
        else :
            GRAVITY = self.GAME_MODE_VALUE
            self.GRAVITY = GRAVITY
            self.draw_WIN(DRAW_GRAVITY_BOX =  {'DRAW': True, 'RETURN_VALUE': False})
            print("The Gravity is on",GRAVITY)
            return GRAVITY


    # def print_Board(self, board):                               # To print the self.board for each moves.
    #     print((' ~~~~~~~~~~~~~~~~~~~ ').center(80))
    #     print(('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |').center(80))
    #     print(('|---+---+---+---+---|').center(80))
    #     print(('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' |').center(80))
    #     print(('|---+---+---+---+---|').center(80))
    #     print(('| ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' |').center(80))
    #     print(('|---+---+---+---+---|').center(80))
    #     print(('| ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20] + ' |').center(80))
    #     print(('|---+---+---+---+---|').center(80))
    #     print(('| ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25] + ' |').center(80))
    #     print((' ~~~~~~~~~~~~~~~~~~~~ ').center(80))
    #     print("\n")


    def Space_Is_Free(self, POSITION, GRAVITY):                          # To check whether the space is free or not.
        if GRAVITY == 'UP':
            BELOW_POSITION = int(POSITION)-5         #Below position of current position
            if POSITION <=5 :
                if self.board[POSITION] == ' ':
                    return True
                else:
                    return False
            else:
                if self.board[POSITION] == ' ' and self.board[BELOW_POSITION]!=' ':
                    return True
                else:
                    return False

        elif GRAVITY == 'RIGHT':
            BELOW_POSITION = int(POSITION)+1
            if POSITION in (5,10,15,20,25):
                if self.board[POSITION] == ' ':
                    return True
                else:
                    return False
            else:
                if self.board[POSITION] == ' ' and self.board[BELOW_POSITION]!=' ':
                    return True
                else:
                    return False

        elif GRAVITY == 'LEFT':
            BELOW_POSITION=int(POSITION)-1
            if POSITION in (1,6,11,16,21):
                if self.board[POSITION] == ' ':
                    return True
                else:
                    return False
            else:
                if self.board[POSITION] == ' ' and self.board[BELOW_POSITION]!=' ':
                    return True
                else:
                    return False

        else:       #DOWN
            BELOW_POSITION=int(POSITION)+5
            if POSITION >=21 :
                if self.board[POSITION] == ' ':
                    return True
                else:
                    return False
            else:
                if self.board[POSITION] == ' ' and self.board[BELOW_POSITION]!=' ':
                    return True
                else:
                    return False
    

    def check_For_Win_Or_Draw(self, STATUS):                                   # To check whether any of players won the game.
        if STATUS == 'CHECK FOR DRAW':
            for key in self.board.keys():
                if (self.board[key] == ' '):
                    return False
            return True
        
        elif STATUS == 'CHECK FOR WIN':
            if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == self.board[4] and self.board[1] != ' '):             #Codes for Rows
                return True
            elif (self.board[2] == self.board[3] and self.board[2] == self.board[4] and self.board[2] == self.board[5] and self.board[2] != ' '):
                return True
            elif (self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[6] == self.board[9] and self.board[6] != ' '):
                return True
            elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == self.board[10] and self.board[7] != ' '):
                return True
            elif (self.board[11] == self.board[12] and self.board[11] == self.board[13] and self.board[11] == self.board[14] and self.board[11] != ' '):
                return True
            elif (self.board[12] == self.board[13] and self.board[12] == self.board[14] and self.board[12] == self.board[15] and self.board[12] != ' '):
                return True
            elif (self.board[16] == self.board[17] and self.board[16] == self.board[18] and self.board[16] == self.board[19] and self.board[16] != ' '):
                return True
            elif (self.board[17] == self.board[18] and self.board[17] == self.board[19] and self.board[17] == self.board[20] and self.board[17] != ' '):
                return True
            elif (self.board[21] == self.board[22] and self.board[21] == self.board[23] and self.board[21] == self.board[24] and self.board[21] != ' '):
                return True
            elif (self.board[22] == self.board[23] and self.board[22] == self.board[24] and self.board[22] == self.board[25] and self.board[22] != ' '):
                return True

            elif (self.board[1] == self.board[6] and self.board[1] == self.board[11] and self.board[1] == self.board[16] and self.board[1] != ' '):           #Codes for Columns
                return True
            elif (self.board[6] == self.board[11] and self.board[6] == self.board[16] and self.board[6] == self.board[21] and self.board[6] != ' '):
                return True
            elif (self.board[2] == self.board[7] and self.board[2] == self.board[12] and self.board[2] == self.board[17] and self.board[2] != ' '):
                return True
            elif (self.board[7] == self.board[12] and self.board[7] == self.board[17] and self.board[7] == self.board[22] and self.board[7] != ' '):
                return True
            elif (self.board[3] == self.board[8] and self.board[3] == self.board[13] and self.board[3] == self.board[18] and self.board[3] != ' '):
                return True
            elif (self.board[8] == self.board[13] and self.board[8] == self.board[18] and self.board[8] == self.board[23] and self.board[8] != ' '):
                return True
            elif (self.board[4] == self.board[9] and self.board[4] == self.board[14] and self.board[4] == self.board[19] and self.board[4] != ' '):
                return True
            elif (self.board[9] == self.board[14] and self.board[9] == self.board[19] and self.board[9] == self.board[24] and self.board[9] != ' '):
                return True
            elif (self.board[5] == self.board[10] and self.board[5] == self.board[15] and self.board[5] == self.board[20] and self.board[5] != ' '):
                return True
            elif (self.board[10] == self.board[15] and self.board[10] == self.board[20] and self.board[10] == self.board[25] and self.board[10] != ' '):
                return True
            
            elif (self.board[1] == self.board[7] and self.board[1] == self.board[13] and self.board[1] == self.board[19] and self.board[1] != ' '):           #Codes for Diagonals
                return True
            elif (self.board[7] == self.board[13] and self.board[7] == self.board[19] and self.board[7] == self.board[25] and self.board[7] != ' '):           
                return True
            elif (self.board[6] == self.board[12] and self.board[6] == self.board[18] and self.board[6] == self.board[24] and self.board[6] != ' '):           
                return True
            elif (self.board[2] == self.board[8] and self.board[2] == self.board[14] and self.board[2] == self.board[20] and self.board[2] != ' '):           
                return True
            elif (self.board[5] == self.board[9] and self.board[5] == self.board[13] and self.board[5] == self.board[17] and self.board[5] != ' '):           
                return True
            elif (self.board[9] == self.board[13] and self.board[9] == self.board[17] and self.board[9] == self.board[21] and self.board[9] != ' '):          
                return True
            elif (self.board[10] == self.board[14] and self.board[10] == self.board[18] and self.board[10] == self.board[22] and self.board[10] != ' '):      
                return True
            elif (self.board[4] == self.board[8] and self.board[4] == self.board[12] and self.board[4] == self.board[16] and self.board[4] != ' '):           
                return True
            else:
                return False


    def insert_value(self, PLAYER, POSITION, POSITION_BLOCK_CORRIDATE, GRAVITY):                        # To insert a letter of Player 1.
        if self.Space_Is_Free(POSITION, GRAVITY):
            self.board[POSITION] = PLAYER
            DRAW_PLAYER_IMAGE = (True, PLAYER, POSITION, POSITION_BLOCK_CORRIDATE)
            self.draw_WIN(DRAW_PLAYER_IMAGE)
            # self.print_Board(self.board)              # To print the Game Board in Terminal [To access it remove the comment statements from "print_Board(self, board)" and current line]
            if self.check_For_Win_Or_Draw('CHECK FOR WIN'):
                if PLAYER == self.PLAYER_X:
                    return {'WIN_OR_DRAW':'WIN', 'PLAYER':PLAYER}
                elif PLAYER == self.PLAYER_O:
                    return {'WIN_OR_DRAW':'WIN', 'PLAYER':PLAYER}
            
            elif (self.check_For_Win_Or_Draw('CHECK FOR DRAW')):
                return {'WIN_OR_DRAW':'DRAW'}
                                
            else:
                return {'WRONG POSITION':False, 'WIN_OR_DRAW':'NEITHER'}

        else:
            return {'WRONG POSITION':True, 'WIN_OR_DRAW':False}
            

    def player_position(self, PLAYER, EVENT, GRAVITY):
        if EVENT.type == pygame.MOUSEBUTTONDOWN and self.mouse_input('MOUSE PRESSED'):
            self.audio(PLAY_SEFX_BUTTON_CLICK = True)     # Mouse Click Button Sound Effect
            while True :
                try:
                    STATUS = self.Restart_Box_function(EVENT)
                    if STATUS['RESTART'] is True:
                        return STATUS

                    MOUSE_GET_BLOCK = self.mouse_input('GET BLOCK')[0]
                    POSITION = self.PYGAME_BOARD[MOUSE_GET_BLOCK]  
                    POSITION_BLOCK_CORRIDATE = self.mouse_input('GET BLOCK')[1]       # It is a TUPLE & Corridate of Block for drawing the input IMAGE          
                    
                    STATUS = self.insert_value(PLAYER, POSITION, POSITION_BLOCK_CORRIDATE, GRAVITY) 
                    
                    if STATUS['WIN_OR_DRAW'] == 'WIN':
                        return {'MOUSE_CLICKED': True, 'INSERT_SUCCESS':True, 'WIN_OR_DRAW':'WIN', 'PLAYER':STATUS['PLAYER'], 'RESTART': False}       

                    elif STATUS['WIN_OR_DRAW'] == 'DRAW':
                        return {'MOUSE_CLICKED': True, 'INSERT_SUCCESS':True, 'WIN_OR_DRAW':'DRAW', 'RESTART': False}
                    
                    elif STATUS['WRONG POSITION']:
                        return {'MOUSE_CLICKED': True, 'INSERT_SUCCESS':False, 'WIN_OR_DRAW':'NEITHER', 'RESTART': False}       # To known that Mouse was clicked BUT WRONG POSITION while inserting     
                        
                    else:
                        self.AUDIO_SEFX_XO_INSERT.play()
                        return {'MOUSE_CLICKED': True, 'INSERT_SUCCESS':True, 'WIN_OR_DRAW':'NEITHER', 'RESTART': False}         # To known that Mouse was clicked and Successfully Inserted
                    
                except:
                    return {'MOUSE_CLICKED': False, 'INSERT_SUCCESS':False, 'RESTART': False}

        else:
            return {'MOUSE_CLICKED': False, 'INSERT_SUCCESS':False, 'RESTART': False}
            
    
    def main(self):
        self.audio()
        clock = pygame.time.Clock()
        run = self.check_For_Win_Or_Draw("CHECK FOR WIN")
        GRAVITY = self.Gravity_Value()
        self.draw_WIN( DRAW_PLAYER_MOVE_BOX = {'DRAW': True, 'RETURN_VALUE': False})
        print(self.PLAYER, " :MOVE")
        
        while not run:
            clock.tick(self.FPS)
            
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    run = self.exit_WIN()
                    if run is False:
                        exit()      # To exit from all the loop and functions
                
                STATUS = self.player_position(self.PLAYER, EVENT, GRAVITY)

                if STATUS['RESTART'] is True:
                    RESTART_RUN = self.restart_WIN()
                    
                    if RESTART_RUN is not True:
                        self.RESTART = True

                        self.PLAY_BGM_Mode_Complex = False
                        self.PLAY_BGM_Mode_Simple = False
                        self.audio()
                        run = True

                if STATUS['INSERT_SUCCESS'] is False:
                    pass
                
                elif STATUS['WIN_OR_DRAW'] == 'WIN':
                    if STATUS['PLAYER'] == self.PLAYER_X:
                        print(self.PLAYER_X,"wins !")
                        self.PLAY_BGM_Mode_Complex = False
                        self.PLAY_BGM_Mode_Simple = False
                        self.audio()
                        self.AUDIO_SEFX_WIN.play()
                        self.RESTART = self.result_WIN('PLAYER X')
                        
                    elif STATUS['PLAYER'] == self.PLAYER_O:
                        print(self.PLAYER_O,"wins !")
                        self.PLAY_BGM_Mode_Complex = False
                        self.PLAY_BGM_Mode_Simple = False
                        self.audio()
                        self.AUDIO_SEFX_WIN.play()
                        self.RESTART = self.result_WIN('PLAYER O')

                    
                    run = True  # To stop the main WHILE LOOP
                    
                elif STATUS['WIN_OR_DRAW'] == 'DRAW':
                    run = True  # To stop the main WHILE LOOP
                    print('DRAW !')

                    self.PLAY_BGM_Mode_Complex = False
                    self.PLAY_BGM_Mode_Simple = False
                    self.audio()
                    self.AUDIO_SEFX_WIN.play()
                    self.RESTART = self.result_WIN('DRAW')

                    
              
                elif STATUS['MOUSE_CLICKED']:
                    if self.PLAYER == self.PLAYER_X:
                        self.PLAYER = self.PLAYER_O
                    elif self.PLAYER == self.PLAYER_O:
                        self.PLAYER = self.PLAYER_X
                    
                    GRAVITY = self.Gravity_Value()
                    self.draw_WIN( DRAW_PLAYER_MOVE_BOX = {'DRAW': True, 'RETURN_VALUE': False})
                    print(self.PLAYER, ": MOVE")
        
            self.draw_WIN()    


# When the Python interpreter reads a source file, it sets the special variable __name__ to have a value "__main__" if the script is being run directly by the user.
# If the script is being imported from another module, the __name__ variable will be set to the name of the module.      
if __name__ == "__main__":      
    while True:
        CONNECT_4_GAME = game()
        CONNECT_4_GAME.main()
        if CONNECT_4_GAME.RESTART is False:
            break