class Subsystem1:
    def operation_1(self) -> str:
        return "Subsystem 1: Ready!"
    # ...
    def operation_n(self) -> str:
        return "Subsystem 1: Go!"


class Subsystem2:
    def operation_1(self) -> str:
        return "Subsystem 2: Get Ready!"
    # ...
    def operation_n(self) -> str:
        return "Subsystem 2: Fire!"


class Facade:
    def __init__(self, subsystem_1: Subsystem1, subsystem_2: Subsystem2) -> None:
        self._subsystem_1 = subsystem_1 or Subsystem1()
        self._subsystem_2 = subsystem_2 or Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_1.operation_1())
        results.append(self._subsystem_2.operation_1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_1.operation_n())
        results.append(self._subsystem_2.operation_n())
        return "\n".join(results)


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


def main():
    subsystem_1 = Subsystem1()
    subsystem_2 = Subsystem2()
    facade = Facade(subsystem_1, subsystem_2)
    client_code(facade)


if __name__=="__main__": main()