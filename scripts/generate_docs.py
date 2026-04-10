"""Generate README.md with API docs from wigglystuff's ApiDoc.to_markdown()."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from wigglystuff import ApiDoc
from hastyplot.qplot import qplot

MARKER_START = "<!-- API_DOCS_START -->"
MARKER_END = "<!-- API_DOCS_END -->"

readme_path = Path(__file__).resolve().parent.parent / "README.md"
readme = readme_path.read_text()

api_md = ApiDoc(qplot).to_markdown()

start = readme.index(MARKER_START) + len(MARKER_START)
end = readme.index(MARKER_END)
readme = readme[:start] + "\n" + api_md + "\n" + readme[end:]

readme_path.write_text(readme)
print("README.md updated with API docs.")
