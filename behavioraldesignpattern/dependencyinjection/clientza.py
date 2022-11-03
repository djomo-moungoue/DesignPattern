from serviceza import ServiceZa, ServiceIntZa


class ClientZa1:
    """
    Injection de constructeur, où les dépendances sont fournies par le constructeur de classe d'un client.
    """

    def __init__(self, name: str, serviceza: ServiceZa):
        print(f"I'm {name}, the client")
        print(f"I'm using the service via constructor injection.")
        serviceza.serves()


class ClientZa2:
    """
    Injection de function par typage des canards, où le client expose une méthode qui accepte la dépendance sans
    se soucier de savoir s'il est un canard, mais se soucie uniquement de savoir s'il fait coin-coin.
    """

    def __init__(self, name: str):
        print(f"I'm {name}, the client")

    def do_something(self, serviceza: ServiceZa) -> None:
        print(f"I'm using the service via ducktyping function injection.")
        serviceza.serves()


class ClientZa31(ServiceZa):
    """
    Injection d'interfaces ou parents, où l'interface ou la classe de base de la dépendance fournit une méthode
    d'injection qui injectera la dépendance dans tout client qui lui est passé.
    """

    def __init__(self, name: str):
        print(f"I'm {name}, the client")
        super().serves()


class ClientZa32(ServiceIntZa):
    """
    Injection d'interfaces ou parents, où l'interface ou la classe de base de la dépendance fournit une méthode
    d'injection qui injectera la dépendance dans tout client qui lui est passé.
    """

    def __init__(self, name: str):
        print(f"I'm {name}, the client")

    def serves(self):
        print(f"I did something cool for you.")


class ClientZa4:
    """
    Sans injection de dépendance, où le client construit et contrôle directement le Service dans le constructeur
    créant ainsi une dépendance codée en dur.
    """

    def __init__(self, name: str):
        print(f"I'm {name}, the client. I'm using the service via hard coding.")
        self.serviceza = ServiceZa()
        self.serviceza.serves()


if __name__ == "__main__":
    print("ClientZa1")
    client_za1 = ClientZa1("ClientZa1", ServiceZa())
    # I'm ClientZa1, the client. 2
    # I'm using the service via constructor injection. 3
    # I'm ServiceZa, the service constructor." 1
    # I'm ServiceZa, the service function. 4
    # I did something cool for you." 5

    print("\nClientZa2")
    Client_za2 = ClientZa2("ClientZa2")
    Client_za2.do_something(ServiceZa())
    # I'm ClientZa2, the client. 1
    # I'm using the service via ducktyping function injection.3
    # I'm ServiceZa, the service constructor." 2
    # I'm ServiceZa, the service function. 4
    # I did something cool for you." 5

    print("\nClientZa31")
    client_za31 = ClientZa31("ClientZa31")
    # I'm ClientZa31, the client. 1
    # I'm using the service via base class injection.
    # I'm ServiceZa, the service constructor."
    # I did something cool for you." 3
    # I'm ServiceZa, the service function. 2

    print("\nClientZa32")
    client_za32 = ClientZa32("ClientZa32")
    client_za32.serves()
    # I'm ClientZa32, the client. 1
    # I'm using the service via interface injection.
    # I'm ServiceZa, the service function."
    # I did something cool for you." 2

    print("\nClientZa4")
    client_za4 = ClientZa4("ClientZa4")
    # I'm ClientZa4, the client. I'm using the service via hard coding. 1
    # I'm ServiceZa, the service function." 3
    # I did something cool for you." 4
    # I'm ServiceZa, the service constructor. 2
