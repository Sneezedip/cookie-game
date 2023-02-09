import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Clicker Game")
white = (255, 255, 255)
font = pygame.font.Font("manaspc.ttf", 20)
font.get_bold()

clicks = 0
upgradex = 0
cps = 0
upgrade1_price = 15
upgrade2_price = 25

last_update = pygame.time.get_ticks()
click_interval = 1000

cookie = pygame.image.load("cookie.png")
cookie_rect = cookie.get_rect()
cookie_rect.center = (150, 150)
cookie_scaled = pygame.transform.scale(cookie, (150, 150))


def loadstats():
    global clicks, upgradex, cps, upgrade1_price, upgrade2_price
    with open("save.txt", "r") as r:
        lines = r.readlines()
        if not lines:
            return
        for line in lines:
            data = line.strip().split(":")
            if len(data) != 2:
                return
            if data[0] == "clicks":
                clicks = int(data[1])
            elif data[0] == "upgradex":
                upgradex = int(data[1])
            elif data[0] == "cps":
                cps = int(data[1])
            elif data[0] == "upgrade1_price":
                upgrade1_price = int(data[1])
            elif data[0] == "upgrade2_price":
                upgrade2_price = int(data[1])


def savestats():
    with open("save.txt", "w") as f:
        f.write(f"Clicks:{clicks}\n")
        f.write(f"Upgradex:{upgradex}\n")
        f.write(f"CPS:{cps}\n")
        f.write(f"Upgrade 1 Price:{upgrade1_price}\n")
        f.write(f"Upgrade 2 Price:{upgrade2_price}\n")


running = True
loadstats()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clicks = clicks
            upgradex = upgradex
            cps = cps
            upgrade1_price = upgrade1_price
            upgrade2_price = upgrade2_price

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if cookie_rect.collidepoint(mouse_pos):
                    clicks += 1 + upgradex
                if upgrade1.collidepoint(mouse_pos):
                    if clicks >= upgrade1_price:
                        clicks -= upgrade1_price
                        upgradex += 1
                        upgrade1_price = upgrade1_price * 2
                        print(f"New price : {upgrade1_price}")
                    else:
                        pass
                if upgrade2.collidepoint(mouse_pos):
                    if clicks >= upgrade2_price:
                        clicks -= upgrade2_price
                        cps += 1
                        upgrade2_price = upgrade2_price * 2
                        print(f"New price : {upgrade2_price}")
                    else:
                        pass

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= click_interval:
        clicks += cps
        last_update = current_time

    screen.fill(white)

    text = font.render(f"Clicks: {clicks}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (200, 20)
    button_text = font.render("UPGRADES", True, (0, 0, 0))
    button_text_rect = button_text.get_rect()
    button_text_rect.center = (200, 230)

    def upgrades():
        global upgrade1, upgrade2
        # drawing rectangle
        if clicks >= upgrade1_price:
            upgrade1 = pygame.draw.rect(
                screen, (250, 250, 250), (15, 265, 70, 50))
        else:
            upgrade1 = pygame.draw.rect(
                screen, (200, 200, 200), (15, 265, 70, 50))
        if clicks >= upgrade2_price:
            upgrade2 = pygame.draw.rect(
                screen, (250, 250, 250), (100, 265, 70, 50))
        else:
            upgrade2 = pygame.draw.rect(
                screen, (200, 200, 200), (100, 265, 70, 50))

        def texts():
            global up_text, up, up_text2, up_text2_rect, up_text_rect, upgrade_text, upgrade_text_rect, upgrade_text2, upgrade_text2_rect
            font1 = pygame.font.Font("manaspc.ttf", 10)
            up_text = font1.render(
                f"{upgrade1_price} CLICKS", True, (0, 50, 250))
            up_text_rect = up_text.get_rect()
            up_text_rect.center = (15 + 35, 265 + -5)
            upgrade_text = font.render("+1 click", True, (255, 0, 0))
            upgrade_text_rect = upgrade_text.get_rect()
            upgrade_text_rect.center = (15 + 35, 265 + 25)

            up_text2 = font1.render(
                f"{upgrade2_price} CLICKS", True, (0, 50, 250))
            up_text2_rect = up_text.get_rect()
            up_text2_rect.center = (100 + 35, 265 + -5)
            upgrade_text2 = font.render("1 cps", True, (255, 0, 0))
            upgrade_text2_rect = upgrade_text2.get_rect()
            upgrade_text2_rect.center = (100 + 35, 265 + 25)

        texts()
        screen.blit(cookie_scaled, (130, 50))
        screen.blit(up_text2, up_text2_rect)
        screen.blit(up_text, up_text_rect)
        screen.blit(upgrade_text, upgrade_text_rect)
        screen.blit(text, text_rect)
        screen.blit(button_text, button_text_rect)
        screen.blit(upgrade_text2, upgrade_text2_rect)

    upgrades()
    savestats()
    pygame.display.update()

pygame.quit()
