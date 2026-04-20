from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from ex2.exceptions import InvalidStrategyCreatureError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature) -> None:
        print(creature.attack())

    def is_valid(self, creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                "Invalid Creature "
                f"'{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                "Invalid Creature "
                f"'{creature.name}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)
