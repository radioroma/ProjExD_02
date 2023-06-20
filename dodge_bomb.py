#演習1途中
import random
import sys
import pygame as pg
#import math

WIDTH, HEIGHT = 1600, 900

def check_bound(rect: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right: 
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  
        tate = False
    return yoko, tate

delta = {
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,+5), 
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(5,0),
    }
def asdf():
    kk_img0 =pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"),0, 2.0)
    kk_img = pg.transform.flip(kk_img0, True, False)
    return {
        (0,0):kk_img,#キーを押してない時
        (+5, 0):kk_img,  # 右
        (+5, -5):pg.transform.rotozoom(kk_img, 45, 1.0),  # 右上
        (0, -5):pg.transform.rotozoom(kk_img, 90, 1.0), # 上            
        (-5, -5):pg.transform.rotozoom(kk_img, -45, 1.0),# 左上
        (-5, 0):kk_img,
        (-5, +5):pg.transform.rotozoom(kk_img, -45, 1.0),              
        (0, +5):pg.transform.rotozoom(kk_img, -90, 1.0),  
        (+5, +5):pg.transform.rotozoom(kk_img, 45, 1.0),
        }
   
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    kk_imgs=asdf()
    kk_rct=kk_imgs[(0,0)].get_rect()
    kk_rct.center=900,400
    bd_img= pg.Surface((20,20))
    pg.draw.circle(bd_img,(255,0,0), (10,10 ), 10)
    bd_img.set_colorkey((0, 0, 0))
    x =random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    bd_rct= bd_img.get_rect()
    #爆弾surface
    bd_rct.center = x,y 
    vx,vy = +5,+5
   
    
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):  
            print("ゲームオーバー")
            return 
        
        key_lst = pg.key.get_pressed()
        # kk_img =asdf[(sum_mv)]
        sum_mv = [0, 0] 
        sum_kk_mv=[0,0] 
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
                sum_kk_mv[0] +=mv[0]
                sum_kk_mv[1] +=mv[1]
        #screen.blit(kk_img,kk_rct)
                kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) !=(True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        
            
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_imgs[tuple(sum_mv)], kk_rct)
        bd_rct.move_ip(vx, vy)
        yoko,tate = check_bound(bd_rct)
        if not yoko:
            vx *=-1
        if not tate:
            vy *=-1
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

    #key_lst = pg.key.get_pressed()
    
        #sum_mv=[0,0]
        #for k,mv in delta.items():
         ###     sum_mv[0]+=mv[0]
            #    sum_mv[1]+=mv[1]
        #kk_rct.moveip(sum_mv[0],sum_mv[1])
         #   #print(key_lst)