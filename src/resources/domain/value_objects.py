from dataclasses import dataclass
import validators
from src.resources.domain.exceptions import UrlNotValidException

@dataclass(frozen=True,kw_only=True)
class ResourceUrl:
    value:str

    def __post_init__(self) -> None:
        if not validators.url(self.value):
            raise UrlNotValidException

