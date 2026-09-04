from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Content:
    contents: list[str | Path] = field(default_factory=list)

    @property
    def preview_image(self) -> Path | None:
        for item in self.contents:
            if isinstance(item, Path):
                return item
        return None

    def to_markdown(self) -> str:
        parts = []
        for item in self.contents:
            if isinstance(item, Path):
                clean_path = str(item).lstrip("/")
                parts.append(f"\n![](/resources/{clean_path})\n")
            else:
                parts.append(str(item))
        return "\n".join(parts)