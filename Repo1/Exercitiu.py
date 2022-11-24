# o functie care sa ne recunoasca numele de fete sau baieti
def nume_fete(nume):
    if nume.endswith("__a"):
        print("Acest nume este de baiat." )
    else:
        print("Acest nume este de fata" )


nume_fete("Maria")
