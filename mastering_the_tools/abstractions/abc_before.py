from dataclasses import dataclass


@dataclass
class Light:
    name: str

    def on(self):
        print(f"The {self.name} light is on.")

    def off(self):
        print(f"The {self.name} light is off.")


@dataclass
class Heating:
    name: str

    def on(self):
        print(f"The {self.name} heating is on.")

    def off(self):
        print(f"The {self.name} heating is off.")


def wake_up(heating: Heating, light: Light):
    heating.on()
    light.on()


def go_to_bed(heating: Heating, light: Light):
    heating.off()
    light.off()


def main():
    light = Light("bedroom")
    heating = Heating("bedroom")
    wake_up(heating, light)


if __name__ == "__main__":
    main()
