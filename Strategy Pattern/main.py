from abc import ABC, abstractmethod


class IQuackBehavior(ABC):
	@abstractmethod
	def quack(self):
		pass


class SimpleQuack(IQuackBehavior):
	def quack(self):
		print("Simple Quack")


class NoQuack(IQuackBehavior):
	def quack(self):
		print("No Quack")


class IDisplayBehavior(ABC):
	@abstractmethod
	def display(self):
		pass


class GraphicsDisplay(IDisplayBehavior):
	def display(self):
		print("Graphics Display")


class TextDisplay(IDisplayBehavior):
	def display(self):
		print("Text Display")


class IFlyBehavior(ABC):
	@abstractmethod
	def fly(self):
		pass


class JetFly(IFlyBehavior):
	def fly(self):
		print("Ject Fly")


class NoFly(IFlyBehavior):
	def fly(self):
		print("No Fly")


class Duck:
	def __init__(self, qb: IQuackBehavior, db: IDisplayBehavior, fb: IFlyBehavior) -> None:
		self._qb = qb
		self._db = db
		self._fb = fb

	def quack(self):
		self._qb.quack()

	def display(self):
		self._db.display()

	def fly(self):
		self._fb.fly()


def client_code():
	duck = Duck(SimpleQuack(), TextDisplay(), NoFly())
	duck.quack()
	duck.display()
	duck.quack()


def main():
	client_code()


if __name__ == "__main__":
	main()
