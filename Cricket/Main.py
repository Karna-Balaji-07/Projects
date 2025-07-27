
import csv
import os
import random

# ************************************************BATTING************************************************************* #
class Batsman:
    def __init__(self,name,jno):
        self.name = name
        self.highest = 0
        self.hundreds = 0
        self.fifty = 0
        self.total = 0
        self.average = 0
        self.innings = 0
        self.balls = 0
        self.innings = 0
        self.Batplayer = []
        
    def bats(self,score,out = True):
        self.total += score
        self.balls +=1
        if out:
            self.innings +=1
            self.average = round(self.total/self.innings,2)
            
        self.highest = max(score, self.highest)
        if score >= 100:
            self.hundreds +=1
        elif score >= 50 and score < 100:
            self.fifty += 1
            
    def details(self):
        self.Batpalyer.append([self.name,self.total, self.average, self.highest, self.hundreds,self.fifty])
    
    def Batting(self):
        filename = 'batting.csv'
        file_exists = os.path.exists(filename)
        with open(filename,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Batsman','Total Runs','Average','Highest','Hundreds','Fifty'])
            
            for i in self.Batplayer:
                writer.writerow(i)
    
# ************************************************BOWLING************************************************************* #    

class Bowler:
    def __init__(self,name):
        self.name = name
        self.wickets = 0
        self.maiden = 0
        self.overs = 0
        self.runs = 0
        self.economy = 0.0
        self.fiveWickerhaul = 0
        self.best = 0
        self.Bowlplayer = []
        
    def details(self):
        self.Bowlplayer.append([self.name,self.wickets, self.maiden, self.runs, self.economy, self.fiveWickethaul, self.best])
        
    def bowls(self, wickets,runs_in_over):
        self.wickets += wickets
        self.overs +=1
        self.runs += runs_in_over
        if runs_in_over == 0:
            self.maiden +=1
        
        if wickets >= 5:
            self.fiveWickerhaul +=1
        
        self.best = max(self.best, wickets)
        
        if self.overs > 0:
            self.economy = round(self.runs/self.overs,2)
    
    def Bowling(self):
        filename = 'Bowling.csv'
        file_exists = os.path.exists(filename)
        with open(filename,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name','Wickets','Maiden','Runs','Economy','5-Wicket haul','Best Figures'])
            for bowl in self.Bowlplayer:
                writer.writerow(bowl)
                
# ************************************************Current Match************************************************************* #
class Current_Match:
    
    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.total_runs = 0
        self.striker = None
        self.NonStriker = None
        self.bowler = None
        self.nextBowler = []
        self.nextstriker = []
        self.teamA = []
        self.teamB = []
        self.balls = 0
        self.ballFaced =0 
        self.overs = 0
        self.maiden = 0

    def toss(self,flip):
        tossString = ['Head','Tail']
        user_input = input().lower()
        index = random.randint(0,1)
        if user_input == tossString[index]:
            print('Choose Batting or Bowling')
            choice = int(input())
            if choice == 1:
                #Batting
                pass
            else:
                #Bowling
                pass
            
    def teamA(self):
        for i in range(12):
            name = input().lower()
            jno = int(input())
            self.teamA.append([jno, name])
        
    def teamB(self):
        for i in range(12):
            jno = int(input())
            name = input().lower()
            self.teamB.append([jno,name])
        
    def MatchBatting(self,name,runs,balls,strikerate):
        filename = 'MatchBatting.csv'
        file_exists = os.path.exists(filename)
        with open(filename,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name','Runs','Balls','Strike Rate'])
            writer.writerow([name,runs,balls,strikerate])
            

#********************************************************************************************************#
    def batting(self):
        jno1 = int(input("Enter jersey number for striker: "))
        jno2 = int(input("Enter jersey number for non-striker: "))

        self.striker = next((player for player in self.teamA if player.jno == jno1), None)
        self.NonStriker = next((player for player in self.teamA if player.jno == jno2), None)
                
        self.nextstriker = [p for p in self.teamA if p.jno not in [jno1, jno2]]
        
        while self.wickets < 10:
            runs = int(input())
            self.runs += runs
            self.striker.ballFaced += 1
            self.balls +=1
            self.total_runs += runs
            
            gotOut = self.got_OUT(runs)
            if gotOut:
                self.wickets +=1
                self.striker.bats(0, out=True)
                if self.nextstriker:
                    name = int(input("Enter Jersey Number"))
                    self.striker = next((player for player in self.teamA if player.jno == jno1), None)
                else:
                    print("All OUT")
                    break
            
            else:
                self.striker.bats(runs,out=False)
                if runs % 2 != 0:
                    self.striker,self.NonStriker = self.NonStriker, self.striker
                    
            if self.balls % 6 == 0:
                self.overs +=1
                self.striker,self.NonStriker = self.NonStriker, self.striker
                
            for player in self.teamA:
                if player.ballFaced > 0:
                    try:
                        strike_rate = round((player.runs / player.ballFaced) * 100, 2)
                    except ZeroDivisionError:
                        strike_rate = 0.0
                    self.MatchBatting(player.name, player.runs, player.ballFaced, strike_rate)
            
            if self.overs == self.total_overs:  # Assuming you define total overs somewhere
                print("Overs complete.")
                break
    
#************************************************************************************************************#

def bowling(self):
    jno1 = int(input("Enter jersey number for Bowler: "))
    self.bowler = next((player for player in self.teamB if player.jno == jno1), None)
    self.nextBowler = [p for p in self.teamB if p.jno not in [jno1]]