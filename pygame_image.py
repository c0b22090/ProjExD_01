import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_f = pg.transform.flip(bg_img, True, False)
    bg_img3 = pg.image.load("ex01/fig/3.png")
    tmr = 0
    bg_img3_f = pg.transform.flip(bg_img3, True, False)
    bg_img3_rz = pg.transform.rotozoom(bg_img3_f, 10, 1.0)
    lst1 = [bg_img3_f, bg_img3_rz]
    x = 0
    kkmv = 0
    fs = 500
    num=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_f, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        if tmr%(fs//5)<=fs//10:
            kkmv = 0
        else:
            kkmv = 1
        screen.blit(lst1[kkmv], [300, 200])
        pg.display.update()
        tmr += 1    
        x = num%3200
        num+=1
        #if x >= 1600:
            #x = 0
        clock.tick(fs)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()