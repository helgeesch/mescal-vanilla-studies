import os
import pypsa

from mescal import StudyManager
from mescal_pypsa import PyPSADataset

from studies.study_01_intro_to_mescal.src.study_specific_model_interpreters import ControlAreaModelInterpreter, ScigridDEBusModelInterpreter

PyPSADataset.register_interpreter(ControlAreaModelInterpreter)
PyPSADataset.register_interpreter(ScigridDEBusModelInterpreter)


def get_scigrid_de_study_manager() -> StudyManager:
    study_folder = 'studies/study_01_intro_to_mescal'
    networks_folder = os.path.join(study_folder, 'data/networks_scigrid_de')

    n_base = pypsa.Network(os.path.join(networks_folder, 'base.nc'))
    n_solar_150 = pypsa.Network(os.path.join(networks_folder, 'solar_150.nc'))
    n_solar_200 = pypsa.Network(os.path.join(networks_folder, 'solar_200.nc'))
    n_wind_150 = pypsa.Network(os.path.join(networks_folder, 'wind_150.nc'))
    n_wind_200 = pypsa.Network(os.path.join(networks_folder, 'wind_200.nc'))

    study_manager = StudyManager.factory_from_scenarios(
        scenarios=[
            PyPSADataset(n_base,        name='base'),
            PyPSADataset(n_solar_150,   name='solar_150'),
            PyPSADataset(n_solar_200,   name='solar_200'),
            PyPSADataset(n_wind_150,    name='wind_150'),
            PyPSADataset(n_wind_200,    name='wind_200'),
        ],
        comparisons=[('solar_150', 'base'), ('solar_200', 'base'), ('wind_150', 'base'), ('wind_200', 'base')],
        export_folder=os.path.join(study_folder, 'non_versioned/output'),
    )
    return study_manager


if __name__ == '__main__':
    study = get_scigrid_de_study_manager()
