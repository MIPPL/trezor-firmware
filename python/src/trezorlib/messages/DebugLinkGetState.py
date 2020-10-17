# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugLinkGetState(p.MessageType):
    MESSAGE_WIRE_TYPE = 101

    def __init__(
        self,
        *,
        wait_word_list: bool = None,
        wait_word_pos: bool = None,
        wait_layout: bool = None,
    ) -> None:
        self.wait_word_list = wait_word_list
        self.wait_word_pos = wait_word_pos
        self.wait_layout = wait_layout

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('wait_word_list', p.BoolType, None),
            2: ('wait_word_pos', p.BoolType, None),
            3: ('wait_layout', p.BoolType, None),
        }
