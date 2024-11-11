import pygame#路径：pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple
import random
import time

# Initialize pygame and set up window
title='Star Wars'
SCREEN_WIDTH=900
SCREEN_HEIGHT=800
bg = (55,85,155)#调色三原色
pygame.init()#初始化
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#建立窗口
pygame.display.set_caption(title)#建立标题


screen.fill(bg)
# 初始化pygame和设置窗口

class GameSprite(pygame.sprite.Sprite):
    """Base Game Sprite Class 游戏基础精灵类"""
    # Initialize sprite, load image, set position and speed
    # 初始化精灵，加载图片，设置位置和速度
    # Update method controls vertical movement
    # update方法控制垂直移动

class Hero(GameSprite):
    """Player Aircraft Class 玩家飞机类"""

    def __init__(self):
        # Call parent class constructor
        super().__init__("hero.png", speed=0)
        # Set initial position
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 60
        # Create bullet group
        self.bullets = pygame.sprite.Group()

    def fire(self):
        # Create a bullet instance
        bullet = Bullet("bullet.png", -2)
        # Set bullet position
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        # Add bullet to bullet group
        self.bullets.add(bullet)

class Bullet(GameSprite):
    """Bullet Class 子弹类"""
    # Initialize bullet, set speed
    # 初始化子弹，设置速度
    # Update method controls bullet movement and destruction
    # update方法控制子弹移动和销毁

class Enemy(GameSprite):
    """Enemy Aircraft Class 敌机类"""
    # Initialize enemy, random position and speed
    # 初始化敌机，随机位置和速度
    # Update method controls enemy movement and destruction
    # update方法控制敌机移动和销毁

class Game:
    """Main Game Class 游戏主类"""

    def __init__(self):
        # Initialize game window and clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        # Create player and enemy groups
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()
        # Set timer events for enemy creation and firing
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(FIRE_EVENT, 500)

    def create_enemy(self):
        """Create Enemy Method 创建敌机方法"""
        # Create enemy and add to sprite group
        enemy = Enemy()
        self.enemy_group.add(enemy)

    def run(self):
        """Game Main Loop 游戏主循环"""
        while True:
            # 1. Set frame rate 设置帧率
            self.clock.tick(FRAME_RATE)
            # 2. Event listening (quit and fire) 事件监听（退出和开火）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == ENEMY_EVENT:
                    self.create_enemy()
                elif event.type == FIRE_EVENT:
                    self.hero.fire()
            # 3. Player movement control 玩家移动控制
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                self.hero.rect.x -= self.hero.speed
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.rect.x += self.hero.speed
            # 4. Create enemies 创建敌机
            # Enemies are created via timer events
            # 5. Update sprite groups 更新精灵组
            self.hero_group.update()
            self.hero.bullets.update()
            self.enemy_group.update()
            # 6. Collision detection 碰撞检测
            pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
            if pygame.sprite.spritecollideany(self.hero, self.enemy_group):
                pygame.quit()
                exit()
            # 7. Draw screen 绘制画面
            self.screen.fill(BACKGROUND_COLOR)
            self.hero_group.draw(self.screen)
            self.hero.bullets.draw(self.screen)
            self.enemy_group.draw(self.screen)
            # 8. Update display 更新显示
            pygame.display.update()

# Game Start 游戏启动
if __name__ == "__main__":
    game = Game()
    game.run()