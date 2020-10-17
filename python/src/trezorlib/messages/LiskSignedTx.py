# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class LiskSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 117

    def __init__(
        self,
        *,
        signature: bytes = None,
    ) -> None:
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('signature', p.BytesType, None),
        }
