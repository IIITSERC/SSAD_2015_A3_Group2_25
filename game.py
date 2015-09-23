import pygame
red=(255,0,0)
w=(255,255,255)
ww=(30,90,0)
b=(0,0,0)
class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
    
        self.image=pygame.Surface([width, height])
        self.image.fill(red)
		
        self.rect=self.image.get_rect()
	W=(0,0,0)
        self.rect.y=y
	bb=(67,87,98)
        self.rect.x=x 
class Ladder(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
	pygame.sprite.Sprite.__init__(self)
	self.image=pygame.Surface([width,height])
	self.image.fill(ww)
	self.rect=self.rect=self.image.get_rect()
	self.rect.y=y
	self.rect.x=x
	
class Kong(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
	k=(34,33,54)
        self.image=pygame.Surface([15,15])
        self.image.fill(b)
 	self.rest=False
        self.rect=self.image.get_rect()
	self.change_y=0
        self.change_x=0
        self.walls=None
	self.rect.y=y
        self.rect.x=x	
 	self.dy=0
    def update(self,dt):
        self.rect.x+=self.change_x
 
        hitblock=pygame.sprite.spritecollide(self,self.walls,False)
        for block in hitblock:
            if self.change_x<0:
                self.rect.left=block.rect.right
            else:
                self.rect.left=block.rect.right
 	
        self.rect.y+=self.change_y
 
        hitblock=pygame.sprite.spritecollide(self,self.walls,False)
        for block in hitblock:
 
            if self.change_y<0:
                self.rect.top=block.rect.bottom
		self.dy=0
		self.rest=True
            else:
                self.rect.bottom=block.rect.top
		self.dy=0
		self.est=True
 	self.dy=min(400,self.dy+40)
	self.rect.y+=(self.dy)*dt

    def velocity(self,x,y):
    	self.change_y+=y
        self.change_x+=x

 
def main(): 
	pygame.init()
 
	screen=pygame.display.set_mode((1000,700)) 
	all_sprite_list=pygame.sprite.Group()
 
	brick_list=pygame.sprite.Group()
 
	brick = Brick(0, 0, 10, 700)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	brick = Brick(10,0,990,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
 
	brick = Brick(990 , 10 , 10, 700)
	all_sprite_list.add(brick)
	brick_list.add(brick)

	brick= Brick(0,690,990,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)

	brick=Brick(0,570,700,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	brick=Brick(200,450,990,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	
	brick=Brick(0,330,650,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	
	brick=Brick(300,220,990,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	brick=Brick(0,110,400,10)
	all_sprite_list.add(brick)
	brick_list.add(brick)
	 
	kong=Kong(50,50)
	kong.walls=brick_list
	 
	all_sprite_list.add(kong)
	 
	clock=pygame.time.Clock()
 
	done=True
	speed=[1,1]
	while done:
		dt=pygame.time.Clock().tick(60)*(1.0/1000)
		for event in pygame.event.get():
	        	if event.type==pygame.QUIT:
        	    		done=False
		key=pygame.key.get_pressed()
      	#  elif event.type == pygame.KEYDOWN:
		if key[pygame.K_LEFT]:
           # if event.key == pygame.K_LEFT:
			kong.rect.x-=300*dt
               # kong.velocity(-3, 0)
       # elif event.key == pygame.K_RIGHT:
		if key[pygame.K_RIGHT]:
			kong.rect.x+=300*dt
        #elif event.key == pygame.K_SPACE:
		if key[pygame.K_SPACE]:
			kong.dy=-500
	#kong.dy=min(400,kong.dy - 40)
	#kong.rect.y+=kong.dy * dt
# dt=pygame.time.Clock().tick(60)
	    
        #    elif event.key == pygame.K_UP:
         #       kong.velocity(0, -3)
          #  elif event.key == pygame.K_DOWN:
          #    kong.velocity(0, 3)
    
   #     elif event.type == pygame.KEYUP:
    #        if event.key == pygame.K_LEFT:
#		kong.rect.x -= 300*dt
              #  kong.velocity(3, 0)
 #           elif event.key == pygame.K_RIGHT:
#		kong.rect.x += 300*dt
#	    elif event.key == pygame.K_SPACE:
#		kong.dy=-500
 #               kong.velocity(-3, 0)
           # elif event.key == pygame.K_UP:
    #            kong.velocity(0, 3)
     #       elif event.key == pygame.K_DOWN:
      #          kong.velocity(0, -3)

    #clock.tick(60)
		all_sprite_list.update(dt*(1.0/1000))
 
		screen.fill(w)
 
		all_sprite_list.draw(screen)
 
		pygame.display.flip()
 
 
	pygame.quit()
if __name__ == "__main__":
	main()
