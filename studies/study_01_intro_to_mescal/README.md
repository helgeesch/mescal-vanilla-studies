# Study 01: Intro to MESCAL
The intro study primarily uses a PyPSA example network to introduce the MESCAL modules and framework. The series is structured as follows and will continuously be updated. So stay tuned.

### Getting Started Series
- [mescal_101_study_manager_and_basic_fetching](notebooks/mescal_101_study_manager_and_basic_fetching.ipynb) - Getting started with scenarios and comparisons [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_101_study_manager_and_basic_fetching.ipynb) 
- [mescal_102_mastering_data_fetching](notebooks/mescal_102_mastering_data_fetching.ipynb) - Mastering the fetch method and data access patterns [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_102_mastering_data_fetching.ipynb) 
- [mescal_103_scenario_attributes](notebooks/mescal_103_scenario_attributes.ipynb) - Managing and utilizing scenario metadata effectively [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_103_scenario_attributes.ipynb) 

### KPI Framework Series
- mescal_201_kpi_framework_and_units - Building a structured KPI system with proper unit handling
- mescal_202_kpi_collections_and_tables - Extracting pretty KPI tables

### Visualization Series
- [mescal_301_time_series_dashboard](notebooks/mescal_301_time_series_dashboard.ipynb) - The best way to visualize, compare and understand time-series [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_301_time_series_dashboard.ipynb) 
- [mescal_302_segmented_colormap](notebooks/mescal_302_segmented_colormap.ipynb) - A useful colormap to merge multiple linear segments into a single colormap [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_302_segmented_colormap.ipynb) 
- [mescal_303_folium_model_df_map](notebooks/mescal_303_folium_model_df_map.ipynb) - Creating interactive Folium maps visualizing model info [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_303_folium_model_df_map.ipynb) 
- [mescal_304_folium_area_kpi_map](notebooks/mescal_304_folium_area_kpi_map.ipynb) - Creating interactive Folium maps with area KPIs for scenarios and comparisons [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_304_folium_area_kpi_map.ipynb) 
- mescal_305_area_border_kpi_map - Creating interactive Folium maps with area-border KPIs for scenarios and comparisons
- mescal_306_icon_kpi_map - Creating interactive Folium maps with KPIs projected as icons for scenarios and comparisons
- [mescal_307_country_plotter_util](notebooks/mescal_307_country_plotter_util.ipynb) - GeoJSON library of country shapes [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_307_country_plotter_util.ipynb) 
- [mescal_308_html_dashboards](notebooks/mescal_308_html_dashboards.ipynb) - Multiple HTML plots (e.g. plotly figures) in one share-able html file [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mescal-vanilla-studies/blob/main/studies/study_01_intro_to_mescal/notebooks/mescal_308_html_dashboards.ipynb)

### Advanced Dataset Handling Series
- mescal_401_dataset_collections - Linking, merging and managing multiple data sources
- mescal_402_custom_interpreters - Creating study-specific data interpreters and variables
- mescal_403_model_timeseries_integration - Combining static model data with time series for richer analysis
- mescal_404_dot_notation_api - Using Python's dot notation for elegant data access

### Expert Dataset Handling Series
- mescal_501_configuration_hierarchy - Mastering dataset and fetch-level configurations
- mescal_502_validation_framework - Ensuring data consistency across scenarios
- mescal_503_pickle_database_integration - Intro to simple .pickle DB integration for faster fetching 

### Managing Multiple Studies Series
- mescal_601_multi_study_architecture - Organizing repositories with multiple studies
- mescal_602_color_themes - Managing different color themes across different studies

### Interface Builder Series
- mescal_701_platform_dataset - An abstract container class for data interpreters to cover all aspects of handling data from a platform
- mescal_702_flag_index_system - Understanding relationships between model and time series data
- mescal_703_model_enrichment_patterns - Advanced techniques for property and membership enrichment
- mescal_704_variable_aggregation_patterns - Advanced techniques for automatic variable aggregations

### Advanced DataFrame Handling Series
- mescal_801_granularity_analysis_and_conversion - Handling time-series of different granularities
- mescal_802_multi_index_utils - xs_df, set_new_column, sort_multi_index

## References and Third-Party Assets
- PyPSA and Scigrid-DE example network: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14824654.svg)](https://doi.org/10.5281/zenodo.14824654) - [MIT License]
- GeoJSON of DE control areas: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7530196.svg)](https://doi.org/10.5281/zenodo.7530196) - [CC BY 4.0]
