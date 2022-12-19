import pygame

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
first=[200,20]
second=[first[0]-20,first[1]]
snake_position=[first,[first[0]-20,first[1]],[first[0]-40,first[1]],[first[0]-60,first[1]]]
# 함수 생성

# 먹이 생성 함수
def apple():
    pygame.draw.rect(screen, RED,[120,120,20,20],0)
# 스네이크 생성 함수

def snake(position):
    pygame.draw.rect(screen, BLACK,[position[0],position[1],20,20],0)


# 뱀의 이동할 때 앞에 있는 뱀의 위치를 저장하는 함수
# 뱀의 첫번째 부분이 한 칸 이동하면 뱀의 두번째 부분이 첫번째 부분이 있던 위치로 바로 이동한다.
# 배열의 역순으로 반복문을 실행해서 위치좌표를 한 칸씩 밀어낸다?
def follow_head(position):
    for i in range(len(position),1,-1):
        position[i-1][0]=position[i-2][0]
        position[i-1][1]=position[i-2][1]

#블럭을 움직이는 함수

def move_block():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            # snake_position[1][0]=snake_position[0][0]
            # snake_position[1][1]=snake_position[0][1]
            follow_head(snake_position)
            snake_position[0][1] -= 20         # 블록의 y 좌표를 20 뺀다
        elif event.key == pygame.K_DOWN:
            follow_head(snake_position)
            snake_position[0][1] += 20         # 블록의 y 좌표를 20 더한다
        elif event.key == pygame.K_LEFT:
            follow_head(snake_position)
            snake_position[0][0] -= 20         # 블록의 x 좌표를 20 뺀다
        elif event.key == pygame.K_RIGHT:
            follow_head(snake_position)
            snake_position[0][0] += 20         # 블록의 x 좌표를 20 더한다

    
# 게임하는 동안 작동하는 함수
def rungame():
    global running,event
    while running:
        fps.tick(10) #초당 10프레임?로 재
        screen.fill(WHITE)
        for i in range(len(snake_position)):
            snake(snake_position[i])
        apple()
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문 -> 중간에 발생한 이벤트를 캐치하고 검사
            move_block()    #블럭을 움직이는 함수
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False
            
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()   #update 와 비슷하지만 flip은 전체 surface를 업데이트, update는 특정 부분 가능

rungame()
pygame.quit()
