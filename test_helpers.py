class FakeRNG:
    def __init__(
        self,
        uniforms: list[float],
        randints: list[int],
        choices: list | None = None,
    ):
        self._uniforms = iter(uniforms)
        self._randints = iter(randints)
        self._choices = iter(choices) if choices is not None else None

    def uniform(self, a: float, b: float) -> float:
        return next(self._uniforms)

    def randint(self, a: int, b: int) -> int:
        return next(self._randints)

    def choice(self, seq):
        if self._choices is not None:
            return next(self._choices)
        return seq[0]
