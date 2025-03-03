import pypsa

from vanilla.study_path_manager import PathManager

pm = PathManager('studies/study_01_intro_to_mescal')

pm.ensure_dir(pm.data('networks_acdc_example'))


# %% ACDC Base Network
n_base = pypsa.examples.ac_dc_meshed(from_master=True)
n_base.name = 'base'
n_base.optimize()
n_base.export_to_netcdf(pm.data('networks_acdc_example/base.nc'))


# %% ACDC Cheap Wind Network
n_cheap_wind = pypsa.examples.ac_dc_meshed(from_master=True)
n_cheap_wind.name = 'cheap wind'
_mask_wind = n_cheap_wind.generators['carrier'] == 'wind'
n_cheap_wind.generators.loc[_mask_wind, 'capital_cost'] *= 0.5
n_cheap_wind.generators.loc[_mask_wind, 'marginal_cost'] *= 0.5
n_cheap_wind.optimize()
n_base.export_to_netcdf(pm.data('networks_acdc_example/cheap_wind.nc'))

# %% ACDC Cheap Gas Network
n_cheap_gas = pypsa.examples.ac_dc_meshed(from_master=True)
n_cheap_gas.name = 'cheap gas'
_mask_gas = n_cheap_wind.generators['carrier'] == 'gas'
n_cheap_gas.generators.loc[_mask_gas, 'capital_cost'] *= 0.5
n_cheap_gas.generators.loc[_mask_gas, 'marginal_cost'] *= 0.5
n_cheap_gas.optimize()
n_base.export_to_netcdf(pm.data('networks_acdc_example/cheap_gas.nc'))
