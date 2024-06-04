import pygame
import random

# تهيئة Pygame
pygame.init()

# إعدادات الشاشة
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("لعبة الألغاز الرياضية")

# ألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# إعدادات الخط
font = pygame.font.Font(None, 36)

# توليد سؤال رياضي بسيط
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"{num1} {operator} {num2} = ?"
    options = [answer, answer + random.randint(1, 3), answer - random.randint(1, 3)]
    random.shuffle(options)
    return question, answer, options

# رسم النص على الشاشة
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# اللعبة الرئيسية
def main():
    running = True
    question, answer, options = generate_question()
    selected = None
    result = ""

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if option1_rect.collidepoint(mouse_x, mouse_y):
                    selected = options[0]
                elif option2_rect.collidepoint(mouse_x, mouse_y):
                    selected = options[1]
                elif option3_rect.collidepoint(mouse_x, mouse_y):
                    selected = options[2]
                
                if selected is not None:
                    if selected == answer:
                        result = "صحيح!"
                        result_color = GREEN
                    else:
                        result = "خطأ!"
                        result_color = RED

        draw_text(question, font, BLACK, screen, 20, 20)
        
        option1_rect = pygame.Rect(50, 100, 200, 50)
        option2_rect = pygame.Rect(50, 200, 200, 50)
        option3_rect = pygame.Rect(50, 300, 200, 50)

        pygame.draw.rect(screen, BLACK, option1_rect, 2)
        pygame.draw.rect(screen, BLACK, option2_rect, 2)
        pygame.draw.rect(screen, BLACK, option3_rect, 2)

        draw_text(str(options[0]), font, BLACK, screen, 60, 110)
        draw_text(str(options[1]), font, BLACK, screen, 60, 210)
        draw_text(str(options[2]), font, BLACK, screen, 60, 310)

        if result:
            draw_text(result, font, result_color, screen, 20, 400)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
