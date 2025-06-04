from model.model import Model

mymodel = Model()
mymodel.buildGraph(3)
numVertici = mymodel.getNumNodes()
print(f"Numero vertici: {numVertici}")
nodes = mymodel.getNodes()
for n in nodes:
    print(n)
