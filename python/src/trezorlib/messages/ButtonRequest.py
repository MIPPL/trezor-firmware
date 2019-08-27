# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeButtonRequestType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeButtonRequestType = None  # type: ignore


class ButtonRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 26

    def __init__(
        self,
        code: EnumTypeButtonRequestType = None,
        data: str = None,
    ) -> None:
        self.code = code
        self.data = data

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('code', p.EnumType("ButtonRequestType", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)), 0),
            2: ('data', p.UnicodeType, 0),
        }