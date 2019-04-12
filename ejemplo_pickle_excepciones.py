import pickle

def main():
    mifichero = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle_excepciones.dat", "wb")
    a = 21
    b = 34.98
    c = "Jose Luis Hernández"
    d = [12, 67, 32]
    e = (90, 77)
    f = { "af": 21, "gh": 32}
    pickle.dump(a, mifichero)
    pickle.dump(b, mifichero)
    pickle.dump(c, mifichero)
    pickle.dump(d, mifichero)
    pickle.dump(e, mifichero)
    pickle.dump(f, mifichero)
    mifichero.close()

    mifichero = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle_excepciones.dat", "rb")
    misdatos = []
    fin_fichero = False
    try:
        while not fin_fichero:
            misdatos.append(pickle.load(mifichero))
    except:
        mifichero.close()
    print("Los datos que hemos almacenado en el fichero y que hemos recuperado almacenándolos")
    print("en una lista,son:")
    print(misdatos)

main()
