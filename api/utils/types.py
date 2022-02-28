from typing import List,Optional, Generic, TypeVar
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")

class GenericResponse(GenericModel, Generic[DataT]):
    """
    通用返回数据
    """
    code: int = 0
    msg: str = ""
    data: Optional[DataT] = None  # 可能连data都没有
    # 设置response_model_exclude_unset=True即可