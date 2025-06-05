def interesse_composto(capitale, tasso_annuo, anni):
    """
    Calcola l'interesse composto.
    :param capitale: Capitale iniziale
    :param tasso_annuo: Tasso annuale in percentuale
    :param anni: Numero di anni
    :return: Capitale finale
    """
    return capitale * (1 + tasso_annuo / 100) ** anni

if __name__ == "__main__":
    risultato = interesse_composto(1700, 2, 5)
    print(f"Totale dopo 5 anni: {risultato:.2f} €")
