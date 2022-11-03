class LogZa:
    """
    LogZa fournit des fonctions qui vous peermettent d'écrire le journal chronologique de l'exécution de votre application.
    Format : csv.
    Structure : counter, message
    """

    counter = 0

    @classmethod
    def log_za(cls, message: str) -> None:
        """
        Permet d'écrire le journal chronologique de l'exécution de votre application. Format : csv. Structure : counter, message
        """
        cls.counter += 1
        print(f"{cls.counter}, {message}")


if __name__ == "__main__":
#    LogZa.log_za("Test")
    pass