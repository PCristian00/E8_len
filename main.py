def mia_len(elem):
    lun = 0
    for el in elem:
        lun += 1
    print("Lunghezza " + elem + " = " + str(lun))


e = input("Inserire lista o stringa: ")
mia_len(e)
