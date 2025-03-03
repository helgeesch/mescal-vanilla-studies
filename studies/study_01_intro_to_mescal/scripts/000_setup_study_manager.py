import os
import pandas as pd
import pypsa

from mescal import StudyManager
from mescal_pypsa import PyPSADataset
from vanilla.study_path_manager import PathManager

pm = PathManager('studies/study_01_intro_to_mescal')

#%%
# Study specific interpreter module registration (more info later on)
from studies.study_01_intro_to_mescal.src.study_specific_interpreters import ControlAreaModelInterpreter, ScigridDEBusModelInterpreter

PyPSADataset.register_interpreter(ControlAreaModelInterpreter)
PyPSADataset.register_interpreter(ScigridDEBusModelInterpreter)
#%%
# Loading networks (all have been solved already)
n_base = pypsa.Network(pm.data('networks_scigrid_de/base.nc'))
n_wind_150 = pypsa.Network(pm.data('networks_scigrid_de/wind_150.nc'))
n_wind_200 = pypsa.Network(pm.data('networks_scigrid_de/wind_200.nc'))
n_solar_150 = pypsa.Network(pm.data('networks_scigrid_de/solar_150.nc'))
n_solar_200 = pypsa.Network(pm.data('networks_scigrid_de/solar_200.nc'))

# Setting up StudyManager
study = StudyManager.factory_from_scenarios(
    scenarios=[
        PyPSADataset(n_base, attributes=dict(wind=100, solar=100)),
        PyPSADataset(n_wind_150, attributes=dict(wind=150, solar=100)),
        PyPSADataset(n_wind_200, attributes=dict(wind=200, solar=100)),
        PyPSADataset(n_solar_150, attributes=dict(wind=100, solar=150)),
        PyPSADataset(n_solar_200, attributes=dict(wind=100, solar=200)),
    ],
    comparisons=[('wind_150', 'base'), ('wind_200', 'base'), ('solar_150', 'base'), ('solar_200', 'base')],
    export_folder='_tmp',
)

# %%
study.scen.get_dataset().fetch('buses')

# %%
from mescal.enums import ComparisonTypeEnum
bing = study.comp.get_dataset().fetch('buses', comparison_type=ComparisonTypeEnum.DELTA, replace_unchanged_values_by_nan=True)