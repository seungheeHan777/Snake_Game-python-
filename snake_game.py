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

# 뱀의 초기 좌표값
first=[200,20]
# 함수 생성

# 스네이크 생성 함수

def snake():
    pygame.draw.rect(screen, BLACK,[first[0],first[1],20,20],0)
    pygame.draw.rect(screen, BLACK,[first[0]-20,first[1],20,20],0)
    pygame.draw.rect(screen, BLACK,[first[0]-40,first[1],20,20],0)
    pygame.draw.rect(screen, BLACK,[first[0]-60,first[1],20,20],0)

#블럭을 움직이는 함

def move_block():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:       
            first[1] -= 20         # 블록의 y 좌표를 1 뺀다
        elif event.key == pygame.K_DOWN:   
            first[1] += 20         # 블록의 y 좌표를 1 더한다
        elif event.key == pygame.K_LEFT:   
            first[0] -= 20         # 블록의 x 좌표를 1 뺀다
        elif event.key == pygame.K_RIGHT:  
            first[0] += 20         # 블록의 x 좌표를 1 더한다
    
# 게임하는 동안 작동하는 함수
def rungame():
    global running,event
    while running:
        fps.tick(10) #초당 10프레임?로 재
        screen.fill(WHITE)
        snake()
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문 -> 중간에 발생한 이벤트를 캐치하고 검사
            move_block()    #블럭을 움직이는 함수
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False
            
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()   #update 와 비슷하지만 flip은 전체 surface를 업데이트, update는 특정 부분 가능


rungame()
pygame.quit()
