from ManejadorHelados import ManejaHelados
from ManejadorSabores import ManejaSabores
from Menu import menu
if __name__=='__main__':
    MH = ManejaHelados()
    MH.test2()
    print('\n')

    MS = ManejaSabores()
    MS.initms()
    MS.test()
    print('\n')

    menu(MH,MS)

    
