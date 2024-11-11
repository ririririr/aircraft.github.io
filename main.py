import pygame
import random

# 初始化pygame和设置窗口
pygame.init()
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("飞机大战")

# 基础精灵类
class GameSprite(pygame.sprite.Sprite):
    """游戏基础精灵类"""
    def __init__(self, image_name, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self):
        self.rect.y += self.speed

# 创建玩家飞机类
class Hero(GameSprite):
    """玩家飞机类"""
    def __init__(self):
        super().__init__("images/hero.png", 0, SCREEN_HEIGHT - 126)
        self.bullets = pygame.sprite.Group()
        self.speed = 5

    def fire(self):
        bullet = Bullet()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        self.bullets.add(bullet)

# 创建子弹类
class Bullet(GameSprite):
    """子弹类"""
    def __init__(self):
        super().__init__("images/bullet.png", 0, 0)
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# 创建敌机类
class Enemy(GameSprite):
    """敌机类"""
    def __init__(self):
        y = -random.randint(0, 100)
        x = random.randint(0, SCREEN_WIDTH - 57)
        super().__init__("images/enemy.png", x, y)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# 创建游戏主类
class Game:
    """游戏主类"""
    def __init__(self):
        self.hero = Hero()
        self.enemies = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
    def create_enemy(self):
        """创建敌机方法"""
        enemy = Enemy()
        self.enemies.add(enemy)

    def run(self):
        """游戏主循环"""
        running = True
        while running:
            # 设置刷新帧率
            self.clock.tick(60)
            
            # 事件监听
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.hero.fire()

            # 获取按键
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.hero.rect.x -= self.hero.speed
            if keys[pygame.K_RIGHT]:
                self.hero.rect.x += self.hero.speed

            # 限制英雄的活动范围
            if self.hero.rect.left < 0:
                self.hero.rect.left = 0
            if self.hero.rect.right > SCREEN_WIDTH:
                self.hero.rect.right = SCREEN_WIDTH

            # 随机生成敌机
            if random.random() < 0.02:
                self.create_enemy()

            # 更新精灵组
            self.hero.bullets.update()
            self.enemies.update()

            # 碰撞检测
            pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)

            # 绘制画面
            screen.fill((255, 255, 255))  # 白色背景
            self.hero.bullets.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.hero.image, self.hero.rect)
            
            # 更新显示
            pygame.display.flip()

        # 游戏退出
        pygame.quit()

# 游戏启动
if __name__ == "__main__":
    game = Game()
    game.run()