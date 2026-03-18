class Character():
    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__mana = 100
        self.__damage = 5
        self.__str = 0 # Strenght stat
        self.__vit = 0 # Vitality stat
        self.__int = 0 # Intelligence stat
        self.__agi = 0 # Agility stat
    def getUsername(self):
        return self.__username
    def setUsername(self, new_username):
        self.__username = new_username
        
    ## Character Status
    def getHp(self):
        return self.__hp
    def setHp(self, new_hp):
        self.__hp = new_hp
    def getDamage(self):
        return self.__damage
    def setDamage(self, new_damage):
        self.__damage = new_damage
    
    ## Character Stats
    
    ## Strength
    def getStr(self):
        return self.__str
    def setStr(self, new_str):
        self.__str = new_str
        
    ## Vitality    
    def getVit(self):
        return self.__vit
    def setVit(self, new_vit):
        self.__vit = new_vit
        
    ## Intelligence    
    def getInt(self):
        return self.__int
    def setInt(self, new_int):
        self.__int = new_int
    
    ## Agility    
    def getAgi(self):
        return self.__agi
    def setAgi(self, new_agi):
        self.__agi = new_agi
    
    ## Character Damage and Heal taken
    def reduceHp(self, damage_amount):
        self.__hp = self.__hp - damage_amount
    def addHp(self, heal_amount):
        self.__hp = self.__hp + heal_amount
    
character1 = Character("Shinji")
## print(character1.__username) 
# this is invalid as there is no way to access the variable __username be cause the variable is private meaning it can not be directly accessed
print(character1.getUsername())

