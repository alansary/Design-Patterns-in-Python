from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class IObservable(ABC):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self):
        pass


class WeatherStation(IObservable):
    def __init__(self):
        self.observers = list()
        self.temperature = 0.0

    def attach(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_state(self, temp):
        self.temperature = temp
        self.notify()

    def get_state(self):
        return self.temperature


class PhoneDisplay(IObserver):
    def __init__(self, weather_station: WeatherStation) -> None:
        self.weather_station = weather_station
        self.weather_station.attach(self)

    def update(self):
        print(self, "State Updated", self.weather_station.get_state())


class WindowDisplay(IObserver):
    def __init__(self, weather_station: WeatherStation) -> None:
        self.weather_station = weather_station
        self.weather_station.attach(self)

    def update(self):
        print(self, "State Updated", self.weather_station.get_state())


def main():
    weather_station = WeatherStation()
    phone_display = PhoneDisplay(weather_station)
    window_display = WindowDisplay(weather_station)
    weather_station.set_state(1.0)
    weather_station.set_state(2.0)


if __name__=="__main__":
    main()