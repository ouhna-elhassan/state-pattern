
class Context:
    def __init__(self,state):
        self.state = state
    
    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state = state

    def push(self):
        self.state.handlePush(self)

    def pull(self):
        self.state.handlePull(self)