import pygame

pygame.init() #pygame 모듈 초기화
size   = [400, 300]
screen = pygame.display.set_mode(size) #display 사이즈 지정
pygame.display.set_caption("snake game")

#이벤트 루프 pygame 유지

running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중

#배경 이미지 불러오기

background = pygame.image.load("C:\\Users\\ASUS\\Desktop\\snake_game\\black&yellow.jpg")

screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정

pygame.display.update() #업데이트

while running:
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False

pygame.quit()
