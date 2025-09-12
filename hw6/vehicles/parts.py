from dataclasses import dataclass

@dataclass(frozen=True)
class Engine:
    _kind: str = 'base engine'


    def make_sound(self):
        print(f'{self._kind} sound')


if __name__ == '__main__':
    base_eng = Engine()
    base_eng.make_sound()

    sport_eng = Engine('sport engine')
    sport_eng.make_sound()
