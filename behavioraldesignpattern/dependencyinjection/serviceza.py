"""
Le module serviceza offre les services suivants :
- serves()
"""
from abc import ABC, abstractmethod
from DesignPattern.logza import LogZa



class ServiceZa:
    """
    ServiceZa vous offre différents services
    """

    def __init__(self):
        LogZa.log_za("Je suis le constructeur de ServiceZa.")

    def serves(self) -> None:
        """
        Rend service à une tierce personne
        """
        LogZa.log_za("Je suis une des fonctionnalités de ServiceZa.")
        LogZa.log_za("J'ai fait quelque chose de cool pour vous!")


class ServiceIntZa(ABC):
    """
    interface/abstract base class
    """

    @abstractmethod
    def serves(self):
        """
        Implémenter cette fonction si vous voulez rendre un service à quelqu'un.
        """
        pass
