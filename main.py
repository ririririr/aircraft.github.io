import pygame#路径：pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple
import random
import time
import os

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

# Define constants
ENEMY_EVENT = pygame.USEREVENT + 1
FIRE_EVENT = pygame.USEREVENT + 2
FRAME_RATE = 60
BACKGROUND_COLOR = bg

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GameSprite(pygame.sprite.Sprite):
    """Base Game Sprite Class 游戏基础精灵类"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        # Load image with full path
        full_path = os.path.join(BASE_DIR, image_name)
        self.image = pygame.image.load(full_path)
        self.rect = self.image.get_rect()
        # Set speed
        self.speed = speed

    def update(self):
        # Move sprite vertically
        self.rect.y += self.speed

class Hero(GameSprite):
    """Player Aircraft Class 玩家飞机类"""

    def __init__(self):
        super().__init__("hero.png", speed=5)
        # Set initial position
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 60
        # Create bullet group
        self.bullets = pygame.sprite.Group()

    def update(self):
        # Movement handled in Game class
        pass

    def fire(self):
        # Create a bullet instance
        bullet = Bullet("bullet.png", -10)
        # Set bullet position
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        # Add bullet to bullet group
        self.bullets.add(bullet)

class Bullet(GameSprite):
    """Bullet Class 子弹类"""

    def __init__(self, image_name, speed):
        super().__init__(image_name, speed)

    def update(self):
        # Move bullet upwards
        self.rect.y += self.speed
        # Destroy bullet if it moves out of screen
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameSprite):
    """Enemy Aircraft Class 敌机类"""

    def __init__(self):
        super().__init__("enemy.png")
        # Random horizontal position
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        # Start above the screen
        self.rect.y = -self.rect.height
        # Random speed
        self.speed = random.randint(1, 3)

    def update(self):
        # Move enemy downwards
        self.rect.y += self.speed
        # Destroy enemy if it moves out of screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

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