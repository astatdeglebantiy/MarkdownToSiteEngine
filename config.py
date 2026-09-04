import os
from pathlib import Path
from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).parent.resolve()

load_dotenv(BASE_DIR / ".env")

CONFIG_YAML_PATH = BASE_DIR / "config.yaml"
YAML_CONFIG = {}

if CONFIG_YAML_PATH.exists():
    with open(CONFIG_YAML_PATH, "r", encoding="utf-8") as f:
        YAML_CONFIG = yaml.safe_load(f) or {}

POSTS_DIR = BASE_DIR / "inwards"
STATIC_DIR = BASE_DIR / "static"
RESOURCES_DIR = BASE_DIR / "resources"
TEMPLATES_DIR = BASE_DIR / "templates"

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", "3000"))

SITE_TITLE = YAML_CONFIG.get("site_title", "Site Title")
DEFAULT_PAGE = YAML_CONFIG.get("default_page", "index")
GITHUB_LINK = YAML_CONFIG.get("github_link", "https://github.com/astatdeglebantiy/MarkdownToSiteEngine")

POSTS_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)
RESOURCES_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)