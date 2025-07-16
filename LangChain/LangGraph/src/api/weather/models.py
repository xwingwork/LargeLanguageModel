from typing import TypedDict, Annotated, Sequence
import operator

# 上下文傳遞模型
class AllState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]

