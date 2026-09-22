project = "Awesome Django Modern REST"
copyright = "2026, Awesome Django Modern REST contributors"

extensions = ["myst_parser"]
source_suffix = {
    ".md": "markdown",
}
exclude_patterns = ["_build"]

html_theme = "shibuya"
html_title = "Awesome Django Modern REST"
html_theme_options = {
    "github_url": "https://github.com/kondratevdev/awesome-django-modern-rest",
    "readthedocs_url": "https://awesome-django-modern-rest.readthedocs.io",
    "accent_color": "green",
    "light_logo": "logo-dark.svg",
    "dark_logo": "logo-light.svg",
}
html_context = {
    "source_type": "github",
    "source_user": "kondratevdev",
    "source_repo": "awesome-django-modern-rest",
    "source_version": "master",
}
html_static_path = ["../assets", "_static"]
html_css_files = ["css/catalog.css"]
html_show_sourcelink = False
