from typing import Tuple, Union

from typing_extensions import Final

TIMEOUT_TYPE = Union[int, Tuple[int, int]]
DEFAULT_TIMEOUT: Final[int] = 60
