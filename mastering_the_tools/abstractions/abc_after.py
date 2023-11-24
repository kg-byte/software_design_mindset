from abc import ABC, abstractmethod
from dataclasses import dataclass


class Switchable(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


@dataclass
class Light(Switchable):
    name: str

    def on(self):
        print(f"The {self.name} light is on.")

    def off(self):
        print(f"The {self.name} light is off.")


@dataclass
class Heating(Switchable):
    name: str

    def on(self):
        print(f"The {self.name} heating is on.")

    def off(self):
        print(f"The {self.name} heating is off.")


def wake_up(devices: list[Switchable]):
    for device in devices:
        device.on()


def go_to_bed(devices: list[Switchable]):
    for device in devices:
        device.off()


def main():
    light_bedroom = Light("bedroom")
    light_living = Light("living room")
    heating = Heating("bedroom")
    wake_up([heating, light_bedroom, light_living])


if __name__ == "__main__":
    main()
