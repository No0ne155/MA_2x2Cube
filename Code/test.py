# Die beiden Programme Importieren
import py222
import solver

# Einen Cube genannt myCube erstellen, und in Grundposition definieren
Cube = py222.initState()

# Dr Cube führt nun den folgenden Bewegungsablauf durch
Cube = py222.doAlgStr(Cube, "R U2 R2 F2 R' F2 R F R")

# Der Cube wird vom solver-Programm gelöst
solver.solveCube(Cube)