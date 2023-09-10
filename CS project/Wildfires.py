import pygame
from PIL import Image
import pygame

def draw_rounded_rectangle(window, color, rectangle, corner_radius):
    mainrect = pygame.Rect(rectangle)
    toprect = pygame.Rect(rectangle[0], rectangle[1] - corner_radius, rectangle[2], rectangle[3] + 2 * corner_radius)
    bottomrect = pygame.Rect(rectangle[0] - corner_radius, rectangle[1], rectangle[2] + 2 * corner_radius, rectangle[3])
    
    pygame.draw.rect(window, color, mainrect)
    pygame.draw.circle(window, color, (mainrect.left, mainrect.top), corner_radius)
    pygame.draw.circle(window, color, (mainrect.right, mainrect.top), corner_radius)
    pygame.draw.circle(window, color, (mainrect.left, mainrect.bottom), corner_radius)
    pygame.draw.circle(window, color, (mainrect.right, mainrect.bottom), corner_radius)
    pygame.draw.rect(window, color, toprect)
    pygame.draw.rect(window, color, bottomrect)
def scale(image, scalefactor):
    image = pygame.transform.scale(image, (int(image.get_width() * scalefactor), int(image.get_height() * scalefactor)))
    return image
def over_rect(rectangle, corner_radius = 0):
    rectangle = pygame.Rect(rectangle)
    x, y = pygame.mouse.get_pos()
    if x > rectangle.left - corner_radius and x < rectangle.right + corner_radius and y > rectangle.top - corner_radius and y < rectangle.bottom + corner_radius:
        return True
    else:
        return False

pygame.init()
window = pygame.display.set_mode([1000, 1000])
counties = pygame.image.load("Washington-00.png")
pin = pygame.image.load("1200px-Google_Maps_pin.svg.png")
warning = pygame.image.load("warning-removebg-preview.png")
warning = scale(warning, 0.07)
fire = pygame.image.load("fire-removebg-preview.png")
fire = scale(fire, 0.04)
scale_factor = 1000 / counties.get_width()
counties = pygame.transform.scale(counties, (1000, int(counties.get_height() * scale_factor)))
pin = scale(pin, 0.075)
font = pygame.font.Font("Roboto-Black.ttf", 30)
countieslist = [["Adams", 791, 508], ["Asotin", 937, 635], ["Benton", 660, 607], ["Chelan", 553, 337], ["Clallam", 147, 315], ["Clark", 302, 713], ["Columbia", 851, 611], ["Cowlitz", 287, 636], 
                ["Douglis", 649, 356], ["Ferry", 779, 241], ["Franklin", 721, 583], ["Garfield", 895, 583], ["Grant", 667, 486], ["Grays Harbor", 145, 465], ["Island", 284, 282], ["Jefferson", 161, 367], 
                ["King", 353, 404], ["Kitsap", 285, 395], ["Kittitas", 526, 478], ["Klickitat", 482, 699], ["Lewis", 304, 575], ["Lincoln", 777, 409], ["Mason", 215, 429], ["Okanogan", 643, 226], ["Pacific", 165, 577], 
                ["Pend Oreille", 929, 217], ["Pierce", 341, 483], ["San Juan", 241, 228], ["Skagit", 413, 230], ["Skamania", 379, 653], ["Snohomish", 392, 306], ["Spokane", 913, 395], ["Stevens", 853, 243], 
                ["Thurston", 259, 507], ["Wahkiakum", 196, 615], ["Walla Walla", 786, 631], ["Whatcom", 411, 178], ["Whitman", 907, 505], ["Yakima", 520, 599]]
markerstodisplay = []
countyon = 0
selected = False
running = True
clicking = False
countyselect = ""
while running:
    for info in countieslist:
        if countyselect == info[0]:
            window.blit(counties, (0, 100))
            window.blit(pin, (info[1] - 10, info[2] - 25))
            window.blit(text_surface, (200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                countyon -= 1
                if countyon == -1:
                    countyon = 38
            elif event.key == pygame.K_RIGHT:
                countyon += 1
                if countyon == 39:
                    countyon = 0
            elif event.key == pygame.K_s:
                selected = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = False
    countyselect = countieslist[countyon][0]                    
    for marker in markerstodisplay:
        if marker[0] == "Warning":
            window.blit(warning, (marker[1], marker[2]))
        elif marker[0] == "Fire":
            window.blit(fire, (marker[1], marker[2]))
    if selected:
        draw_rounded_rectangle(window, (50, 50, 50), (300, 300, 200, 200), 10)
        font = pygame.font.Font("Roboto-Black.ttf", 15)
        asktext = font.render("Report in: " + countieslist[countyon][0], True, (255, 255, 255))
        window.blit(asktext, (320, 330))
        asktext = font.render("Report Risk", True, (255, 255, 255))
        draw_rounded_rectangle(window, (0, 50, 50), (300, 372, 200, 15), 10)        
        if over_rect((300, 372, 200, 15), 10):
            draw_rounded_rectangle(window, (0, 0, 0), (300, 372, 200, 15), 10)
            if clicking:
                selected = False
                markerstodisplay.append(["Warning", countieslist[countyon][1], countieslist[countyon][2]])
        window.blit(warning, (320, 370))
        window.blit(asktext, (360, 370))
        draw_rounded_rectangle(window, (0, 50, 50), (300, 405, 200, 15), 10)
        if over_rect((300, 405, 200, 15), 10):
            draw_rounded_rectangle(window, (0, 0, 0), (300, 405, 200, 15), 10)
            if clicking:
                selected = False
                markerstodisplay.append(["Fire", countieslist[countyon][1], countieslist[countyon][2]])
        asktext = font.render("Report Fire", True, (255, 255, 255))
        window.blit(asktext, (360, 405))
        window.blit(fire, (320, 401))
        draw_rounded_rectangle(window, (0, 50, 50), (300, 438, 200, 15), 10)
        if over_rect((300, 438, 200, 15), 10):
            draw_rounded_rectangle(window, (0, 0, 0), (300, 438, 200, 15), 10)
            if clicking:
                selected = False
        asktext = font.render("Cancel", True, (255, 255, 255))
        window.blit(asktext, (320, 436))

        font = pygame.font.Font("Roboto-Black.ttf", 30)
    pygame.display.flip()
    text_surface = font.render(countieslist[countyon][0], True, (0, 0, 0))


