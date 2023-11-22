#main
import tkinter as tk
import pygame

def sf(frame):
    frame.tkraise()

pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(loops=-1)

main = tk.Tk()

main.geometry("1000x600")
main.minsize(1000, 600)
main.maxsize(1000, 600)

main.title("ClusterQuest Arcade")

# Frames
game_screen = tk.Frame(main)
load_screen = tk.Frame(main)
for frame in (game_screen, load_screen):
    frame.grid(row=0, column=0, sticky="nsew")

main.rowconfigure(0, weight=1)
main.columnconfigure(0, weight=1)
main.state('zoomed')

# Load Screen Code:
bg = tk.PhotoImage(file="welcome.png")
rpl = tk.Label(load_screen, image=bg).place(relx=0, rely=0)

# Create the game selection textbox
game_selection_textbox = tk.Entry(load_screen, width=20)
game_selection_textbox.place(relx=0.42, rely=0.50)


def handleGameSelection():
    # Get the input from the textbox
    game_number = int(game_selection_textbox.get())

    if game_number == 1:
        rock_paper_scissors()
        sf(game_screen)  # Switch to game screen
    elif game_number == 2:
        flappy_bird()
    elif game_number == 3:
        hangman()
    elif game_number == 4:
        tetris()
    elif game_number == 5:
        sudoku()
    elif game_number == 6:
        minesweeper()
    elif game_number == 7:
        pong()
    elif game_number == 8:
        snake()
    elif game_number == 9:
        tic_tac_toe()
    elif game_number == 10:
        treasure_hunt()


play_button = tk.Button(load_screen, text="Play Game", font="Helvetica 20", padx=10, pady=2, command=lambda: handleGameSelection()).place(relx=0.50, rely=0.45, anchor="center")
exit_button = tk.Button(load_screen, text="Exit", font="Helvetica 20", padx=10, pady=6, command=exit).place(relx=0.50, rely=0.60, anchor="center")



def rock_paper_scissors():
    import tkinter as tk
    import pygame
    import random
    rps = tk.Tk()
    def sf(frame):
        frame.tkraise()
    computer_throws = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }
    # Player throws rock

    def p_rock():
        ct = computer_throws[str(random.randint(1, 3))]
        if ct == "Rock":
            matchres = "Draw"
        elif ct == "Paper":
            matchres = "Computer"
        else:
            matchres = "Player"
        board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=490, y=520, width=290, height=40)
        ptb = tk.Label(game_screen, text="Rock", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=815, y=300, width = 150, height=40)
        ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=310, width = 150, height=40)

    # Player throws paper
    def p_paper():
        ct = computer_throws[str(random.randint(1,3))]
        if ct == "Rock":
            matchres = "Player"
        elif ct == "Paper":
            matchres = "Draw"
        else:
            matchres = "Computer"
        board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=490, y=520, width=290, height=40)
        ptb = tk.Label(game_screen, text="Paper", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=815, y=300, width = 150, height=40)
        ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=310, width = 150, height=40)

    # Player throws scissors
    def p_scissors():
        ct = computer_throws[str(random.randint(1,3))]
        if ct == "Rock":
            matchres = "Computer"
        elif ct == "Paper":
            matchres = "Player"
        else:
            matchres = "Draw"
        board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=490, y=520, width=290, height=40)
        ptb = tk.Label(game_screen, text="Scissors", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=815, y=300, width = 150, height=40)
        ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=310, width = 150, height=40)

    pygame.mixer.init()
    pygame.mixer.music.load("rpsmusic.mp3")
    pygame.mixer.music.play(loops=-1)

    rps.geometry("1000x600")
    rps.minsize(1000, 600)
    rps.maxsize(1000, 600)

    rps.title("Rock Paper Scissors")
    # Frames
    game_screen = tk.Frame(rps)
    load_screen = tk.Frame(rps)
    for frame in (game_screen, load_screen):
        frame.grid(row=0, column=0, sticky="nsew")

    rps.rowconfigure(0, weight=1)
    rps.columnconfigure(0, weight=1)
    rps.state('zoomed')

    # Load Screen code:
    bg = tk.PhotoImage(file="rps1.png")
    rpl = tk.Label(load_screen, image=bg).place(relx=0, rely=0)
    play_button = tk.Button(load_screen, text="Play Game", font="Helvetica 20", padx=10, pady=2, command=lambda: sf(game_screen)).place(relx=0.50, rely=0.85, anchor="center")
    exit_button = tk.Button(load_screen, text="Exit", font="Helvetica 20", padx=10, pady=6, command=exit).place(relx=0.5, rely=0.93, anchor="center")

    # Game Screen Code:
    image = tk.PhotoImage(file="gamescreen.png")
    rpg = tk.Label(game_screen, image=image).place(relx=0, rely=0)
    gs_back = tk.Button(game_screen, text="Back", font="Helvetica 10", command=lambda: sf(load_screen)).place(relx=0.0, rely=0.955)
    rockb = tk.Button(game_screen, text="🪨", font="Commando 15 bold", bg="#d52c0d", fg="black", command=p_rock).place(x=750, y=360)
    paperb = tk.Button(game_screen, text="📄", font="Commando 15 bold", bg="#d52c0d", fg="black", command=p_paper).place(x=750, y=410)
    scissorsb = tk.Button(game_screen, text="✂️", font="Commando 15 bold", bg="#d52c0d", fg="black", command=p_scissors).place(x=750, y=465)

    rps.mainloop()
        




def treasure_hunt():
    def start_adventure():
        print("Welcome to the Adventure of the Lost Realm!")
        print("You find yourself at a crossroads. Which path will you choose?")
        print("1. The Forest Trail")
        print("2. The Mountain Pass")
        print("3. The Deserted Village")

        choice = input("Enter the number of your chosen path: ")

        if choice == "1":
            forest_path()
        elif choice == "2":
            mountain_pass()
        elif choice == "3":
            deserted_village()
        else:
            game_over("Invalid choice. The adventure ends.")

    def forest_path():
        print("\nYou enter a dense forest. Sunlight filters through the leaves, and the air is filled with bird songs.")
        print("As you walk deeper, you encounter a fork in the road.")
        print("1. Take the left path deeper into the forest.")
        print("2. Take the right path leading uphill.")

        choice = input("What will you choose? ")

        if choice == "1":
            forest_clearing()
        elif choice == "2":
            mountain_view()
        else:
            game_over("You stumble and lose your way in the forest.")

    def forest_clearing():
        print("\nYou emerge into a peaceful clearing with a mystical pool at its center.")
        print("A mysterious figure offers you a glowing potion.")
        print("1. Drink the potion and discover hidden memories.")
        print("2. Politely decline and continue exploring.")

        choice = input("What is your decision? ")

        if choice == "1":
            print("\nThe potion reveals forgotten memories, unlocking secret knowledge.")
            print("Congratulations, you have gained wisdom!")
            play_again()
        elif choice == "2":
            print("\nThe figure nods and vanishes into the shadows. You continue your journey.")
            continue_journey()
        else:
            game_over("Your indecision leads to confusion, and you remain in the clearing.")

    def mountain_pass():
        print("\nYou ascend a rugged mountain pass. The air becomes thinner, and the view is breathtaking.")
        print("Ahead, you encounter a mystical creature blocking the path.")
        print("1. Engage in conversation with the creature.")
        print("2. Find an alternative route around the creature.")

        choice = input("What will you do? ")

        if choice == "1":
            creature_encounter()
        elif choice == "2":
            alternative_route()
        else:
            game_over("The creature senses your hesitation and disappears, leaving the path blocked.")
    # ... (previous code)

    def mountain_view():
        print("\nAs you ascend higher, you reach a breathtaking mountain viewpoint.")
        print("The serene landscape stretches below, revealing hidden valleys and distant peaks.")
        print("Congratulations, you've gained a new perspective on your journey!")
        play_again()

    def cave_exploration():
        print("\nYou enter the mysterious cave, discovering ancient markings on the walls.")
        print("The cave leads to a hidden chamber with a sparkling gem.")
        print("1. Touch the gem and unlock its power.")
        print("2. Leave the cave without touching the gem.")

        choice = input("What will you choose? ")

        if choice == "1":
            print("\nThe gem imbues you with magical abilities, enhancing your skills.")
            print("Congratulations, you are now infused with mystical powers!")
            play_again()
        elif choice == "2":
            print("\nYou decide to leave the cave without disturbing its mystical contents.")
            continue_journey()
        else:
            game_over("Your hesitation leaves you lingering in the depths of the cave.")

    # ... (remaining code)

    def creature_encounter():
        print("\nThe creature is a wise guardian of the mountains. It poses a riddle.")
        print("\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\"")
        
        answer = input("Enter your answer: ").lower()

        if answer == "echo":
            print("\nThe creature nods in approval, granting you passage. You continue your climb.")
            continue_journey()
        else:
            game_over("The creature shakes its head, and an unseen force pushes you back down the mountain.")

    def alternative_route():
        print("\nYou search for a hidden path and discover a cave system leading through the mountain.")
        print("1. Enter the cave and explore its mysteries.")
        print("2. Decide to stay on the mountain pass.")

        choice = input("What will you choose? ")

        if choice == "1":
            cave_exploration()
        elif choice == "2":
            print("\nYou decide to stay on the mountain pass, enjoying the scenic view.")
            continue_journey()
        else:
            game_over("Your uncertainty leaves you stuck in a decision loop, unable to proceed.")

    def deserted_village():
        print("\nYou reach a village frozen in time. Empty houses and a haunting silence surround you.")
        print("As you explore, you discover two paths leading to different parts of the village.")
        print("1. Head towards the abandoned marketplace.")
        print("2. Follow the overgrown path to the crumbling castle.")

        choice = input("Which path will you take? ")

        if choice == "1":
            marketplace_discovery()
        elif choice == "2":
            castle_exploration()
        else:
            game_over("Your confusion intensifies, and you remain stuck in the deserted village.")

    def marketplace_discovery():
        print("\nIn the abandoned marketplace, you find remnants of a forgotten civilization.")
        print("A mysterious merchant appears, offering an ancient artifact.")
        print("1. Accept the artifact and uncover its powers.")
        print("2. Politely decline and continue exploring.")

        choice = input("What is your decision? ")

        if choice == "1":
            print("\nThe artifact glows with ancient magic, enhancing your abilities.")
            print("Congratulations, you have gained a powerful ally!")
            play_again()
        elif choice == "2":
            print("\nThe merchant nods and fades away. You continue your exploration.")
            continue_journey()
        else:
            game_over("Your hesitation leaves you lingering in the abandoned marketplace.")

    def castle_exploration():
        print("\nThe crumbling castle hides secrets of a bygone era. You sense a mystical presence within.")
        print("1. Enter the castle and delve into its mysteries.")
        print("2. Choose to bypass the castle and explore the outskirts.")

        choice = input("What will you do? ")

        if choice == "1":
            castle_secrets()
        elif choice == "2":
            print("\nYou decide to explore the outskirts, avoiding the unknown within the castle.")
            continue_journey()
        else:
            game_over("Your indecision echoes in the deserted village, leaving you stuck in uncertainty.")

    def castle_secrets():
        print("\nWithin the castle, you discover ancient chambers filled with magical relics.")
        print("A ghostly figure appears, offering you a choice.")
        print("1. Embrace the magic and unlock your true potential.")
        print("2. Politely decline and seek answers elsewhere.")

        choice = input("What is your decision? ")

        if choice == "1":
            print("\nThe magic transforms you, granting extraordinary abilities.")
            print("Congratulations, you have become a legend!")
            play_again()
        elif choice == "2":
            print("\nThe ghostly figure nods and fades away. You continue your quest for answers.")
            continue_journey()
        else:
            game_over("Your uncertainty lingers, leaving you trapped in the mystical castle.")

    def continue_journey():
        print("\nYou've reached a crossroads once again, with three new paths.")
        print("4. The Cavern of Whispers - A place of ancient secrets.")
        print("5. The Ephemeral Bridge - A bridge that appears only at night.")
        print("6. The Forgotten Temple - A temple obscured by illusions.")

        choice = input("Which path will you choose? ")

        if choice == "4":
            cavern_of_whispers()
        elif choice == "5":
            ephemeral_bridge()
        elif choice == "6":
            forgotten_temple()
        else:
            game_over("Your confusion grows, and the crossroads vanish, leaving you lost in uncertainty.")

    def cavern_of_whispers():
        print("\nYou enter a dark cavern filled with mysterious whispers.")
        print("A glowing orb hovers in the center, radiating ancient knowledge.")
        print("1. Approach the orb and absorb its wisdom.")
        print("2. Choose to leave the cavern and continue your journey.")

        choice = input("What is your decision? ")

        if choice == "1":
            print("\nThe orb shares profound insights, unlocking hidden truths.")
            print("Congratulations, you have gained unparalleled wisdom!")
            play_again()
        elif choice == "2":
            print("\nYou decide to leave the cavern, carrying the whispers with you.")
            continue_journey()
        else:
            game_over("Your indecision echoes in the cavern, leaving you surrounded by whispers.")

    def ephemeral_bridge():
        print("\nThe Ephemeral Bridge appears as the moon rises, connecting two mystical lands.")
        print("A guardian spirit awaits, offering you a choice.")
        print("1. Cross the bridge and explore the unknown land.")
        print("2. Politely decline and wait for the bridge to fade with the dawn.")

        choice = input("What will you do? ")

        if choice == "1":
            print("\nAs you cross the bridge, you discover a realm of dreams and illusions.")
            print("Congratulations, you have transcended reality!")
            play_again()
        elif choice == "2":
            print("\nThe guardian spirit nods, and the bridge fades with the dawn. You continue your journey.")
            continue_journey()
        else:
            game_over("Your uncertainty leaves you stranded between worlds on the ephemeral bridge.")

    def forgotten_temple():
        print("\nThe Forgotten Temple hides amidst illusions, revealing glimpses of its true form.")
        print("An ancient guardian awaits, offering a final challenge.")
        print("1. Accept the challenge and prove your worth.")
        print("2. Politely decline and seek a different path.")

        choice = input("What is your decision? ")

        if choice == "1":
            print("\nYou embrace the challenge, overcoming trials with courage and skill.")
            print("Congratulations, you have proven yourself!")
            play_again()
        elif choice == "2":
            print("\nThe guardian nods, allowing you to choose another path.")
            continue_journey()
        else:
            game_over("Your hesitation echoes in the temple, leaving you surrounded by illusions.")

    def game_over(reason):
        print("\n" + reason)
        print("The adventure concludes. Thank you for playing!")
        play_again()

    def play_again():
        print("\nDo you want to embark on another adventure? (yes or no)")
        choice = input(">").lower()

        if choice == "yes":
            start_adventure()
        else:
            print("\nThank you for playing! Until next time.")

    # Start the adventure
    start_adventure()






def tetris():
    import tkinter as tk
    import pygame
    import random
    from threading import Lock
    import os
    import pygame

    pygame.mixer.init()

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the MP3 file
    mp3_file_path = os.path.join(script_dir, "tetrismusic.mp3")

    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play(loops=-1)

    COLORS = ['black', 'red', 'pink', 'blue', 'orange', 'purple']

    class Tetris():
        FIELD_HEIGHT = 20
        FIELD_WIDTH = 10
        SCORE_PER_ELIMINATED_LINES = (0, 40, 100, 300, 1200)
        TETROMINOS = [
            [(0, 0), (0, 1), (1, 0), (1,1)], # O
            [(0, 0), (0, 1), (1, 1), (2,1)], # L
            [(0, 1), (1, 1), (2, 1), (2,0)], # J 
            [(0, 1), (1, 0), (1, 1), (2,0)], # Z
            [(0, 1), (1, 0), (1, 1), (2,1)], # T
            [(0, 0), (1, 0), (1, 1), (2,1)], # S
            [(0, 1), (1, 1), (2, 1), (3,1)], # I
        ]

        def __init__(self):
            self.field = [[0 for c in range(Tetris.FIELD_WIDTH)] for r in range(Tetris.FIELD_HEIGHT)]
            self.score = 0
            self.level = 0
            self.total_lines_eliminated = 0
            self.game_over = False
            self.move_lock = Lock()
            self.reset_tetromino()

        def reset_tetromino(self):
            self.tetromino = random.choice(Tetris.TETROMINOS)[:]
            self.tetromino_color = random.randint(1, len(COLORS)-1)
            self.tetromino_offset = [-2, Tetris.FIELD_WIDTH//2]
            self.game_over = any(not self.is_cell_free(r, c) for (r, c) in self.get_tetromino_coords())

        def get_tetromino_coords(self):
            return [(r+self.tetromino_offset[0], c + self.tetromino_offset[1]) for (r, c) in self.tetromino]

        def apply_tetromino(self):
            for (r, c) in self.get_tetromino_coords():
                self.field[r][c] = self.tetromino_color

            new_field = [row for row in self.field if any(tile == 0 for tile in row)]
            lines_eliminated = len(self.field)-len(new_field)
            self.total_lines_eliminated += lines_eliminated
            self.field = [[0]*Tetris.FIELD_WIDTH for x in range(lines_eliminated)] + new_field
            self.score += Tetris.SCORE_PER_ELIMINATED_LINES[lines_eliminated] * (self.level + 1)
            self.level = self.total_lines_eliminated // 10
            self.reset_tetromino()

        def get_color(self, r, c):
            return self.tetromino_color if (r, c) in self.get_tetromino_coords() else self.field[r][c]

        def is_cell_free(self, r, c):
            return r < Tetris.FIELD_HEIGHT and 0 <= c < Tetris.FIELD_WIDTH and (r < 0 or self.field[r][c] == 0)

        def move(self, dr, dc):
            with self.move_lock:
                if self.game_over:
                    return

                if all(self.is_cell_free(r + dr, c + dc) for (r, c) in self.get_tetromino_coords()):
                    self.tetromino_offset = [self.tetromino_offset[0] + dr, self.tetromino_offset[1] + dc]
                elif dr == 1 and dc == 0:
                    self.game_over = any(r < 0 for (r, c) in self.get_tetromino_coords())
                    if not self.game_over:
                        self.apply_tetromino()

        def rotate(self):
            with self.move_lock:
                if self.game_over:
                    self.__init__()
                    return

                ys = [r for (r, c) in self.tetromino]
                xs = [c for (r, c) in self.tetromino]
                size = max(max(ys) - min(ys), max(xs)-min(xs))
                rotated_tetromino = [(c, size-r) for (r, c) in self.tetromino]
                wallkick_offset = self.tetromino_offset[:]
                tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
                min_x = min(c for r, c in tetromino_coord)
                max_x = max(c for r, c in tetromino_coord)
                max_y = max(r for r, c in tetromino_coord)
                wallkick_offset[1] -= min(0, min_x)
                wallkick_offset[1] += min(0, Tetris.FIELD_WIDTH - (1 + max_x))
                wallkick_offset[0] += min(0, Tetris.FIELD_HEIGHT - (1 + max_y))

                tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
                if all(self.is_cell_free(r, c) for (r, c) in tetromino_coord):
                    self.tetromino, self.tetromino_offset = rotated_tetromino, wallkick_offset

    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.tetris = Tetris()
            self.pack()
            self.create_widgets()
            self.update_clock()

        def update_clock(self):
            self.tetris.move(1, 0)
            self.update()  
            self.master.after(int(1000*(0.66**self.tetris.level)), self.update_clock)

        def create_widgets(self):
            PIECE_SIZE = 30
            self.canvas = tk.Canvas(self, height=PIECE_SIZE*self.tetris.FIELD_HEIGHT, 
                                        width = PIECE_SIZE*self.tetris.FIELD_WIDTH, bg="black", bd=0)
            self.canvas.bind('<Left>', lambda _: (self.tetris.move(0, -1), self.update()))
            self.canvas.bind('<Right>', lambda _: (self.tetris.move(0, 1), self.update()))
            self.canvas.bind('<Down>', lambda _: (self.tetris.move(1, 0), self.update()))
            self.canvas.bind('<Up>', lambda _: (self.tetris.rotate(), self.update()))
            self.canvas.focus_set()
            self.rectangles = [
                self.canvas.create_rectangle(c*PIECE_SIZE, r*PIECE_SIZE, (c+1)*PIECE_SIZE, (r+1)*PIECE_SIZE)
                    for r in range(self.tetris.FIELD_HEIGHT) for c in range(self.tetris.FIELD_WIDTH)
            ]
            self.canvas.pack(side="left")
            self.status_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24))
            self.status_msg.pack(side="top")
            self.game_over_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24), fg='red')
            self.game_over_msg.pack(side="top")

        def update(self):
            for i, _id in enumerate(self.rectangles):
                color_num = self.tetris.get_color(i//self.tetris.FIELD_WIDTH, i % self.tetris.FIELD_WIDTH)
                self.canvas.itemconfig(_id, fill=COLORS[color_num])

            self.status_msg['text'] = "Score: {}\nLevel: {}".format(self.tetris.score, self.tetris.level)
            self.game_over_msg['text'] = "GAME OVER.\nPress UP\nto reset" if self.tetris.game_over else ""

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()





def hangman():
    import pygame
    import random
    import pygame
    import os 
    pygame.mixer.init()

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the MP3 file
    mp3_file_path = os.path.join(script_dir, "hangman music.mp3")

    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play(loops=-1)
    pygame.init()

    winHeight = 480
    winWidth = 700
    win=pygame.display.set_mode((winWidth,winHeight))

    BLACK = (0,0, 0)
    WHITE = (255,255,255)
    RED = (255,0, 0)
    PINK = (255, 182, 193)
    YELLOW = (255, 255, 0)
    
    btn_font = pygame.font.SysFont("arial", 20)
    guess_font = pygame.font.SysFont("monospace", 24)
    lost_font = pygame.font.SysFont('arial', 20)
    word = ''
    buttons = []
    guessed = []
    hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

    limbs = 0


    def redraw_game_window():
        nonlocal guessed
        nonlocal hangmanPics
        nonlocal limbs
        win.fill(PINK)
        # Buttons
        for i in range(len(buttons)):
            if buttons[i][4]:
                pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
                pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                                )
                label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
                win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

        spaced = spacedOut(word, guessed)
        label1 = guess_font.render(spaced, 1, BLACK)
        rect = label1.get_rect()
        length = rect[2]
        
        win.blit(label1,(winWidth/2 - length/2, 400))

        pic = hangmanPics[limbs]
        win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
        pygame.display.update()


    def randomWord():
        file = open('words.txt')
        f = file.readlines()
        i = random.randrange(0, len(f) - 1)

        return f[i][:-1]


    def hang(guess):
        nonlocal word
        if guess.lower() not in word.lower():
            return True
        else:
            return False


    def spacedOut(word, guessed=[]):
        spacedWord = ''
        guessedLetters = guessed
        for x in range(len(word)):
            if word[x] != ' ':
                spacedWord += '_ '
                for i in range(len(guessedLetters)):
                    if word[x].upper() == guessedLetters[i]:
                        spacedWord = spacedWord[:-2]
                        spacedWord += word[x].upper() + ' '
            elif word[x] == ' ':
                spacedWord += ' '
        return spacedWord
                

    def buttonHit(x, y):
        for i in range(len(buttons)):
            if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
                if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                    return buttons[i][5]
        return None


    def end(winner=False):
        nonlocal limbs
        lostTxt = 'You lost. Press any key to play again.'
        winTxt = 'WINNER! Press any key to play again.'
        redraw_game_window()
        pygame.time.delay(1000)
        win.fill(PINK)

        if winner == True:
            label = lost_font.render(winTxt, 1, BLACK)
        else:
            label = lost_font.render(lostTxt, 1, BLACK)

        wordTxt = lost_font.render(word.upper(), 1, BLACK)
        wordWas = lost_font.render('The word was: ', 1, BLACK)

        win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
        win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
        win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
        pygame.display.update()
        again = True
        while again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    again = False
        reset()


    def reset():
        nonlocal limbs
        nonlocal guessed
        nonlocal buttons
        nonlocal word
        for i in range(len(buttons)):
            buttons[i][4] = True

        limbs = 0
        guessed = []
        word = randomWord()

    #MAINLINE


    # Setup buttons
    increase = round(winWidth / 13)
    for i in range(26):
        if i < 13:
            y = 40
            x = 25 + (increase * i)
        else:
            x = 25 + (increase * (i - 13))
            y = 85
        buttons.append([YELLOW, x, y, 20, True, 65 + i])
        # buttons.append([color, x_pos, y_pos, radius, visible, char])

    word = randomWord()
    inPlay = True

    while inPlay:
        redraw_game_window()
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickPos = pygame.mouse.get_pos()
                letter = buttonHit(clickPos[0], clickPos[1])
                if letter != None:
                    guessed.append(chr(letter))
                    buttons[letter - 65][4] = False
                    if hang(chr(letter)):
                        if limbs != 5:
                            limbs += 1
                        else:
                            end()
                    else:
                        print(spacedOut(word, guessed))
                        if spacedOut(word, guessed).count('_') == 0:
                            end(True)

    pygame.quit()





from tkinter import *

def minesweeper():
    from tkinter import messagebox as tkMessageBox
    import random
    import platform
    from datetime import datetime
    from collections import deque
    import pygame

    SIZE_X = 10
    SIZE_Y = 10

    STATE_DEFAULT = 0
    STATE_CLICKED = 1
    STATE_FLAGGED = 2

    BTN_CLICK = "<Button-1>"
    BTN_FLAG = "<Button-2>" if platform.system() == 'Darwin' else "<Button-3>"

    window = None
    pygame.mixer.init()

    class Minesweeper:

        def __init__(self, tk):

            # import images
            self.images = {
                "plain": PhotoImage(file="tile_plain.png"),
                "clicked": PhotoImage(file="tile_clicked.png"),
                "mine": PhotoImage(file="tile_mine.png"),
                "flag": PhotoImage(file="tile_flag.png"),
                "wrong": PhotoImage(file="tile_wrong.png"),
                "numbers": []
            }
            for i in range(1, 9):
                self.images["numbers"].append(PhotoImage(file="tile_" + str(i) + ".png"))

            # set up frame
            self.tk = tk
            self.frame = Frame(self.tk)
            self.frame.pack()

            self.start_button = Button(self.frame, text="Start", command=self.restart)
            self.start_button.grid(row=SIZE_X + 2, column=0, columnspan=SIZE_Y)

            self.game_sound = pygame.mixer.Sound("04 Jingle #01.mp3")

            # set up labels/UI
            self.labels = {
                "time": Label(self.frame, text="00:00:00"),
                "mines": Label(self.frame, text="Mines: 0"),
                "flags": Label(self.frame, text="Flags: 0")
            }
            self.labels["time"].grid(row=0, column=0, columnspan=SIZE_Y)  # top full width
            self.labels["mines"].grid(row=SIZE_X + 1, column=0, columnspan=int(SIZE_Y / 2))  # bottom left
            self.labels["flags"].grid(row=SIZE_X + 1, column=int(SIZE_Y / 2) - 1, columnspan=int(SIZE_Y / 2))  # bottom right

            self.restart()  # start game
            self.updateTimer()  # init timer

        def setup(self):
            # flag and clicked tile variables
            self.flagCount = 0
            self.correctFlagCount = 0
            self.clickedCount = 0
            self.startTime = None

            # buttons
            self.tiles = dict({})
            self.mines = 0
            for x in range(0, SIZE_X):
                for y in range(0, SIZE_Y):
                    if y == 0:
                        self.tiles[x] = {}

                    id = str(x) + "_" + str(y)
                    isMine = False

                    # tile image changeable for debug reasons:
                    gfx = self.images["plain"]

                    # currently random amount of mines
                    if random.uniform(0.0, 1.0) < 0.1:
                        isMine = True
                        self.mines += 1

                    tile = {
                        "id": id,
                        "isMine": isMine,
                        "state": STATE_DEFAULT,
                        "coords": {
                            "x": x,
                            "y": y
                        },
                        "button": Button(self.frame, image=gfx),
                        "mines": 0  # calculated after grid is built
                    }

                    tile["button"].bind(BTN_CLICK, self.onClickWrapper(x, y))
                    tile["button"].bind(BTN_FLAG, self.onRightClickWrapper(x, y))
                    tile["button"].grid(row=x + 1, column=y)  # offset by 1 row for timer

                    self.tiles[x][y] = tile

            # loop again to find nearby mines and display the number on the tile
            for x in range(0, SIZE_X):
                for y in range(0, SIZE_Y):
                    mc = 0
                    for n in self.getNeighbors(x, y):
                        mc += 1 if n["isMine"] else 0
                    self.tiles[x][y]["mines"] = mc

        def restart(self):
            self.setup()
            self.refreshLabels()

        def refreshLabels(self):
            self.labels["flags"].config(text="Flags: " + str(self.flagCount))
            self.labels["mines"].config(text="Mines: " + str(self.mines))

        def gameOver(self, won):
            for x in range(0, SIZE_X):
                for y in range(0, SIZE_Y):
                    if self.tiles[x][y]["isMine"] == False and self.tiles[x][y]["state"] == STATE_FLAGGED:
                        self.tiles[x][y]["button"].config(image=self.images["wrong"])
                    if self.tiles[x][y]["isMine"] == True and self.tiles[x][y]["state"] != STATE_FLAGGED:
                        self.tiles[x][y]["button"].config(image=self.images["mine"])

            self.tk.update()

            msg = "You Win! Play again?" if won else "You Lose! Play again?"
            res = tkMessageBox.askyesno("Game Over", msg)
            if won:
                self.game_sound.play()
            else:
                self.game_sound.play()
            if res:
                self.restart()
            else:
                self.tk.quit()

        def updateTimer(self):
            ts = "00:00:00"
            if self.startTime != None:
                delta = datetime.now() - self.startTime
                ts = str(delta).split('.')[0]  # drop ms
                if delta.total_seconds() < 36000:
                    ts = "0" + ts  # zero-pad
            self.labels["time"].config(text=ts)
            self.frame.after(100, self.updateTimer)

        def getNeighbors(self, x, y):
            neighbors = []
            coords = [
                {"x": x - 1, "y": y - 1},  # top right
                {"x": x - 1, "y": y},  # top middle
                {"x": x - 1, "y": y + 1},  # top left
                {"x": x, "y": y - 1},  # left
                {"x": x, "y": y + 1},  # right
                {"x": x + 1, "y": y - 1},  # bottom right
                {"x": x + 1, "y": y},  # bottom middle
                {"x": x + 1, "y": y + 1},  # bottom left
            ]
            for n in coords:
                try:
                    neighbors.append(self.tiles[n["x"]][n["y"]])
                except KeyError:
                    pass
            return neighbors

        def onClickWrapper(self, x, y):
            return lambda event: self.onClick(self.tiles[x][y])

        def onRightClickWrapper(self, x, y):
            return lambda event: self.onRightClick(self.tiles[x][y])

        def onClick(self, tile):
            if self.startTime == None:
                self.startTime = datetime.now()

            if tile["isMine"] == True:
                # end game
                self.gameOver(False)
                return

            # change image
            if tile["mines"] == 0:
                tile["button"].config(image=self.images["clicked"])
                self.clearSurroundingTiles(tile["id"])
            else:
                tile["button"].config(image=self.images["numbers"][tile["mines"] - 1])
            # if not already set as clicked, change state and count
            if tile["state"] != STATE_CLICKED:
                tile["state"] = STATE_CLICKED
                self.clickedCount += 1
            if self.clickedCount == (SIZE_X * SIZE_Y) - self.mines:
                self.gameOver(True)

        def onRightClick(self, tile):
            if self.startTime == None:
                self.startTime = datetime.now()

            # if not clicked
            if tile["state"] == STATE_DEFAULT:
                tile["button"].config(image=self.images["flag"])
                tile["state"] = STATE_FLAGGED
                tile["button"].unbind(BTN_CLICK)
                # if a mine
                if tile["isMine"] == True:
                    self.correctFlagCount += 1
                self.flagCount += 1
                self.refreshLabels()
            # if flagged, unflag
            elif tile["state"] == 2:
                tile["button"].config(image=self.images["plain"])
                tile["state"] = 0
                tile["button"].bind(BTN_CLICK, self.onClickWrapper(tile["coords"]["x"], tile["coords"]["y"]))
                # if a mine
                if tile["isMine"] == True:
                    self.correctFlagCount -= 1
                self.flagCount -= 1
                self.refreshLabels()

        def clearSurroundingTiles(self, id):
            queue = deque([id])

            while len(queue) != 0:
                key = queue.popleft()
                parts = key.split("_")
                x = int(parts[0])
                y = int(parts[1])

                for tile in self.getNeighbors(x, y):
                    self.clearTile(tile, queue)

        def clearTile(self, tile, queue):
            if tile["state"] != STATE_DEFAULT:
                return

            if tile["mines"] == 0:
                tile["button"].config(image=self.images["clicked"])
                queue.append(tile["id"])
            else:
                tile["button"].config(image=self.images["numbers"][tile["mines"] - 1])

            tile["state"] = STATE_CLICKED
            self.clickedCount += 1


    ### END OF CLASSES ###

    def main():
        # create Tk instance
        window = Tk()
        # set program title
        window.title("Minesweeper")
        # create game instance
        Minesweeper(window)
        # run event loop
        window.mainloop()

    if __name__ == "__main__":
        main()




def pong():
    import pygame

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    pygame.init()

    # Initializing the display window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pong")

    # Starting coordinates of the paddle
    rect_x = 400
    rect_y = 580

    # Initial speed of the paddle
    rect_change_x = 0
    rect_change_y = 0

    # Initial position of the ball
    ball_x = 50
    ball_y = 50

    # Speed of the ball
    ball_change_x = 5
    ball_change_y = 5

    score = 0

    # Load the bounce sound
    pygame.mixer.music.load("/Users/anushkasharma/Documents/GitHub/Pong/bounce.wav")

    # Draws the paddle. Also restricts its movement between the edges
    # of the window.
    def drawrect(screen, x, y):
        if x <= 0:
            x = 0
        if x >= 699:
            x = 699
        pygame.draw.rect(screen, RED, [x, y, 100, 20])


    # Game's main loop
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_change_x = -6
                elif event.key == pygame.K_RIGHT:
                    rect_change_x = 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    rect_change_x = 0

        screen.fill(BLACK)
        rect_x += rect_change_x
        rect_y += rect_change_y

        ball_x += ball_change_x
        ball_y += ball_change_y

        # This handles the movement of the ball.
        if ball_x < 0:
            ball_x = 0
            ball_change_x = ball_change_x * -1
            pygame.mixer.music.play()
        elif ball_x > 785:
            ball_x = 785
            ball_change_x = ball_change_x * -1
            pygame.mixer.music.play()
        elif ball_y < 0:
            ball_y = 0
            ball_change_y = ball_change_y * -1
            pygame.mixer.music.play()
        elif ball_x > rect_x and ball_x < rect_x + 100 and ball_y == 565:
            ball_change_y = ball_change_y * -1
            score = score + 1
            pygame.mixer.music.play()
        elif ball_y > 600:
            ball_change_y = ball_change_y * -1
            score = 0
            pygame.mixer.music.play()

        pygame.draw.rect(screen, WHITE, [ball_x, ball_y, 15, 15])
        drawrect(screen, rect_x, rect_y)

        # Scoreboard
        font = pygame.font.SysFont('Calibri', 15, False, False)
        text = font.render("Score = " + str(score), True, WHITE)
        screen.blit(text, [600, 100])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()






def snake():
    import pygame
    import time
    import random
    
    pygame.init()
    
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    
    dis_width = 600
    dis_height = 400
    
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')
    
    clock = pygame.time.Clock()
    
    snake_block = 10
    snake_speed = 15
    
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    
    
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])
    
    
    
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    
    
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
    
    def gameLoop():
        game_over = False
        game_close = False
    
        x1 = dis_width / 2
        y1 = dis_height / 2
    
        x1_change = 0
        y1_change = 0
    
        snake_List = []
        Length_of_snake = 1
    
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
        while not game_over:
    
            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
    
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
    
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
    
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
    
            pygame.display.update()
    
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
    
            clock.tick(snake_speed)
    
        pygame.quit()
        quit()
    
    
    gameLoop()







def tic_tac_toe():
    import tkinter as tk            
    from tkinter import messagebox    #messagebox is a module within tkinter
    '''0,0      0,1      0,2
    1,0      1,1      1,2
    2,0      2,1      2,2'''

    def check_winner():                #to determine if a player has won the game
        for row in board:             #iterates through each row
            if len(set(row)) == 1 and row[0] != 0:        #checks if all elements in row are equal and first element in a row is not empty,indicating a winner in that row
                return True

        for col in range(3):               #iterates through each column 
            if board[0][col] == board[1][col] == board[2][col] != 0:            #checks if all elements in column are filled,indicating a winner in that row
                return True

        if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:     #checks if there is a winner in both diagonals
            return True

        return False             #returns false if no winner is found

    def check_draw():
        return all(cell != 0 for row in board for cell in row)    #checks if clicked cell is empty and there is no winner yet,here all function check if condition holds for all cells

    def on_click(row, col):     #this function is called when a button on game grid is clicked
        nonlocal current_player

        if board[row][col] == 0 and not winner:       
            board[row][col] = current_player              #updates the board with the current player's move
            buttons[row][col].config(text=players[current_player], state=tk.DISABLED)    #updates button text to display player's symbol and disables the button after the move

            if check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {players[current_player]} wins!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                reset_game()
            else:
                current_player = 1 if current_player == 2 else 2       #switches the current player

    def reset_game():              #to reset game variable and button states
        nonlocal board, winner, current_player
        board = [[0, 0, 0] for _ in range(3)]           #initialize the game board as 3*3 matrix filled with zeroes
        winner = False
        current_player = 1
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text="", state=tk.NORMAL)      #configures each button on grid with default setting

    # Initialize the game
    board = [[0, 0, 0] for _ in range(3)]   #re-initialize the board after resetting
    winner = False
    current_player = 1
    players = {1: "X", 2: "O"}   #dictionary mapping player number to their symbols

    # Create the main window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Create buttons for the game grid
    buttons = [[tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i, j=j: on_click(i, j)) for j in range(3)] for i in range(3)]

    # Place buttons on the grid
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=i, column=j)    #place each button on grid

    # Create a Reset button
    reset_button = tk.Button(root, text="Reset", command=reset_game)   #here root means we are saying that put this button in a main window
    reset_button.grid(row=3, column=1)      #place the reset button on grid

    # Run the Tkinter event loop
    root.mainloop()





from tkinter import *         #import all the functionality of the tkinter module 

def sudoku():
    #import necessary libraries
    import tkinter
    import random
    #guess = str()
    #initialize a 9*9 sudoku grid with zeroes
    grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    #creating tkinter window
    root = Tk()
    root.title("Sudoku")
    root.minsize(width=500, height=635)        #size of the window
    root.attributes("-alpha", 0.90)
    root.configure(background="#282828")

    title = Label(root, text='Sudoku', fg="#FFFF00",font="Geneva 30",bg="#282828")
    title.pack()      #pack organizes and displays the label in the window.

    box = Canvas(root, width = 435, height = 435,background="#282828",bd=6, highlightthickness=6)    #Canvas is used to create a drawing area
    box.pack()

    entry_list = [[],[],[]]
    var =[]
    done = False

    def one_grid(row):
        nonlocal grid,entry_list
        g1 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        entry_list[0].append(g1)
        g1.place(x = 5,y = 5)
        g2 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        entry_list[0].append(g2)
        g2.place(x = 52,y = 5)
        g3 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g3.place(x = 102,y = 5)
        entry_list[0].append(g3)
        g4 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g4.place(x = 5,y = 52)
        entry_list[1].append(g4)
        g5 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g5.place(x = 52,y = 52)
        entry_list[1].append(g5)
        g6 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g6.place(x = 102,y = 52)
        entry_list[1].append(g6)
        g7 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g7.place(x = 5,y = 102)
        entry_list[2].append(g7)
        g8 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g8.place(x = 52,y = 102)
        entry_list[2].append(g8)
        g9 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
        g9.place(x = 102,y = 102)
        entry_list[2].append(g9)

    def display_val():
        nonlocal entry_list
        u=0
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(grid[u][y] != 0):
                    a_splited[0][y].insert(0,grid[u][y]) 
            u+=1
        u=3
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(grid[u][y] != 0):
                    a_splited[1][y].insert(0,grid[u][y]) 
            u+=1
            
        u=6
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(grid[u][y] != 0):
                    a_splited[2][y].insert(0,grid[u][y]) 
            u+=1
                
                

    def clear():
        nonlocal grid
        grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    def scramble():
        nonlocal grid
        clear()
        for a in entry_list:
            for b in a:
                b.delete(first=0,last=100)
        amount = 20

        
        for i in range(amount):
            y = random.randint(0,len(grid)-1)
            x = random.randint(0,len(grid)-1)
            num = random.randint(1,len(grid))
            allow = 0
            for e in range(len(grid)):
                if num not in grid[x] and num != grid[e][y]:
                    allow +=1
            grid[x][y] = num
            tempo = grid     
            tempo = rearrange(tempo)
            
            for e in range(len(grid)):
                if(duplicate_checker(tempo[e])):
                    allow = 0
            if allow !=len(grid):
                grid[x][y] = 0
                
        display_val()


    def stay(num,x,y):

        for e in range(9):
            if grid[y][e] ==num:
                return False
        for e in range(9):
            if grid[e][x] ==num:
                return False

        for i in range(3):
            for e in range(3):
                if grid[((y//3)*3)+i][((x//3)*3)+e] ==num:
                    return False
        return True

    def pressed_solve():
        nonlocal grid,done
        done =False
        solver()
    def solver():
        nonlocal grid,done
        
        if(done ==False):
            
            for y in range(9):
                for x in range(9):
                    if grid[y][x] == 0:
                        for num in range(1,10):
                            if stay(num,x,y):
                                grid[y][x]=num
                                solver()
                                grid[y][x]=0
                        return
            done =True
            for a in entry_list:
                for b in a:
                    b.delete(first=0,last=100)
            display_val()
            
            return

    def rearrange(a):
        temp=[[],[],[],[],[],[],[],[],[]]
        count =0
        ch = 0
        for e in range(len(a)):
            for x in range(3):
                if(a[e][x]!=0):
                    temp[ch].append(a[e][x])
            count+=1
            if(count ==3):
                ch+=1
                count = 0
        for e in range(len(a)):
            for x in range(3,6):
                if(a[e][x]!=0):
                    temp[ch].append(a[e][x])
            count+=1
            if(count ==3):
                ch+=1
                count = 0
        for e in range(len(a)):
            for x in range(6,9):
                if(a[e][x]!=0):
                    temp[ch].append(a[e][x])
            count+=1
            if(count ==3):
                ch+=1
                count = 0
        return temp

    def duplicate_checker(a):
            b = set(a)
            result = len(a) != len(b)
            #print(result)
            if(result == True):
                return True
                
    def checkrow_horz(a):
        for x in a:
            if(duplicate_checker(x) == True):
                return True
            
            
    def checkrow_vert(a):
        for y in range(len(a)):
            temp = []
            for x in a:
                temp.append(x[y])
            if(duplicate_checker(temp) == True):
                return True
                
    def checkcol(a):
        for y in range(3):
            temp = []
            for x in range(int(len(a)/3)):
                temp.append(a[x][3*y])
                temp.append(a[x][3*y+1])
                temp.append(a[x][3*y+2])
            if(duplicate_checker(temp) == True):
                return True
                temp = []
            for x in range(3,(int(len(a)/3))*2):
                temp.append(a[x][3*y])
                temp.append(a[x][3*y+1])
                temp.append(a[x][3*y+2])
            if(duplicate_checker(temp) == True):
                return True
            temp = []
            for x in range(6,(int(len(a)/3))*3):
                temp.append(a[x][3*y])
                temp.append(a[x][3*y+1])
                temp.append(a[x][3*y+2])
                if(duplicate_checker(temp) == True):
                    return True
            
    def submit():
        nonlocal entry_list
        
        temp = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        u=0
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(a_splited[0][y].get() != '' ):
                    temp[u][y]= int(a_splited[0][y].get())
            u+=1
        u=3
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(a_splited[1][y].get() != '' ):
                    temp[u][y]= int(a_splited[1][y].get())
            u+=1
            
        u=6
        for a in entry_list:
            a_splited = [a[x:x+9] for x in range(0, len(a), 9)]
            for y in range(9):
                if(a_splited[2][y].get() != '' ):
                    temp[u][y]= int(a_splited[2][y].get())
            u+=1
                
        if(checkrow_horz(temp) == True or checkrow_vert(temp) ==True or checkcol(temp) ==True):
            wrong()
        else:
            correct()

    def wrong():
        title.config(fg="#990000",text="Try Again")
        row1.config(highlightbackground="#990000")
        row2.config(highlightbackground="#990000")
        row3.config(highlightbackground="#990000")
        row4.config(highlightbackground="#990000")
        row5.config(highlightbackground="#990000")
        row6.config(highlightbackground="#990000")
        row7.config(highlightbackground="#990000")
        row8.config(highlightbackground="#990000")
        row9.config(highlightbackground="#990000")
        row1.after(2100, lambda: row1.config(highlightbackground="white"))
        row2.after(2100, lambda: row2.config(highlightbackground="white"))
        row3.after(2100, lambda: row3.config(highlightbackground="white"))
        row4.after(2100, lambda: row4.config(highlightbackground="white"))
        row5.after(2100, lambda: row5.config(highlightbackground="white"))
        row6.after(2100, lambda: row6.config(highlightbackground="white"))
        row7.after(2100, lambda: row7.config(highlightbackground="white"))
        row8.after(2100, lambda: row8.config(highlightbackground="white"))
        row9.after(2100, lambda: row9.config(highlightbackground="white"))
        title.after(2100, lambda: title.config(fg="#382888",text ="Sudoku"))

    def correct():
        title.config(fg="#288888",text="Correct")
        row1.config(highlightbackground="#288888")
        row2.config(highlightbackground="#288888")
        row3.config(highlightbackground="#288888")
        row4.config(highlightbackground="#288888")
        row5.config(highlightbackground="#288888")
        row6.config(highlightbackground="#288888")
        row7.config(highlightbackground="#288888")
        row8.config(highlightbackground="#288888")
        row9.config(highlightbackground="#288888")
        row1.after(2100, lambda: row1.config(highlightbackground="white"))
        row2.after(2100, lambda: row2.config(highlightbackground="white"))
        row3.after(2100, lambda: row3.config(highlightbackground="white"))
        row4.after(2100, lambda: row4.config(highlightbackground="white"))
        row5.after(2100, lambda: row5.config(highlightbackground="white"))
        row6.after(2100, lambda: row6.config(highlightbackground="white"))
        row7.after(2100, lambda: row7.config(highlightbackground="white"))
        row8.after(2100, lambda: row8.config(highlightbackground="white"))
        row9.after(2100, lambda: row9.config(highlightbackground="white"))
        title.after(2100, lambda: title.config(fg="#382888",text ="Sudoku"))


    row1 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row1)
    row1.place(x = 0,y = 0)
    row2 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row2)
    row2.place(x = 150,y = 0)
    row3 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row3)
    row3.place(x = 300,y = 0)

    row4 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row4)
    row4.place(x = 0,y = 150)
    row5 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row5)
    row5.place(x = 150,y = 150)
    row6 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row6)
    row6.place(x = 300,y = 150)

    row7 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row7)
    row7.place(x = 0,y = 300)
    row8 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row8)
    row8.place(x = 150,y = 300)
    row9 = Canvas(box, width = 120, height = 120,background="#282828",bd=10, highlightthickness=10)
    one_grid(row9)
    row9.place(x = 300,y = 300)

    scramble()


    but = Canvas(root, width = 500, height = 45,background="#282828",bd=13, highlightthickness=0)  
    but.pack()
    enter = Button(but,text ="Submit", fg="#282828",command=submit, font="Geneva 30 bold",bg='#6495ED',activebackground='#6495ED',highlightbackground="#6495ED",disabledforeground="#6495ED",justify=CENTER)
    enter.configure(bg='#6495ED',width = 12)
    enter.place(x = 0,y = 10)
    reset = Button(but,text ="Reset", fg="#282828",command=scramble, font="Geneva 30 bold",bg='#53BDA5',activebackground='#53BDA5',highlightbackground="#53BDA5",disabledforeground="#53BDA5",justify=CENTER)
    reset.configure(bg='#53BDA5',width = 12)
    reset.place(x = 250,y = 10)
    solve = Button(root,text ="Solve", fg="#282828",command=pressed_solve, font="Geneva 30 bold",bg='#FCD4D4',activebackground='#FCD4D4',highlightbackground="#FCD4D4",disabledforeground="#FCD4D4",justify=CENTER)
    solve.configure(bg='#FCD4D4',width = 12)
    solve.place(x = 120,y = 575)



    root.mainloop()





from pygame.locals import * # Basic pygame imports


def flappy_bird():
    import random # For generating random numbers
    import sys # To exit the program
    import pygame

    FPS = 45
    SCREENWIDTH = 289
    SCREENHEIGHT = 511
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}
    PLAYER = 'gallery/sprites/bird.png'
    BACKGROUND = 'gallery/sprites/background.png'
    PIPE = 'gallery/sprites/pipe.png'

    def welcomeScreen():
        
        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    return
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping


        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()


            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    print(f"Your score is {score}") 
                    GAME_SOUNDS['point'].play()


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            GAME_SOUNDS['hit'].play()
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                GAME_SOUNDS['hit'].play()
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe






    if __name__ == "__main__":
        # This will be the main point from where our game will start
        pygame.init() # Initialize all pygame's modules
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )

        # Game sounds
        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

        while True:
            welcomeScreen() # Shows welcome screen to the user until he presses a button
            mainGame() # This is the main game function 



main.mainloop()

