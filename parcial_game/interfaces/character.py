
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from interfaces.Item import Items

from interfaces.stats import Stats


class CharacterICharacter:
    name: str
    level: int


@dataclass
class Character(ABC, Stats):
    name: str
    level: int = 1
    health: int
    speed: int
    damage: int
    defense: int
    magia: int
    move: int
    mana: int
    items: List[Items] = []

    @abstractmethod
    def attack() -> int:
        pass

    @abstractmethod
    def level_up() -> None:
        pass

    @abstractmethod
    def activate_skill() -> None:
        pass
