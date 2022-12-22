import pygame
from datetime import datetime
from datetime import timedelta
from random import randrange
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

pygame.init() #pygame 모듈 초기화
size   = [400, 400]
screen = pygame.display.set_mode(size) #display 사이즈 지정
pygame.display.set_caption("snake game")

#이벤트 루프 pygame 유지

running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중

pygame.display.update() #업데이트

#Loop until the user clicks the close button.
fps = pygame.time.Clock() # 프레임

# 뱀의 머리 좌표값
##first=[200,20]
##snake_position=[first,[first[0]-20,first[1]],[first[0]-40,first[1]],[first[0]-60,first[1]]]
snake_position=[[200,20],[180,20],[160,20],[140,20]]

# 먹이의 좌표값
# first =[120,120]
apple_position=[120,120]
# 뱀이 자동으로 움직이게 하기위한 시간 계산
last_moved = datetime.now()
direction = ''
# 함수 생성
# 먹이 클래스 
# 먹이 생성 함수
class Apple:
    def __init__(self,position):
        pygame.draw.rect(screen, RED,[position[0],position[1],20,20],0)
        print("먹이의 좌표는",position[0],position[1])
# 랜덤으로 먹이 생성
    def random(self,position):
        position[0]=randrange(0,400,20)
        position[1]=randrange(0,400,20)
        print("새로운 먹이의 좌표는",position[0],position[1])
##        pygame.draw.rect(screen, RED,[apple_position[0],apple_position[1],20,20],0)


# 스네이크 클래스
class Snake:
    def __init__(self):
        print()
##        self.positions = [(2,0),(1, 0),(0,0)]  # 뱀의 위치, (2,0이 머리)
##        self.direction = ''
        
    # 스네이크 생성 함수

    def make_snake(self,position):
        pygame.draw.rect(screen, BLACK,[position[0],position[1],20,20],0)


    # 뱀의 이동할 때 앞에 있는 뱀의 위치를 저장하는 함수
    # 뱀의 첫번째 부분이 한 칸 이동하면 뱀의 두번째 부분이 첫번째 부분이 있던 위치로 바로 이동한다.
    # 배열의 역순으로 반복문을 실행해서 위치좌표를 한 칸씩 밀어낸다?
    def follow_head(self,position):
        for i in range(len(position),1,-1):
            position[i-1][0]=position[i-2][0]
            position[i-1][1]=position[i-2][1]

    #블럭을 움직이는 함수

    def move_block(self):
        global last_moved,direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not direction =='D':                # 최근에 이동한 방향과 반대 방향으로는 이동할 수 없다
                    self.follow_head(snake_position)
                    snake_position[0][1] -= 20         # 블록의 y 좌표를 20 뺀다
                    last_moved = datetime.now()        # 방향키를 입력한 시간을 기록
                    direction = 'U'                    # 방향 저장하는 변수에 상하좌우을 저장
            elif event.key == pygame.K_DOWN:
                if not direction =='U':                # 최근에 이동한 방향과 반대 방향으로는 이동할 수 없다
                    self.follow_head(snake_position)
                    snake_position[0][1] += 20         # 블록의 y 좌표를 20 더한다
                    last_moved = datetime.now()        # 방향키를 입력한 시간을 기록
                    direction = 'D'                    # 방향 저장하는 변수에 상하좌우을 저장
            elif event.key == pygame.K_LEFT:
                if not direction =='R':                # 최근에 이동한 방향과 반대 방향으로는 이동할 수 없다
                    self.follow_head(snake_position)
                    snake_position[0][0] -= 20         # 블록의 x 좌표를 20 뺀다
                    last_moved = datetime.now()        # 방향키를 입력한 시간을 기록
                    direction = 'L'                    # 방향 저장하는 변수에 상하좌우을 저장
            elif event.key == pygame.K_RIGHT:
                if not direction =='L':                # 최근에 이동한 방향과 반대 방향으로는 이동할 수 없다
                    self.follow_head(snake_position)
                    snake_position[0][0] += 20         # 블록의 x 좌표를 20 더한다
                    last_moved = datetime.now()        # 방향키를 입력한 시간을 기록
                    direction = 'R'                    # 방향 저장하는 변수에 상하좌우을 저장
    # 뱀이 먹이를 먹었을 때 길이가 늘어나는 것
    def add(self):
        snake_position.append([snake_position[-1][0],snake_position[-1][1]])    #append(apple_position)하면 안됨. 먹이가 뱀꼬리에 붙어다니는 꼴이 됨 왠지는 모름


# 게임하는 동안 작동하는 함수
def rungame():
    global running,event,last_moved,direction
    snake = Snake()
    apple = Apple(apple_position)
    while running:
        fps.tick(30) #초당 10프레임?로 재
        screen.fill(WHITE)
        for i in range(len(snake_position)):
            snake.make_snake(snake_position[i])
        Apple(apple_position)  # apple을 사용하면 먹이가 생성이 안됨 ??
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문 -> 중간에 발생한 이벤트를 캐치하고 검사
            snake.move_block()    #블럭을 움직이는 함수
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False

# 게임이 시작하고 뱀이 마지막으로 이동한 방향으로 쭉 이동한다.

        if timedelta(seconds=0.1) <= datetime.now() - last_moved:
            if direction == 'U':
                snake.follow_head(snake_position)
                snake_position[0][1] -= 20         # 블록의 y 좌표를 20 뺀다      
            elif direction == 'D':
                snake.follow_head(snake_position)
                snake_position[0][1] += 20         # 블록의 y 좌표를 20 더한다
            elif direction == 'L':
                snake.follow_head(snake_position)
                snake_position[0][0] -= 20         # 블록의 x 좌표를 20 뺀다
            elif  direction== 'R':
                snake.follow_head(snake_position)
                snake_position[0][0] += 20         # 블록의 x 좌표를 20 더한다
            last_moved = datetime.now()
# 뱀이 먹이를 먹은 경우 다음 먹이의 좌표가 랜덤으로 생성된다.
        if snake_position[0] == apple_position:
            snake.add()
            apple.random(apple_position)
            

# 게임 오버
# 뱀이 벽에 닿았을 때, 게임이 종료된다.
        if (snake_position[0][0]>400)or(snake_position[0][1]>400)or(snake_position[0][0]<0) or(snake_position[0][1]<0) :
            running = False # 이 부분을 나중에는 실행 종료가 되는 것이 아니라 게임 오버된 상태에서 멈췄는 것으로 바꾸는 것이 목표
# 뱀의 머리가 뱀의 몸통에 부딪히는 경우 게임 오버
        if snake_position[0] in snake_position[1:] :
            running = False
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()   #update 와 비슷하지만 flip은 전체 surface를 업데이트, update는 특정 부분 가능

rungame()
pygame.quit()
