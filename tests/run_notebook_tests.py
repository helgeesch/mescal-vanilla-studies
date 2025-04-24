import sys
import subprocess
from pathlib import Path


def test_notebooks(pattern: str = None, verbose: bool = True):
    """Run notebook tests with optional pattern filter"""
    cmd = ["pytest", "tests/test_notebooks.py"]

    if pattern:
        temp_test_file = Path("tests/temp_test_notebooks.py")

        with open("tests/test_notebooks.py") as f:
            content = f.read()

        modified = content.replace(
            "find_notebooks()",
            f"find_notebooks(pattern='{pattern}')"
        )

        with open(temp_test_file, "w") as f:
            f.write(modified)

        cmd = ["pytest", str(temp_test_file)]

    if verbose:
        cmd.append("-v")

    result = subprocess.run(cmd)

    if pattern and temp_test_file.exists():
        temp_test_file.unlink()

    return result.returncode


if __name__ == "__main__":
    pattern = None
    if len(sys.argv) > 1:
        pattern = sys.argv[1]

    print(f"Testing notebooks{f' matching pattern: {pattern}' if pattern else ''}...")
    sys.exit(test_notebooks(pattern=pattern))
