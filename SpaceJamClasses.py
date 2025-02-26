from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
global base

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Universe(ShowBase):
   def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Spaceship(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.SetKeyBindings()

    def SetKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])
        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])
        self.accept('arrow_up', self.UpTurn, [1])
        self.accept('arrow_up-up', self.UpTurn, [0])
        self.accept('arrow_down', self.DownTurn, [1])
        self.accept('arrow_down-up', self.DownTurn, [0])
        self.accept('e', self.RightRotate, [1])
        self.accept('e-up', self.RightRotate, [0])
        self.accept('q', self.LeftRotate, [1])
        self.accept('q-up', self.LeftRotate, [0])
    def Thrust(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyThrust, 'forward-thrust')
        else:
            base.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        trajectory = base.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    def LeftTurn(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyLeftTurn, 'left-turn')

        else:
            base.taskMgr.remove('left-turn')

    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def RightTurn(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyRightTurn, 'right-turn')

        else:
            base.taskMgr.remove('right-turn')

    def ApplyRightTurn(self, task):
        rate = -.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def UpTurn(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyUpTurn, 'up-turn')

        else:
            base.taskMgr.remove('up-turn')

    def ApplyUpTurn(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont

    def DownTurn(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyDownTurn, 'down-turn')

        else:
            base.taskMgr.remove('down-turn')

    def ApplyDownTurn(self, task):
        rate = -.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont
    
    def RightRotate(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyRightRotate, 'right-rotate')

        else:
            base.taskMgr.remove('right-rotate')

    def ApplyRightRotate(self, task):
        rate = .5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont

    def LeftRotate(self, keyDown):
        if keyDown:
            base.taskMgr.add(self.ApplyLeftRotate, 'left-rotate')

        else:
            base.taskMgr.remove('left-rotate')

    def ApplyLeftRotate(self, task):
        rate = -.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)