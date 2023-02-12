import math

import pygame
import constants


class GameSprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../img/icon.jpg"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def setImage(self, img_link, size):
        self.image = pygame.transform.scale(pygame.image.load(img_link), size)


def createClass(sprite, img_link, size, pos):
    sprite.image = pygame.transform.scale(pygame.image.load(img_link), size)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = pos


class StartButton(GameSprite):
    def __init__(self) -> None:
        createClass(self, "img/title_screen/start_button.png", (200, 120), (130, 340))


class Bookshelf(GameSprite):
    def __init__(self) -> None:
        size = (250, 350)
        pos = (185, 282)
        createClass(self, "img/living_room/bookshelf_default.png", size, pos)

    def pop_book(self, screen, bookpage):
        bookpage.draw(screen)

    # changes the state of the bookshelf
    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/bookshelf_default.png", (250, 350))
        elif state == "init_light_bottom_shelf":
            self.setImage("img/living_room/bookshelf_initial_light_bottom_shelf.png", (250, 350))
        elif state == "init_light_dark_blue":
            self.setImage("img/living_room/bookshelf_initial_light_dark_blue.png", (250, 350))
        elif state == "init_light_sage":
            self.setImage("img/living_room/bookshelf_initial_light_sage.png", (250, 350))
        elif state == "final_light_keypad":
            self.setImage("img/living_room/bookshelf_final_light_keypad.png", (250, 350))
        elif state == "final_nolight":
            self.setImage("img/living_room/bookshelf_final_nolight.png", (250, 350))
        elif state == "final_light_dark_blue":
            self.setImage("img/living_room/bookshelf_final_light_dark_blue.png", (250, 350))
        elif state == "final_light_sage":
            self.setImage("img/living_room/bookshelf_final_light_sage.png", (250, 350))


class BlueBook(GameSprite):
    def __init__(self) -> None:
        size = (600, 400)
        pos = (400, 250)
        createClass(self, "img/living_room/blue_book.png", size, pos)

    def changeState(self, state):
        if state == "visible":
            self.setImage("img/living_room/blue_book.png", (600, 400))
        elif state == "eaten":
            self.setImage("img/living_room/blue_book_chewed.png", (600, 400))


class SageBook(GameSprite):
    def __init__(self) -> None:
        size = (600, 400)
        pos = (400, 250)
        createClass(self, "img/living_room/sage_book.png", size, pos)

    def changeState(self, state):
        if state == "visible":
            self.setImage("img/living_room/sage_book.png", (600, 400))
        elif state == "torn":
            self.setImage("img/living_room/sage_book_torn.png", (600, 400))


class Armchair(GameSprite):
    def __init__(self) -> None:
        size = (180, 220)
        pos = (550, 350)
        createClass(self, "img/living_room/armchair.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/armchair.png", (180, 220))
        elif state == "highlighted":
            self.setImage("img/living_room/armchair_light.png", (180, 220))

    # short ending where the cat retires to bed
    def catSleep(self, screen, ending1):
        ending1.draw(screen)


class Keypad(GameSprite):
    def __init__(self) -> None:
        size = (500, 300)
        pos = (400, 250)
        createClass(self, "img/living_room/keypad.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/keypad.png", (500, 300))
        elif state == "correct":
            self.setImage("img/living_room/keypad_correct.png", (500, 300))
        elif state == "incorrect":
            self.setImage("img/living_room/keypad_incorrect.png", (500, 300))


class RightDoor(GameSprite):
    def __init__(self) -> None:
        size = (64, 315)
        pos = (775, 318)
        createClass(self, "img/living_room/door_right.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/door_right.png", (64, 315))
        elif state == "highlighted":
            self.setImage("img/living_room/door_right_light.png", (64, 315))


class LeftDoor(GameSprite):
    def __init__(self) -> None:
        size = (64, 350)
        pos = (25, 290)
        createClass(self, "img/living_room/door_left.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/door_left.png", (64, 350))
        elif state == "highlighted":
            self.setImage("img/living_room/door_left_light.png", (64, 350))


class SecretDoorRight(GameSprite):
    def __init__(self) -> None:
        size = (64, 315)
        pos = (775, 318)
        createClass(self, "img/secret_lab/door_secret.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/secret_lab/door_secret.png", (64, 315))
        elif state == "highlighted":
            self.setImage("img/secret_lab/door_secret_light.png", (64, 315))


class SecretDoorLeft(GameSprite):
    def __init__(self) -> None:
        size = (64, 350)
        pos = (25, 290)
        createClass(self, "img/living_room/door_secret.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/living_room/door_secret.png", (64, 350))
        elif state == "highlighted":
            self.setImage("img/living_room/door_secret_light.png", (64, 350))


class Fridge(GameSprite):
    def __init__(self) -> None:
        size = (150, 300)
        pos = (650, 275)
        createClass(self, "img/kitchen/fridge.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/kitchen/fridge.png", (150, 300))
        elif state == "highlighted":
            self.setImage("img/kitchen/fridge_light.png", (150, 300))


class Salmon(GameSprite):
    def __init__(self) -> None:
        size = (500, 300)
        pos = (400, 250)
        createClass(self, "img/kitchen/salmon_full.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/kitchen/salmon_full.png", (500, 300))
        elif state == "one_bite":
            self.setImage("img/kitchen/salmon_one.png", (500, 300))
        elif state == "two_bites":
            self.setImage("img/kitchen/salmon_two.png", (500, 300))
        elif state == "finish":
            self.setImage("img/kitchen/salmon_final.png", (500, 300))


class Sink(GameSprite):
    def __init__(self) -> None:
        size = (280, 260)
        pos = (445, 305)
        createClass(self, "img/kitchen/sink.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/kitchen/sink.png", (280, 260))
        elif state == "tap_light":
            self.setImage("img/kitchen/sink_tap_light.png", (280, 260))
        elif state == "default_tap_on":
            self.setImage("img/kitchen/sink_on.png", (280, 260))
        elif state == "sink_door_light":
            self.setImage("img/kitchen/sink_door_light.png", (280, 260))
        elif state == "sink_on_door_light":
            self.setImage("img/kitchen/sink_on_door_light.png", (280, 260))


class Cabinet(GameSprite):
    def __init__(self) -> None:
        size = (500, 300)
        pos = (400, 250)
        createClass(self, "img/kitchen/cabinet.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/kitchen/cabinet.png", (500, 300))
        elif state == "lighter_light":
            self.setImage("img/kitchen/cabinet_lighter_light.png", (500, 300))
        elif state == "empty":
            self.setImage("img/kitchen/cabinet_empty.png", (500, 300))


class Flower(GameSprite):
    def __init__(self) -> None:
        size = (100, 100)
        pos = (200, 200)
        createClass(self, "img/kitchen/flower.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/kitchen/flower.png", (100, 100))
        elif state == "light":
            self.setImage("img/kitchen/flower_light.png", (100, 100))
        elif state == "smash":
            self.setImage("img/kitchen/flower_smash.png", (100, 100))

class Oven(GameSprite):
    def __init__(self) -> None:
        size = (240, 180)
        pos = (205, 335)
        createClass(self, "img/kitchen/oven.png", size, pos)

class LabTable(GameSprite):
    def __init__(self) -> None:
        size = (280, 250)
        pos = (180, 365)
        createClass(self, "img/secret_lab/table.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/secret_lab/table.png", (280, 250))
        elif state == "light":
            self.setImage("img/secret_lab/table_light.png", (280, 250))

class Shelf(GameSprite):
    def __init__(self) -> None:
        size = (350, 400)
        pos = (500, 390)
        createClass(self, "img/secret_lab/shelf.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/secret_lab/shelf.png", (280, 250))
        elif state == "light":
            self.setImage("img/secret_lab/shelf_light.png", (280, 250))
        elif state == "fall":
            self.setImage("img/secret_lab/shelf_fall.png", (280, 250))



class BloodMinigame(GameSprite):
    def __init__(self) -> None:
        size = (500, 300)
        pos = (400, 250)
        createClass(self, "img/secret_lab/blood_minigame.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/secret_lab/blood_minigame.png", (500, 300))
        elif state == "light":
            self.setImage("img/secret_lab/blood_minigame_light.png", (500, 300))
        elif state == "finish":
            self.setImage("img/secret_lab/blood_minigame_finish.png", (500, 300))

class Pentagram(GameSprite):
    def __init__(self) -> None:
        size = (75, 75)
        pos = (660, 535)
        createClass(self, "img/endings/pentagram.png", size, pos)

    def changeState(self, state):
        if state == "default":
            self.setImage("img/endings/pentagram.png", (75, 75))
        elif state == "light":
            self.setImage("img/endings/pentagram_light.png", (75, 75))

class Chaosbar():

    def __init__(self, clean_house) -> None:
        self.clean_house = clean_house

    def default_bar(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 22)
        text = font.render("Chaos bar", True, (255, 255, 255))
        screen.blit(text, (450, 10))
        pygame.draw.rect(screen, (255, 0, 0), (600, 10, 150, 30))  # NEW

    def hit(self, damage_points):
        self.clean_house = self.clean_house - damage_points

    def update(self, screen):
        self.default_bar(screen)  # NEW
        pygame.draw.rect(screen, (0, 128, 0), (600, 10, (15 * (10 - self.clean_house)), 30))

    def damageReport(self):
        damage = (constants.HOUSE_HEALTH - self.clean_house)
        msg = ""
        if damage == 0:
            msg = "Mittens retired from a life of crime"

        elif damage < constants.HOUSE_HEALTH / 3:
            msg = "Minor damage done. Perhaps Mittens has grown fond of his new place"

        elif damage == constants.HOUSE_HEALTH:
            msg = "Master would be proud"
        else:
            msg = "Enough damage has been done"
        return msg


class Countdown():

    def __init__(self) -> None:
        print("ye")

    
    def update(self, seconds, screen):
        font = pygame.font.Font('freesansbold.ttf', 32)
        seconds_left = int(constants.MAX_TIME - seconds)
        minutes_left = math.floor(seconds_left / 60)
        remainder_seconds_left = seconds_left - (minutes_left * 60)

        time_string = ""
        border_width = 0
        if minutes_left > 0:
            time_string = str(minutes_left) + "m " + str(remainder_seconds_left) + "s"
            border_width = 400
        else:
            time_string = str(seconds_left) + "s"
            border_width = 350

        summary = "Remaining time: " + time_string
        text = font.render(summary, True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(15, 15, border_width, 40))
        screen.blit(text, (20, 20))




class Endings():

    def __init__(self) -> None:
        print("ye")

    def draw(self, msg, screen):
        font = pygame.font.Font('freesansbold.ttf', 32)

        summary = "Game over. " + msg
        text = font.render(summary, True, (255, 255, 255))
        screen.blit(text, (100, 200))
