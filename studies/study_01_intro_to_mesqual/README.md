# Study 01: Intro to MESQUAL
The intro study primarily uses a PyPSA example network to introduce the MESQUAL modules and framework. The series is structured as follows and will continuously be updated. So stay tuned.

### Getting Started Series
- [mesqual_101_study_manager_and_basic_fetching](notebooks/mesqual_101_study_manager_and_basic_fetching.ipynb) - Getting started with scenarios and comparisons [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_101_study_manager_and_basic_fetching.ipynb) 
- [mesqual_102_mastering_data_fetching](notebooks/mesqual_102_mastering_data_fetching.ipynb) - Mastering the fetch method and data access patterns [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_102_mastering_data_fetching.ipynb) 
- [mesqual_103_scenario_attributes](notebooks/mesqual_103_scenario_attributes.ipynb) - Managing and utilizing scenario metadata effectively [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_103_scenario_attributes.ipynb) 

### KPI Framework Series
- mesqual_201_kpi_framework_and_units - Building a structured KPI system with proper unit handling
- mesqual_202_kpi_collections_and_tables - Extracting pretty KPI tables

### Visualization Series
- [mesqual_301_time_series_dashboard](notebooks/mesqual_301_time_series_dashboard.ipynb) - The best way to visualize, compare and understand time-series [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_301_time_series_dashboard.ipynb) 
- [mesqual_302_segmented_colormap](notebooks/mesqual_302_segmented_colormap.ipynb) - A useful colormap to merge multiple linear segments into a single colormap [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_302_segmented_colormap.ipynb) 
- [mesqual_303_folium_model_df_map](notebooks/mesqual_303_folium_model_df_map.ipynb) - Creating interactive Folium maps visualizing model info [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_303_folium_model_df_map.ipynb) 
- [mesqual_304_folium_area_kpi_map](notebooks/mesqual_304_folium_area_kpi_map.ipynb) - Creating interactive Folium maps with area KPIs for scenarios and comparisons [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_304_folium_area_kpi_map.ipynb) 
- mesqual_305_area_border_kpi_map - Creating interactive Folium maps with area-border KPIs for scenarios and comparisons
- mesqual_306_icon_kpi_map - Creating interactive Folium maps with KPIs projected as icons for scenarios and comparisons
- [mesqual_307_country_plotter_util](notebooks/mesqual_307_country_plotter_util.ipynb) - GeoJSON library of country shapes [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_307_country_plotter_util.ipynb) 
- [mesqual_308_html_dashboards](notebooks/mesqual_308_html_dashboards.ipynb) - Multiple HTML plots (e.g. plotly figures) in one share-able html file [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helgeesch/mesqual-vanilla-studies/blob/main/studies/study_01_intro_to_mesqual/notebooks/mesqual_308_html_dashboards.ipynb)

### Advanced Dataset Handling Series
- mesqual_401_dataset_collections - Linking, merging and managing multiple data sources
- mesqual_402_custom_interpreters - Creating study-specific data interpreters and variables
- mesqual_403_model_timeseries_integration - Combining static model data with time series for richer analysis
- mesqual_404_dot_notation_api - Using Python's dot notation for elegant data access

### Expert Dataset Handling Series
- mesqual_501_configuration_hierarchy - Mastering dataset and fetch-level configurations
- mesqual_502_validation_framework - Ensuring data consistency across scenarios
- mesqual_503_pickle_database_integration - Intro to simple .pickle DB integration for faster fetching 

### Managing Multiple Studies Series
- mesqual_601_multi_study_architecture - Organizing repositories with multiple studies
- mesqual_602_color_themes - Managing different color themes across different studies

### Interface Builder Series
- mesqual_701_platform_dataset - An abstract container class for data interpreters to cover all aspects of handling data from a platform
- mesqual_702_flag_index_system - Understanding relationships between model and time series data
- mesqual_703_model_enrichment_patterns - Advanced techniques for property and membership enrichment
- mesqual_704_variable_aggregation_patterns - Advanced techniques for automatic variable aggregations

### Advanced DataFrame Handling Series
- mesqual_801_granularity_analysis_and_conversion - Handling time-series of different granularities
- mesqual_802_multi_index_utils - xs_df, set_new_column, sort_multi_index

## References and Third-Party Assets
- PyPSA and Scigrid-DE example network: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14824654.svg)](https://doi.org/10.5281/zenodo.14824654) - [MIT License]
- GeoJSON of DE control areas: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7530196.svg)](https://doi.org/10.5281/zenodo.7530196) - [CC BY 4.0]
