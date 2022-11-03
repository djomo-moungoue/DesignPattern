"""
Le module serviceza offre les services suivants :
- serves()
"""
from abc import ABC, abstractmethod


class ServiceZa:
    """
    ServiceZa vous offre différents services
    """

    def __init__(self):
        print(f"I'm ServiceZa, the service constructor.")

    def serves(self)->None:
        """
        Rend service à une tierce personne
        """
        print(f"I'm ServiceZa, the service function.")
        print(f"I did something cool for you.")


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
