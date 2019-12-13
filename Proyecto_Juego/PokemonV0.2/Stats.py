class Stats:

    def __init__(self, HP, Attack, Defense, SpAttack, SpDefense, Speed):

        self.IVs = 3
        self.EVs = 1
        #BASE
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefense = SpDefense
        self.Speed = Speed
        #Current
        self.Current_Attack = Attack
        self.Current_Defense = Defense
        self.Current_SpAttack = SpAttack
        self.Current_SpDefense = SpDefense
        self.Current_Speed = Speed

    def Reset(self, flag):
        if flag:
            self.Current_Attack = self.Attack
            self.Current_Defense = self.Defense
            self.Current_SpAttack = self.SpAttack
            self.Current_SpDefense = self.SpDefense
            self.Current_Speed = self.Speed