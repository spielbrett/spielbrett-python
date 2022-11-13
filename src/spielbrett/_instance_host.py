from abc import ABC
from typing import Optional


class InstanceHostAPI(ABC):
    pass


_instance_host_api: Optional[InstanceHostAPI] = None


def get_instance_host_api() -> Optional[InstanceHostAPI]:
    return _instance_host_api


def set_instance_host_api(instance_host_api: InstanceHostAPI):
    global _instance_host_api
    _instance_host_api = instance_host_api
