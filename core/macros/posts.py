from pathlib import Path
import config
from core.macros.base import BaseMacro
from core.models.posts.content import Content
from core.models.posts.post import Post


class PostsListMacro(BaseMacro):
    @property
    def name(self) -> str:
        return "posts_list"

    def execute(self, arg: str) -> str:
        folder_prefix = arg.strip().strip("'\"") or ""
        target_dir = config.POSTS_DIR / folder_prefix

        if not target_dir.exists():
            return "> Матеріалів поки немає."

        posts = []
        for f in sorted(target_dir.rglob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True):
            if f.name == "index.md":
                continue

            try:
                raw = f.read_text(encoding="utf-8")
                slug = f.relative_to(config.POSTS_DIR).with_suffix("").as_posix()

                title = f.stem
                desc = None
                date_str = ""

                if raw.startswith("---"):
                    parts = raw.split("---", 2)
                    if len(parts) >= 3:
                        for line in parts[1].strip().splitlines():
                            if ":" in line:
                                k, v = line.split(":", 1)
                                k, v = k.strip(), v.strip().strip("'\"")
                                if k == "title":
                                    title = v
                                elif k == "description":
                                    desc = v
                                elif k == "date":
                                    date_str = v

                post = Post(
                    title=title,
                    slug=slug,
                    date=date_str,
                    description=desc,
                    content=Content(contents=[raw])
                )
                posts.append(post)
            except Exception:
                pass

        if not posts:
            return "> Матеріалів поки немає."

        cards_html = "\n".join(p.render_card() for p in posts)
        return f'<div class="posts-grid">\n{cards_html}\n</div>'
