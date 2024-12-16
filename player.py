import random

class Player:
    def __init__(self, camember_number, run, answer, position, winner):
        self.camember_number = camember_number
        self.run = run
        self.answer = answer
        self.position = position
        self.winner = winner

    
    def win_a_camembert(self, camembert_number):
        self.camember_number + 1


    def dice(self):
        return random.randint(1, 6)    


    def nouvelle_position(self, position, direction ):
        if direction == "avant":
            self.position += dice_value
        elif direction == "arriere":
            self.position -= dice_value
        self.position %= 42       
        
        

    
        

