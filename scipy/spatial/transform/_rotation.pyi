from __future__ import annotations
from typing import TYPE_CHECKING, Union, Tuple, Optional, Sequence
import numpy as np

if TYPE_CHECKING:
    import numpy.typing as npt

_IntegerType = Union[int, np.integer]


class Rotation:
    def __init__(self, quat: npt.ArrayLike, normalize: bool = ..., copy: bool = ...) -> None: ...
    @property
    def single(self) -> bool: ...
    def __len__(self) -> int: ...
    @classmethod
    def from_quat(cls, quat: npt.ArrayLike) -> Rotation: ...
    @classmethod
    def from_matrix(cls, matrix: npt.ArrayLike) -> Rotation: ...
    @classmethod
    def from_rotvec(cls, rotvec: npt.ArrayLike) -> Rotation: ...
    @classmethod
    def from_euler(cls, axes: npt.ArrayLike, extrinsic: bool, angles: Union[float, npt.ArrayLike], degrees: bool = ...) -> Rotation: ...
    @classmethod
    def from_davenport(cls, seq: str, angles: Union[float, npt.ArrayLike], degrees: bool = ...) -> Rotation: ...
    @classmethod
    def from_mrp(cls, mrp: npt.ArrayLike) -> Rotation: ...
    def as_quat(self) -> np.ndarray: ...
    def as_matrix(self) -> np.ndarray: ...
    def as_rotvec(self) -> np.ndarray: ...
    def as_euler(self, seq: str, degrees: bool = ...) -> np.ndarray: ...
    def as_davenport(self, axes: npt.ArrayLike, extrinsic: bool, degrees: bool = ...) -> np.ndarray: ...
    def as_mrp(self) -> np.ndarray: ...
    @classmethod
    def concatenate(cls, rotations: Sequence[Rotation]) -> Rotation: ...
    def apply(self, vectors: npt.ArrayLike, inverse: bool = ...) -> np.ndarray: ...
    def __mul__(self, other: Rotation) -> Rotation: ...
    def inv(self) -> Rotation: ...
    def magnitude(self) -> Union[np.ndarray, float]: ...
    def mean(self, weights: Optional[npt.ArrayLike] = ...) -> Rotation: ...
    def reduce(self, left: Optional[Rotation] = ..., right: Optional[Rotation] = ...,
               return_indices: bool = ...) -> Union[Rotation, Tuple[Rotation, np.ndarray, np.ndarray]]: ...
    @classmethod
    def create_group(cls, group: str, axis: str = ...) -> Rotation: ...
    def __getitem__(self, indexer: Union[int, slice, npt.ArrayLike]) -> Rotation: ...
    @classmethod
    def identity(cls, num: Optional[int] = ...) -> Rotation: ...
    @classmethod
    def random(cls, num: Optional[int] = ...,
               random_state: Optional[Union[_IntegerType,
                                            np.random.Generator,
                                            np.random.RandomState]] = ...) -> Rotation: ...
    @classmethod
    def align_vectors(cls, a: npt.ArrayLike, b: npt.ArrayLike,
                      weights: Optional[npt.ArrayLike] = ...,
                      return_sensitivity: bool = ...) -> Union[Tuple[Rotation, float], Tuple[Rotation, float, np.ndarray]]:...

class Slerp:
    def __init__(self, times: npt.ArrayLike, rotations: Rotation) -> None: ...
    def __call__(self, times: npt.ArrayLike) -> Rotation: ...
