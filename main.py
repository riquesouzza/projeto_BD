from persistencia.crudEmpresa import *
from persistencia.crudCobrador import *
from persistencia.crudPontoOnibus import *

#criarPontoOnibus("Rua Maraúba, 20")
#editarPontoOnibus(5, "Rodoviária - Plano Piloto")
#print(lerPontoOnibus(5))
#deletarPontoOnibus(6)

for dado in lerPontosOnibus():
    print(dado)