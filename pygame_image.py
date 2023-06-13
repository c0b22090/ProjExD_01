import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img3 = pg.image.load("ex01/fig/3.png")
    tmr = 0
    bg_img3_f = pg.transform.flip(bg_img3, True, False)
    bg_img3_rz = pg.transform.rotozoom(bg_img3_f, 10, 1.0)
    lst = [bg_img3_f, bg_img3_rz]
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])

        screen.blit(lst[tmr%2], [x, 200])
        pg.display.update()
        tmr += 1    
        x+=1
        if x >= 800:
            x = 0
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()