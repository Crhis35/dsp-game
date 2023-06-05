
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from interfaces.stats import Stats


class ItemRole(Enum):
    MELEE = 'MELEE',
    MAGIC = 'MAGIC',
    TANK = 'TANK',


@dataclass
class Items(ABC):
    role: ItemRole
    name: str
    attributes: Optional[List[Stats]] = []
