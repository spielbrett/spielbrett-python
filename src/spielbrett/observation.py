import inspect
from collections import defaultdict
from typing import TYPE_CHECKING, Callable, Dict, List, TypeVar

from spielbrett.typing import PlayerIndex
if TYPE_CHECKING:
    from spielbrett.game import Game

_R = TypeVar('_R')

_observations: Dict[str, List[str]] = defaultdict(list)


def observation(fn: Callable[["Game", PlayerIndex], _R]) -> Callable[["Game", PlayerIndex], _R]:
    """Designates the provided instance method as an observation."""

    # The current frame is a decorator, the parent frame is a class
    # the method is declared in
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to decorate observation")

    parent_frame = current_frame.f_back
    if parent_frame is None:
        raise RuntimeError("Failed to decorate observation")

    class_name = parent_frame.f_code.co_name
    _observations[class_name].append(fn.__name__)
    return fn
