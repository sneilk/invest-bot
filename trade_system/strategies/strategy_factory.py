from typing import Optional

from trade_system.strategies.change_and_volume_strategy import ChangeAndVolumeStrategy
from trade_system.strategies.base_strategy import IStrategy

__all__ = ("StrategyFactory")


class StrategyFactory:
    """
    Fabric for strategies. Put here new strategy.
    """
    @staticmethod
    def new_factory(strategy_name: str, *args, **kwargs) -> Optional[IStrategy]:
        if strategy_name == "ChangeAndVolumeStrategy":
            return ChangeAndVolumeStrategy(*args, **kwargs)
        else:
            return None
