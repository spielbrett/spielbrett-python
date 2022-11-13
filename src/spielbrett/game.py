from typing import Any, Dict

from spielbrett._instance_host import get_instance_host_api
from spielbrett.observation import _observations
from spielbrett.typing import PlayerIndex


class Game:
    """Base class for Project Spielbrett games."""

    def __init__(self) -> None:
        self._max_player_index = -1

    def _add_player(self) -> PlayerIndex:
        self._max_player_index += 1
        return self._max_player_index

    def _get_all_observations(self, player_index: PlayerIndex) -> Dict[str, Any]:
        class_name = self.__class__.__name__
        observations = {
            observation_name: self.__getattribute__(observation_name)(player_index)
            for observation_name in _observations[class_name]
        }
        return observations

    def _on_action(self) -> None:
        for player_index in range(self._max_player_index + 1):
            observation = self._get_all_observations(player_index)

            iha = get_instance_host_api()
            if iha is not None:
                iha.update_observation(player_index, observation)
