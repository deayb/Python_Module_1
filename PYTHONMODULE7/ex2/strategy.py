from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: object) -> bool:
        ...
    
    @abstractmethod
    def act(self, creature: object) -> None:
        ...
    

class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return True

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Invalid creature for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            name = getattr(creature, "name", "unknown")
            raise InvalidStrategyError(f"Invalid Creature '{name}' for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            name = getattr(creature, "name", "unknown")
            raise InvalidStrategyError(f"Invalid Creature '{name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())