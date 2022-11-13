from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from spielbrett.typing import PlayerIndex


class InstanceHostAPI(ABC):
    @abstractmethod
    def update_observation(self, player_index: PlayerIndex, observation: Dict[str, Any]) -> None:
        pass


instance_host_api: Optional[InstanceHostAPI] = None


def get_instance_host_api() -> Optional[InstanceHostAPI]:
    return instance_host_api


def set_instance_host_api(new_instance_host_api: InstanceHostAPI):
    global instance_host_api
    instance_host_api = new_instance_host_api
