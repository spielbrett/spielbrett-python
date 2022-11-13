import functools
import inspect
from collections import defaultdict
from typing import Callable, Concatenate, Dict, List, ParamSpec, TypeVar

from spielbrett.typing import PlayerIndex

_P = ParamSpec('_P')
_R = TypeVar('_R')

Game = "Game"

_actions: Dict[str, List[str]] = defaultdict(list)


def action(
    fn: Callable[Concatenate[Game, PlayerIndex, _P], _R]
) -> Callable[Concatenate[Game, PlayerIndex, _P], _R]:
    """Designates the provided instance method as an action."""

    @functools.wraps(fn)
    def decorated_fn(
        game: Game, player_index: PlayerIndex,
        *args: _P.args, **kwargs: _P.kwargs
    ) -> _R:
        res = fn(game, player_index, *args, **kwargs)
        game._on_action()
        return res

    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to decorate action")

    parent_frame = current_frame.f_back
    if parent_frame is None:
        raise RuntimeError("Failed to decorate action")

    class_name = parent_frame.f_code.co_name
    _actions[class_name].append(fn.__name__)
    return decorated_fn


# TODO: Implement simultaneous actions (e.g. voting)
# TODO: Implement timed actions
