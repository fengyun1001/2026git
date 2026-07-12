import pygame
import math

# 初始化pygame
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 820, 820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("眼球跟踪训练V1.0")

# 颜色定义
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 旋转参数
center_x, center_y = WIDTH // 2, HEIGHT // 2  # 旋转中心点
radius_rotate = 300       # 旋转轨道半径
circle_r = 20             # 红色圆圈自身大小
angle = 0                 # 初始角度
speed = 0.02              # 旋转速度
clockwise = True          # True顺时针 False逆时针
running = True
clock = pygame.time.Clock()

while running:
    # 帧率控制
    clock.tick(60)
    
    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按键切换方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                clockwise = True
                speed = 0.02
            if event.key == pygame.K_LEFT:
                clockwise = False
                speed = 0.02
            if event.key == pygame.K_SPACE:
                speed = 0  # 正负切换实现暂停反转
            
    
    # 角度更新：控制顺/逆时针
    if clockwise:
        angle += speed
    else:
        angle -= speed
    
    # 计算红色圆圈坐标（三角函数圆周运动）
    circle_x = center_x + radius_rotate * math.cos(angle)
    circle_y = center_y + radius_rotate * math.sin(angle)
    
    # 绘制背景
    screen.fill(BLACK)
    # 绘制旋转轨道（白色虚线圆环，辅助观察）
    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius_rotate, 3)
    # 绘制中心原点
    pygame.draw.circle(screen, WHITE, (center_x, center_y), 5)
    # 绘制红色圆圈
    pygame.draw.circle(screen, RED, (int(circle_x), int(circle_y)), circle_r)
    
    # 文字提示
    font = pygame.font.Font("/windows/fonts/simhei.ttf", 20)
    dir_text = "顺时针" if clockwise else "逆时针"
    text = font.render(f"当前方向：{dir_text} | ←逆时针 →顺时针 空格暂停", True, WHITE)
    screen.blit(text, (10, 10))
    
    # 刷新画面
    pygame.display.flip()

# 退出程序
pygame.quit()
