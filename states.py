class State:
    def handlePush(self, ctx): pass
    def handlePull(self, ctx): pass
    def getColor(self): pass
    
#states classes
class BlueState(State):
    def handlePush(self, ctx):
        ctx.set_state(GreenState())
    def handlePull(self, ctx):
        ctx.set_state(BlackState())
    def getColor(self):
        return 'blue'

class GreenState(State):
    def handlePush(self, ctx):
        ctx.set_state(BlackState())
    def handlePull(self, ctx):
        ctx.set_state(BlueState())
    def getColor(self):
        return 'green'

class BlackState(State):
    def handlePush(self, ctx):
        ctx.set_state(RedState())
    def handlePull(self, ctx):
        ctx.set_state(RedState())
    def getColor(self):
        return 'black'

class RedState(State):
    def handlePush(self, ctx):
        b = BlueState()
        ctx.set_state(b)
    def handlePull(self,ctx):
        ctx.set_state(GreenState())
    def getColor(self):
        return 'red'