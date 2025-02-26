from direct.showbase.ShowBase import ShowBase
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()   

    def SetCamera(self):
        self.disableMouse()
        self.camera.reparentTo(self.Spaceship.modelNode)
        self.camera.setFluidPos(0, 1, 0)

    def SetupScene(self):
      self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', 'Assets/Universe/universe.jpg', (0, 0, 0), 10000)
      self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Earth', 'Assets/Planets/earth.jpg', (150, 5000, 67), 350)
      self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Mars', 'Assets/Planets/mars.jpg', (900, 5000, 67), 250)
      self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Jupiter', 'Assets/Planets/jupiter.jpg', (-850, 5000, 67), 500)
      self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Saturn', 'Assets/Planets/saturn.jpg', (1750, 5000, 67), 400)
      self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Venus', 'Assets/Planets/venus.jpg', (2700, 5000, 67), 350)
      self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Uranus', 'Assets/Planets/uranus.jpg', (-1800, 5000, 67), 250)
      self.Station = spaceJamClasses.SpaceStation(self.loader, "./Assets/SpaceStation/spaceStation.x", self.render, 'Universe', 'Assets/SpaceStation/SpaceStation1_Dif2.png', (150, 8000, 3000), 50)
      self.Spaceship = spaceJamClasses.Spaceship(self.loader, "./Assets/Spaceships/Dumbledore.x", self.render, 'Hero', 'Assets/Spaceships/spacejet_C.png', (150, 6000, 1500), 200)
      self.SetCamera()
      
      fullCycle = 60

      for j in range(fullCycle):
         spaceJamClasses.Drone.droneCount += 1
         nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
  
         self.DrawCloudDefense(self.Planet1, nickName)
         self.DrawBaseballSeams(self.Station, nickName, j, fullCycle, 2)
         self.DrawCircle(self.Planet2, nickName + "_X", j, fullCycle, axis='X')
         self.DrawCircle(self.Planet3, nickName + "_Y", j, fullCycle, axis='Y')
         self.DrawCircle(self.Planet4, nickName + "_Z", j, fullCycle, axis='Z')
      
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
     unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
     unitVec.normalize()
     position = unitVec * radius * 250 + centralObject.modelNode.getPos()
     spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def DrawCloudDefense(self, centralObject, droneName):
     unitVec = defensePaths.Cloud()
     unitVec.normalize()
     position = unitVec * 500 + centralObject.modelNode.getPos()
     spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawCircle(self, centralObject, droneName, step, numDrones, radius = 1, axis = 'X'):
     for i in range(numDrones):
        position = defensePaths.circleMath(i, numDrones, (radius * 500), axis) + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName + str(i), "./Assets/DroneDefender/octotoad1_auv.png", position, 5)


app = MyApp()
app.run()