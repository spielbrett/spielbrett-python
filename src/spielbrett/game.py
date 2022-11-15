import ast
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

    def perform_action(self, player_index: PlayerIndex, action: str) -> None:
        """
        Parses the action argument and performs the corresponding action
        as the provided user.
        """

        if '\n' in action:
            raise ValueError("action string must not contain line breaks")

        a = ast.parse(action)
        if not (len(a.body) == 1 and isinstance(a.body[0], ast.Expr)):
            raise ValueError("action must be a single expression")

        expr_value = a.body[0].value
        if not (isinstance(expr_value, ast.Call) and isinstance(expr_value.func, ast.Name)):
            raise ValueError("action must be a function call")

        action_name = expr_value.func.id
        action_args = [ast.literal_eval(arg) for arg in expr_value.args]

        self.__getattribute__(action_name)(player_index, *action_args)
