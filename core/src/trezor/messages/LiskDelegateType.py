# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class LiskDelegateType(p.MessageType):

    def __init__(
        self,
        *,
        username: str = None,
    ) -> None:
        self.username = username

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('username', p.UnicodeType, None),
        }
