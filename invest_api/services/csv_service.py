import logging

from tinkoff.invest import PositionsSecurities


__all__ = ("CSVService")

logger = logging.getLogger(__name__)


class CSVService:
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def save_positions(self, positions: list[PositionsSecurities]) -> None:
        pass


    def get_positions(self) -> list[PositionsSecurities]:
        pass