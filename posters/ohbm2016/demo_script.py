from .due import due, Doi

# module
due.cite(Doi("1.2.3/x.y.z"), 
         description="Solves all your problems",
         path="magicpy")

# functions
@due.dcite(Doi("1.2.3/x.y.z"), 
           description="Finds love")
def find_love():
    ...

