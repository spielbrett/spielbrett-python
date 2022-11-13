from typing import Any, Dict

from spielbrett.observation import _observations
from spielbrett.typing import PlayerIndex


class Game:
    """Base class for Project Spielbrett games."""

    def observe(self, player_index: PlayerIndex) -> Dict[str, Any]:
        """
        Returns a dictionary containing all the properties observable
        by the provided user.
        """

        return {
            observation_name: self.__getattribute__(observation_name)(player_index)
            for observation_name in _observations[self.__class__.__name__]
        }
