# 🚀 MarkdownToSiteEngine

A lightweight, flexible, and fast Python-based engine that transforms Markdown files into a dynamic, template-driven website or blog.

---

## 📖 Overview

**MarkdownToSiteEngine** simplifies publishing Markdown documents to the web. It uses file-system-based routing, a custom macro/rule system for dynamic content injection, and a built-in server with template support.

---

## ✨ Features

- **📂 File-System Routing:** Structure your pages naturally inside the `inwards/` directory (`index.md`, nested folders, posts).
- **🧩 Custom Macro System:** Extend Markdown with dynamic macros (`core/macros/`) to fetch recent posts, inject metadata, or render complex UI components.
- **🎨 Templating & Static Assets:** Jinja-like-ready HTML layout support (`templates/`) with dedicated `static/` (CSS/JS) and `resources/` (media/downloads) pipelines.
- **⚡ Fast Package Management:** Built and configured for `uv` and modern Python packaging via `pyproject.toml`.
- **🐳 Docker-Ready:** Includes template files for containerized production deployment.
- **⚙️ Flexible Configuration:** Manage site settings via `config.yaml` and sensitive secrets using `.env`.

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.12+**
- [**uv**](https://github.com/astral-sh/uv) (recommended) or standard `pip` / `venv`

---

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/astatdeglebantiy/MarkdownToSiteEngine.git
   cd MarkdownToSiteEngine
   ```

2. **Set up the virtual environment & install dependencies:**

   *Using `uv` (recommended):*
   ```bash
   uv sync
   ```

   *Using standard `pip`:*
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install .
   ```

3. **Configure Environment:**
   Copy example configuration files:
   ```bash
   cp .EXAMPLE.env .env
   ```
   Adjust settings in `.env` and `config.yaml` to fit your needs.

---

## 🚀 Running the Server

Start the local development server:

```bash
# Using uv
uv run main.py

# Using standard Python
python main.py
```

By default, the server will be available at:  
👉 **`http://localhost:3000`** *(or the port configured in `.env`)*

---

## 📝 Content Creation & Routing

Add Markdown files inside the `inwards/` directory to create pages:

| File Location | Route |
| :--- | :--- |
| `inwards/index.md` | `/` |
| `inwards/example.md` | `/example` |
| `inwards/example/subpage.md` | `/example/subpage` |
| `inwards/posts/first_post.md` | `/posts/first_post` |

### Using Assets

- Place global stylesheets and scripts in `/static/` (`/static/style.css`, `/static/app.js`).
- Store media, documents, and images inside `/resources/` and reference them directly in your Markdown files.

---

## 🐳 Running with Docker

1. Create a `Dockerfile` from the provided example:
   ```bash
   cp EXAMPLEDockerfile Dockerfile
   ```

2. Build and run the Docker image:
   ```bash
   docker build -t markdown-to-site-engine .
   docker run -d -p 3000:3000 --env-file .env markdown-to-site-engine
   ```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).