import random
class BirthdayParadox:
    def __init__(self, group_size,simulations=100):
     """
        Initializing simulation with:
        - group_size: number of people in the group
        - simulations: Repetitions of the experiment
        """
     self.group_size = group_size
     self.simulations = simulations
     '''
     Generate Random birthdays for the group.
     Each  birthday represents as integer(1....365)
     
     '''
     
    def make_birthdays(self):
        birthdays=[]   #birthdays will be store here
        for i in range(self.group_size):
            day=random.randint(1,365)
            birthdays.append(day)
        return birthdays
        
    def detect_duplicates(self,birthdays):
        '''
        Check the given list of birthday contain duplicates
        if atleast two people share the same birthday, then return true otherwise return false
        
        '''
        size=len(birthdays)
        for i in range (size): #[200,100,40,50,200] it will take "200" the  first value
         for j in range (i+1 ,size):#it will take the second value cuz it has to check that if there's any duplicate or not
           if birthdays[i]==birthdays[j]:#200==100,200==40,200==50,200==200
               
               return True        # found duplicate
        return False              # no duplicates
    def run(self):
         '''
        Run the simulation multiple times (self.simulations).
        Each run generates birthdays for the group and checks 
        for duplicates. 
        Returns the probability (as a fraction) that at least 
        two people share a birthday.
        
        '''
       
         occurences=0 #calculate how much time duplicates occoured
         for i in range( self.simulations):
           birthdays = self.make_birthdays()
           if self.detect_duplicates(birthdays):
            occurences +=1 # increment if duplicates found
         probability = occurences/self.simulations
         return probability
        
    def show_probability(self):
        probability =self.run()
        print(f"For {self.group_size} people → Probability ≈ {probability:.2f}")
    
