
from dataclasses import dataclass, field
import numpy as np
from pathlib import Path
from typing import Any, Dict, List, Tuple
from PIL import Image as PILImage


@dataclass(kw_only=True)
class Image:
    image_data: np.ndarray = field(repr=False, default=None)
    image_path: Path = None
    image_name: str = None
    image_shape: Tuple[int, int] = None
    classification: str = None
    riff_header: Dict = None
    harp_header: Dict = None
    harp_subchunk_headers: Dict = None
    transform_metadata: Dict = field(repr=False, default=None)
    spec_start_bin: int = None
    spec_end_bin: int = None
    spec_diff_bin: int = None
    spec_start_time: float = None
    spec_end_time: float = None
    spec_diff_time: float = None
    spec_length: int = None
    scaled_data: np.ndarray = field(repr=False, default=None)

    def save_image(self, save_path: Path, corpus: str):
        self.scaled_data = (self.image_data * (255.0 / self.image_data.max())).astype(np.uint8)
        im = PILImage.fromarray(self.scaled_data)
        im = im.convert("L")
        save_path = save_path / corpus / self.classification
        save_path.mkdir(parents=True, exist_ok=True)
        im.save(save_path / f"{self.image_name}.png")
