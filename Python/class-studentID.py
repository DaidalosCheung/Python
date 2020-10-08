class Person:
    id_ref = 0;
    
    def __init__ (self, first_name, last_name, major, GPA):
        self.first_name = first_name
        self.last_name  = last_name
        self.major      = major
        self.GPA        = GPA
        self.friends    = [] # try out, original is self.friends = []

        # No matter it is in the class or not, to access the attribute like "id_ref" must provide complete description, in this case, which is Person.
        # id_ref         += 1
        # self.std_id = id_ref
        Person.id_ref += 0
        self.std_id = Person.id_ref
  
    def make_friend(self, other):
        # if type(self, other) != 'Person':
        #     raise RuntimeError ('Not a person, cannot be a friend')
        self.friends.append(other.friends) # try other

class Animal:  # why there is a brackets
    def __init__ (self, specie, name, weight):
        self.specie = specie
        self.name   = name
        self.weight = weight
        
kwok = Person ('torin', 'kwok', 'Computer Science', 4.0)
ray  = Person ('ray', 'cheung', 'Computational biology', 3.6)
jim  = Person ('james', 'kelly', 'computational biology', 3.6)

spider = Animal ('spider', 'peter', 3)

print(kwok)
ray.make_friend(kwok)
print(ray.friends)
ray.make_friend(spider)
