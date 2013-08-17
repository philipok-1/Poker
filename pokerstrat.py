#poker player strategy and i/o

import random, pokerhands



class Strategy():
        
        def __init__(self, player):
                
                self.tight=0
                self.aggression=0
                self.cool=0
                self.player=player
                self.name=str(self.__class__.__name__)
                
        @property
        
        def play_style(self):
                
                pass

        def decide_play(self, player, pot):
                
                pass

class Random(Strategy):

        
       
        
        def decide_play(self, player, pot):

                stake=0
                if player.all_in or player.stack<=0:

                        player.stake=-2

                else:

                        choice=random.randint(0,50)

                        if choice>12 or player.raised==1:
                                stake=player.to_play
                                if player.stack<player.to_play:
                                        fold_choice=random.randint(0,5)
                                        if fold_choice<3:
                                                stake=-1
                                        else:
                                                stake=player.stack
                
                        elif choice==0:
                                stake=-1

                        else:

                                if choice==1:
                                        stake=player.stack
                                        player.raised+=1
                                else:
                                        stake=player.to_play+random.randrange(10,100,20)
                                        if stake>player.stack:
                                                stake=player.stack
                                        player.raised+=1

                        

                return
		
class Human(Strategy):
    
    options=[['x', 'f', 'b'], ['c', 'r', 'f'], ['c', 'f']]
    choices={0:'check, fold or bet', 1:'call, raise, fold', 2:'call all-in or fold'}
    
    def decide_play(self, player, pot):
        
        options=Human.options
        choices=Human.choices
        action=''
        op=0


        if player.to_play==0:
                op=0
        elif player.to_play<=player.stack:
                op=1
        else: op=2

        if player.all_in or player.stack<=0:
                player.stake=0

        else:

                while action not in options[op]:

                        try:
                                action=input(str(choices[op]))
                        except NameError:
                         print ('enter a valid choice')

    
        if action=='x':
                player.check_call(pot)
        elif action=='f':
                player.fold(pot)
        elif action=='c':
                player.check_call(pot)
        elif action=='b' or action=='r':
                stake=0
                while stake not in range (1,(player.stack+1)):
                        try:
                                stake=int(input('stake..'))
                        except:
                                print ('input a stake')
                                
                player.bet(pot, stake)

        
                                
					
			
			
				
			
		
			
			
			
			
		
	
	
	
