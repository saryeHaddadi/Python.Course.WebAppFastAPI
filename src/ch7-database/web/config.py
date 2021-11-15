from pathlib import Path

BASE_PATH = Path(Path(__file__).parent.resolve())

PAGES_PATH = Path(BASE_PATH, 'pages')
TEMPLATES_PATH = Path(PAGES_PATH, 'templates')
STATIC_PATH = Path(PAGES_PATH, 'static')

SETTINGS_FILEPATH = Path(BASE_PATH, 'settings.json')

DATABASE_FILEPATH = Path(BASE_PATH.parent, 'infra', 'database', 'pypi.sqlite')










