from typing import TYPE_CHECKING, Callable, Concatenate, ParamSpec, TypeVar

from spielbrett.typing import PlayerIndex
if TYPE_CHECKING:
    from spielbrett.game import Game

_P = ParamSpec('_P')
_R = TypeVar('_R')


def action(
    fn: Callable[Concatenate["Game", PlayerIndex, _P], _R]
) -> Callable[Concatenate["Game", PlayerIndex, _P], _R]:
    """Designates the provided instance method as an action."""

    # Currently a no-op, a validation that the method is indeed an action
    # would possibly be added in the future
    return fn


# TODO: Implement simultaneous actions (e.g. voting)
# TODO: Implement timed actions
