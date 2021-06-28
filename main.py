from src import controller
import pygame

def main():
    pygame.init()
    team = {"lead": "Jiawei/Matt", "backend": "Jiawei Liu", "frontend": "Matt M"}
    print("Software Lead is: ", team["lead"])
    print("Backend is: ", team["backend"])
    print("Frontend is: ", team["frontend"])
    #Create an instance on your controller object

    main_window = controller.Controller()
    main_window.mainLoop()

main()
