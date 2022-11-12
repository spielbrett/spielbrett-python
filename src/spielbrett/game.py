import functools

from typing import Callable, Concatenate, ParamSpec, TypeVar


P = ParamSpec('P')
R = TypeVar('R')


class Game:
    def _on_action(self):
        pass


PlayerIndex = int


def action(
    fn: Callable[Concatenate[Game, PlayerIndex, P], R]
) -> Callable[Concatenate[Game, PlayerIndex, P], R]:
    @functools.wraps(fn)
    def decorated_fn(game: Game, player_index: PlayerIndex, *args: P.args, **kwargs: P.kwargs) -> R:
        res = fn(game, player_index, *args, **kwargs)
        game._on_action()
        return res

    return decorated_fn


def observation(
    fn: Callable[Concatenate[Game, PlayerIndex, P], R]
) -> Callable[Concatenate[Game, PlayerIndex, P], R]:
    # TODO: Register observation in a class it was declared in
    return fn
