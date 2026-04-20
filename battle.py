from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing factory")
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def test_battle(factory1, factory2) -> None:
    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()

    print("Testing battle")
    print(base_creature1.describe())
    print("vs.")
    print(base_creature2.describe())
    print("fight!")

    print(base_creature1.attack())
    print(base_creature2.attack())


def battle() -> None:
    factories = [FlameFactory(), AquaFactory()]

    for factory in factories:
        test_factory(factory)

    test_battle(factories[0], factories[1])


if __name__ == "__main__":
    battle()
