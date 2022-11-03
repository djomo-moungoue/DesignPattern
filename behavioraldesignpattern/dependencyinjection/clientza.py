from serviceza import ServiceZa, ServiceIntZa
from DesignPattern.logza import LogZa


class ClientZa1:
    """
    Injection de constructeur, où les dépendances sont fournies par le constructeur de classe d'un client.
    """

    def __init__(self, name: str, service_za: ServiceZa): # injection de constructeur
        LogZa.log_za(f"Je suis le constructeur de {name}")
        LogZa.log_za("Service injecté dans le constructeur.")
        self.service_za = service_za
        LogZa.log_za("Fonctionnalité du service utilisé dans le constructeur")
        self.service_za.serves()

    def do_something(self):
        LogZa.log_za("Fonctionnalité du service utilisé dans une fonction")
        self.service_za.serves()


class ClientZa2:
    """
    Injection de function par typage des canards, où le client expose une méthode qui accepte la dépendance sans
    se soucier de savoir s'il est un canard, mais se soucie uniquement de savoir s'il fait coin-coin.
    """

    def __init__(self, name: str):
        LogZa.log_za(f"Je suis le constructeur de {name}")

    def do_something(self, service_za: ServiceZa) -> None:
        LogZa.log_za("Service injecté dans une fonction par typage des canards.")
        service_za.serves()


class ClientZa31(ServiceZa):
    """
    Injection de classe de base, où la classe de base de la dépendance fournit une méthode d'injection qui injectera
    la dépendance dans tout client qui lui est passé.
    """

    def __init__(self, name: str):
        LogZa.log_za(f"Je suis le constructeur de {name}")
        LogZa.log_za("Fonctionnalité du service utilisé, par héritage, dans le constructeur.")
        self.serves()

    def do_something(self):
        LogZa.log_za("Fonctionnalité du service utilisé, par héritage, dans une des fonctions.")
        self.serves()


class ClientZa32(ServiceIntZa):
    """
    Injection d'interfaces, où l'interface de la dépendance fournit une méthode d'injection qui injectera la dépendance
    dans tout client qui lui est passé.
    """

    def __init__(self, name: str):
        LogZa.log_za(f"Je suis le constructeur de {name}")

    def serves(self):
        LogZa.log_za("Signature implémenté ici.")
        LogZa.log_za("j'ai fait quelque chose de bien pour moi.")


class ClientZa4:
    """
    Sans injection de dépendance, où le client construit et contrôle directement le Service dans le constructeur ou une
    de ces fonctions créant ainsi une dépendance codée en dur.
    """

    def __init__(self, name: str):
        LogZa.log_za(f"Je suis le constructeur de {name}")
        LogZa.log_za(f"J'utilise le service, à travers un codage en dur, dans le constructeur.")
        self.service_za = ServiceZa()
        self.service_za.serves()

    def do_something(self):
        LogZa.log_za(f"J'utilise le service, à travers un codage en dur, dans une fonction.")
        self.service_za.serves()


if __name__ == "__main__":
    print("ClientZa1")
    client_za1 = ClientZa1("ClientZa1", ServiceZa())
    client_za1.do_something()
    """
    ClientZa2
    1, Je suis le constructeur de ServiceZa.
    2, Je suis le constructeur de ClientZa1
    3, Service injecté dans le constructeur.
    4, Fonctionnalité du service utilisé dans le constructeur
    5, Je suis une des fonctionnalités de ServiceZa.
    6, J'ai fait quelque chose de cool pour vous!
    7, Fonctionnalité du service utilisé dans une fonction
    8, Je suis une des fonctionnalités de ServiceZa.
    9, J'ai fait quelque chose de cool pour vous!
    """

    print("\nClientZa2")
    Client_za2 = ClientZa2("ClientZa2")
    Client_za2.do_something(ServiceZa())
    """
    ClientZa2
    10, Je suis le constructeur de ClientZa2
    11, Je suis le constructeur de ServiceZa.
    12, Service injecté dans une fonction par typage des canards.
    13, Je suis une des fonctionnalités de ServiceZa.
    14, J'ai fait quelque chose de cool pour vous!
    """

    print("\nClientZa31")
    client_za31 = ClientZa31("ClientZa31")
    client_za31.do_something()
    """
    ClientZa31
    15, Je suis le constructeur de ClientZa31
    16, Fonctionnalité du service utilisé, par héritage, dans le constructeur.
    17, Je suis une des fonctionnalités de ServiceZa.
    18, J'ai fait quelque chose de cool pour vous!
    19, Fonctionnalité du service utilisé, par héritage, dans une des fonctions.
    20, Je suis une des fonctionnalités de ServiceZa.
    21, J'ai fait quelque chose de cool pour vous!
    """

    print("\nClientZa32")
    client_za32 = ClientZa32("ClientZa32")
    client_za32.serves()
    """
    ClientZa32
    22, Je suis le constructeur de ClientZa32
    23, Signature implémenté ici.
    24, j'ai fait quelque chose de bien pour moi.
    """

    print("\nClientZa4")
    client_za4 = ClientZa4("ClientZa4")
    client_za4.do_something()
    """
    ClientZa4
    25, Je suis le constructeur de ClientZa4
    26, J'utilise le service, à travers un codage en dur, dans le constructeur.
    27, Je suis le constructeur de ServiceZa.
    28, Je suis une des fonctionnalités de ServiceZa.
    29, J'ai fait quelque chose de cool pour vous!
    30, J'utilise le service, à travers un codage en dur, dans une fonction.
    31, Je suis une des fonctionnalités de ServiceZa.
    32, J'ai fait quelque chose de cool pour vous!
    """
