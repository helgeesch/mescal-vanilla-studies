import os
import pytest
import nbformat
from nbclient import NotebookClient
from pathlib import Path


def find_notebooks(base_dir=None, pattern=None):
    """Find notebooks matching optional pattern"""
    if base_dir is None:
        base_dir = Path(__file__).parent.parent

    notebooks = []
    studies_dir = Path(base_dir) / "studies"

    for study_dir in studies_dir.glob("study_*"):
        notebook_dir = study_dir / "notebooks"
        if notebook_dir.exists():
            if pattern:
                notebooks.extend(list(notebook_dir.glob(f"*{pattern}*.ipynb")))
            else:
                notebooks.extend(list(notebook_dir.glob("*.ipynb")))

    notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in str(nb)]
    return notebooks


@pytest.mark.parametrize("notebook_path", find_notebooks())
def test_notebook_runs_without_errors(notebook_path):
    """Test that notebook runs without errors"""
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        **({"async_": False} if "async_" in NotebookClient.__init__.__code__.co_varnames else {}),
        resources={"metadata": {"path": notebook_path.parent}}
    )

    try:
        client.execute()
    except Exception as e:
        pytest.fail(f"Error executing {notebook_path.name}: {str(e)}")
