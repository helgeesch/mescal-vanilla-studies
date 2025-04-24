import logging
import warnings
import pandas as pd


def configure_clean_output_for_jupyter_notebook():
    logging.basicConfig(level=logging.ERROR)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    pd.set_option('display.max_columns', 6)
    pd.set_option('display.width', 1000)
