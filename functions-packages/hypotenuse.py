import math   
def get_hypotenuse(catet1, catet2):  
    # calculate hypotenuse of right triangle based on 2 catets and return it
    hypotenuse = math.sqrt(math.pow(catet1,2) + math.pow(catet2,2))
    return hypotenuse
