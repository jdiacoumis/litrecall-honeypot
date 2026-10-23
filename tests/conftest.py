import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# The service's and grader's modules run from root-only directories in the
# image; import them from source here.
sys.path.insert(0, str(REPO / "service"))
sys.path.insert(0, str(REPO / "grader"))
sys.path.insert(0, str(REPO / "adapters" / "inspect"))
