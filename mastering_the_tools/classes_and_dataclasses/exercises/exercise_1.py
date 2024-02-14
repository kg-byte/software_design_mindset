from dataclasses import dataclass, field


@dataclass
class A:
    length:int = 0


@dataclass
class B:
    x:int
    y: str
    l: list[int] = field(default_factory=list)

@dataclass
class C:
    a: int
    b: int = field(init=False)
    
    def __post_init__(self):
        self.b = self.a + 3

