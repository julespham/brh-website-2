# Boston Robot Hackers Website

Static website generator for the Boston Robot Hackers community built with Python, Jinja2 templates, and UV package management.

## Prerequisites

- Python 3.8 or higher
- UV package manager (installation instructions below)

## Installation

### 1. Install UV (if not already installed)

UV is a fast Python package manager. Install it using one of these methods:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

### 2. Clone and Set Up Project

```bash
git clone https://github.com/Boston-Robot-Hackers/brh-website-2.git
cd brh-website-2
```

### 3. Install Dependencies

UV will automatically create a virtual environment and install all dependencies:

```bash
uv sync
```

## Usage

### Build the Website

Generate the complete website in the `output/` directory:

```bash
uv run python build/build.py
```

### Development Workflow

1. Edit content files in the `content/` directory (markdown format)
2. Modify templates in the `templates/` directory (Jinja2 format)
3. Update styles in the `css/` directory
4. Run the build command to regenerate the site
5. Check the `output/` directory for generated files

## Project Structure

```
├── build/build.py          # Main build script
├── content/               # Markdown content files
│   ├── heroes/           # Hero section content for each page
│   ├── news/             # News/announcements
│   ├── projects/         # Project descriptions
│   └── members/          # Member profiles
├── templates/            # Jinja2 templates
│   ├── pages/           # Page templates
│   ├── components/      # Reusable components
│   └── layouts/         # Base layouts
├── css/                 # Stylesheets
├── images/              # Static images
├── scripts/             # JavaScript files
├── config/              # Site configuration
└── output/              # Generated website (created by build)
```

## Content Management

- **Hero sections**: Edit files in `content/heroes/` to update page headers
- **News**: Add markdown files to `content/news/` for announcements
- **Projects**: Add project descriptions to `content/projects/`
- **Members**: Add member profiles to `content/members/`
- **Site config**: Edit `config/site.json` for site-wide settings

## Key Features

- Static site generation with Python and Jinja2
- Markdown content with frontmatter support
- Syntax highlighting for code blocks
- Responsive Bootstrap-based design
- Automatic image optimization
- Component-based template system

## Deployment

The website is automatically deployed via GitHub Actions when changes are pushed to the main branch. The generated site is served from GitHub Pages.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the build locally
5. Submit a pull request

## Support

For issues or questions, please open an issue on GitHub or contact the Boston Robot Hackers community.