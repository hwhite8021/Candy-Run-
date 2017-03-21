from gamelib import *

game = Game(800,600,"Candy Run")

bk = Image("bk.jpg",game)

bk.resizeTo(game.width, game.height)
game.setBackground(bk)

title = Image("LOGO.png",game)
bk.draw()
title.draw()
game.drawText("Press [SPACE] to play",320,400)
game.drawText("Use arrow keys to move up and down!",100,500)
game.drawText("avoid harmfull items!",100,515)
game.drawText("land on candy to get points!",100,530)
game.update(1)
game.wait(K_SPACE)

person = Animation("girl.jpg",6,game,551/6,91,3)

ball = Image("Spiked.png",game)
ball.resizeBy(-95)
ball.moveTo(500,400)
ball.setSpeed(2,90)

ycandy = Image("yellow candy.png",game)
ycandy.moveTo(500,325)
ycandy.setSpeed(2,90)
ycandy.resizeBy(-70)

monster = Image("monster.png",game)
monster.resizeBy(-85)
monster.moveTo(700,400)
monster.setSpeed(2,90)

candycane = Image("candy cane.png",game)
candycane.moveTo(700,300)
candycane.setSpeed(2,90)
candycane.resizeBy(-85)


D = Image("de.jpg",game)
D.moveTo(600,100)
D.resizeBy(-35)
D.setSpeed(2,90)

knife = Image("knife2.jpg",game)
knife.resizeBy(-60)
knife.moveTo(900,300)
knife.setSpeed(2,90)

s = Image("spike.jpg",game)
s.resizeBy(-30)
s.moveTo(300,550)

s2 = Image("spike.jpg",game)
s2.resizeBy(-30)
s2.moveTo(100,550)

s3 = Image("spike.jpg",game)
s3.resizeBy(-30)
s3.moveTo(500,550)


s4 = Image("spike.jpg",game)
s4.resizeBy(-30)
s4.moveTo(700,550)

ca = Image("candyapple.png",game)
ca.moveTo(300,200)
ca.setSpeed(2,90)
ca.resizeBy(-70)

cc = Image("candy corn.png",game)
cc.moveTo(900,100)
cc.setSpeed(2,90)
cc.resizeBy(-70)

eyes = Image("eyes.jpg",game)
eyes.moveTo(1200,100)
eyes.setSpeed(2,90)
eyes.resizeBy(-95)

win = Image("WIN.png",game)
lose = Image("LOSE.png",game) 

while not game.over:
    
    game.processInput()
         
    game.scrollBackground("left",1)

    ca.move()
    person.move()
    ball.move()
    ycandy.move()
    monster.move()
    candycane.move()
    D.move()
    knife.move()
    s.draw()
    s2.draw()
    s3.draw()
    s4.draw()
    cc.move()
    eyes.move()
    
    
    if keys.Pressed[K_UP]:
        person.y -= 3        
       
    if keys.Pressed[K_DOWN]:
        person.y -= -3

    if person.collidedWith(ycandy): 
        game.score += 1
        ycandy.moveTo(900,900)

    if ycandy.isOffScreen("left"):
        ycandy.moveTo(900,400)

    if ca.isOffScreen("left"):
        ca.moveTo(900,200)

    if cc.isOffScreen("left"):
        cc.moveTo(1000,100)

    if person.collidedWith(cc):
        game.score += 1
        cc.moveTo(900,900)

    if person.collidedWith(ca):
        game.score += 1
        ca.moveTo(900,900)

    if person.collidedWith(candycane):
        game.score += 1
        candycane.moveTo(800,800)

    if candycane.isOffScreen("left"):
        candycane.moveTo(700,300)

    if monster.isOffScreen("left"):
        monster.moveTo(900,400)
        knife.moveTo(1000,300)
        D.moveTo(600,100)

    if eyes.isOffScreen("left"):
        eyes.moveTo(1200,100)

    if person.isOffScreen("all"):
        game.over = True
        lose.draw()
        game.drawText("GAME OVER ",320,400)
        game.drawText("Press [SPACE] to Exit  ",320,200) 
        game.update(1)
        game.wait(K_SPACE)
        game.quit()
        
    if ball.isOffScreen("left"):
        ball.moveTo(900,400)
                 
    if person.collidedWith(ball):
        game.score += -10
        ball.moveTo(900,200)

    if person.collidedWith(monster):
        game.score += -10
        monster.moveTo(900,200)

    if person.collidedWith(D):
        game.score += -10
        D.moveTo(900,600) 

    if person.collidedWith(knife) :
        game.score += -10
        knife.moveTo (900,200)

    if person.collidedWith(eyes):
        game.score += -10
        eyes.moveTo(900,900)

    if  person.collidedWith(s)or person.collidedWith(s2)or person.collidedWith(s3)or person.collidedWith(s4):
        game.score += -10

    if game.score<0:
        game.over = True
        lose.draw()
        game.drawText("Press [SPACE] to Exit  ",320,200) 
        game.update(1)
        game.wait(K_SPACE)
        game.quit()

    if game.score>25:
        game.over = True
        win.draw()
        game.drawText("Press [SPACE] to Exit  ",320,200) 
        game.update(1)
        game.wait(K_SPACE)
        game.quit()

        

    game.displayScore()
    game.update(60)
    






    
        

        

    



























