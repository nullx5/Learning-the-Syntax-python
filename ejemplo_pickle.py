import pickle

def main():
    mifichero = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle.dat", "wb")
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
    mifichero.close() # Close the output file

    mifichero = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle.dat", "rb")
    misdatos = []
    for i in range(6):
        misdatos.append(pickle.load(mifichero))
    print("Hemos escrito datos en el fichero ejemplo_pickle.dat.")
    print("Posteriormente los hemos leído y pasado a una lista. Su contenido es:")
    print(misdatos)
    mifichero.close()

main()
