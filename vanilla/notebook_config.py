def configure_clean_output_for_jupyter_notebook():
    """
    This function suppresses common warnings, configures logging to only show
    errors, and sets pandas display options for cleaner notebook output.
    """
    import logging
    import warnings
    import pandas as pd
    import numpy as np

    # Configure logging to show only errors
    logging.basicConfig(level=logging.ERROR)

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=UserWarning)
    warnings.filterwarnings("ignore", category=RuntimeWarning)

    warnings.filterwarnings("ignore", module="matplotlib")
    warnings.filterwarnings("ignore", module="plotly")
    warnings.filterwarnings("ignore", module="ipykernel")
    warnings.filterwarnings("ignore", module="ipywidgets")
    warnings.filterwarnings("ignore", module="pandas")
    warnings.filterwarnings("ignore", module="geopandas")

    pd.set_option('display.max_columns', 6)
    pd.set_option('display.width', 1000)
    pd.set_option('display.precision', 2)

    np.seterr(all='ignore')


def ensure_repo_root_is_in_path():
    """
    Locate repository root, set working directory, and update Python path.

    This function is designed to be used at the top of notebooks to standardize
    path management across the MESCAL project. It:

    1. Finds the repository root by searching upward for .git or submodules directory
    2. Changes the working directory to the repository root
    3. Adds the repository root to Python's import path if not already present

    After running this function, imports will work consistently regardless of
    where in the repository structure the notebook is located.
    """
    import os
    import sys
    from pathlib import Path

    def find_repo_root():
        current = Path(os.getcwd()).absolute()
        while current != current.parent:
            if (current / '.git').exists() or (current / 'submodules').exists():
                return current
            current = current.parent
        raise FileNotFoundError(f"Could not find repository root starting from {os.getcwd()}.")

    repo_root = find_repo_root()
    os.chdir(repo_root)

    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))


def add_submodules_to_path():
    """Add all required MESCAL submodules to the Python path."""
    import os
    import sys
    from pathlib import Path

    repo_root = Path(os.getcwd()).absolute()
    submodules_dir = repo_root / "submodules"

    if not submodules_dir.exists():
        current_dir = os.getcwd()
        raise FileNotFoundError(
            f"\nSubmodules directory not found at {submodules_dir}\n"
            f"Current working directory: {current_dir}\n\n"
            f"Possible issues:\n"
            f"1. Git submodules not initialized. Run: git submodule update --init\n"
            f"2. Working directory incorrect. Make sure the working directory is set to the mescal-vanilla-studies folder"
        )

    submodule_paths = [
        "mescal",
        "mescal-pypsa",
        # Add future submodules here
    ]

    added = []
    missing = []

    for submodule in submodule_paths:
        path = submodules_dir / submodule
        if path.exists():
            if str(path) not in sys.path:
                sys.path.insert(0, str(path))
                added.append(submodule)
        else:
            missing.append(submodule)

    if missing:
        current_dir = os.getcwd()
        print(
            f"\nWarning: The following submodules were not found: {', '.join(missing)}\n"
            f"Current working directory: {current_dir}\n\n"
            f"Possible issues:\n"
            f"1. Git submodules not initialized. Run: git submodule update --init\n"
            f"2. Working directory incorrect. Make sure the working directory is set to the mescal-vanilla-studies folder"
        )
