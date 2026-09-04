from dataclasses import dataclass
from pathlib import Path
from core.models.posts.content import Content


@dataclass
class Post:
    title: str
    content: Content
    slug: str = ""
    date: str = ""
    description: str | None = None

    @property
    def preview_image(self) -> Path | None:
        return self.content.preview_image

    def generate_markdown(self) -> str:
        return self.content.to_markdown()

    def render_card(self) -> str:
        img_html = ""
        if self.preview_image:
            clean_path = str(self.preview_image).lstrip("/")
            img_html = f'<div class="post-preview-thumb"><img src="/resources/{clean_path}" alt="{self.title}"></div>'

        desc_html = f'<p class="post-card-desc">{self.description}</p>' if self.description else ""
        date_html = f'<span class="post-card-date">{self.date}</span>' if self.date else ""

        return f"""<a href="/p/{self.slug}" class="post-card">
    {img_html}
    <div class="post-card-body">
        <div class="post-card-header">
            <span class="post-card-title">{self.title}</span>
            {date_html}
        </div>
        {desc_html}
    </div>
</a>"""
