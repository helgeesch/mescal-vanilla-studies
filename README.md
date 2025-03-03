[![Python >=3.10](https://img.shields.io/badge/python-≥3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# MESCAL vanilla studies

## Overview

**MESCAL** (Modular Energy Scenario Comparison Analysis and Library) is a Python framework for post-processing and analyzing energy systems data, with a focus on scenario comparison, KPI calculation, and plotly / folium (map) visualizations. This vanilla studies repository demonstrates MESCAL's capabilities through practical examples and serves as a template architecture for organizing energy modeling studies.

**Value proposition:**
- Unified analysis interface for any energy modeling platform, real market data, or custom data sources (e.g. PyPSA, Plexos, Entso-e TP, ...)
- Consistent handling of scenarios and scenario comparisons
- Integrated tools for model data and time series analysis
- Modular design that allows seamless integration of study-specific code

---

## Example Studies

Here is a list of all studies and examples currently part of the mescal-vanilla-studies repo.

### Study 01: Intro to MESCAL ([link](studies/study_01_intro_to_mescal))
The intro study primarily uses a PyPSA example network to introduce the MESCAL modules and framework. Click on the title of the study to see the full overview.

### Study 02 Plexos Example ([link](studies/study_02_plexos_example))
This study demonstrates how to use MESCAL with Plexos simulation outputs, showing the platform-agnostic nature of the framework. It includes examples of loading PLEXOS data, performing common analyses, and visualizing results using the same patterns established in Study 01.

---

## Repository Structure as Framework Template

Beyond providing examples, this repository serves as a template architecture for organizing energy modeling studies. The structure enables:

- Clear separation between generic and study-specific code/data
- Clear separation between shared (version-controlled) and private (local) code/data
- Quick switching between studies, as many analysts need in their daily work
- Reuse of modules across studies
- Low entry barrier to get started, while enabling incremental and modular development
- more about this in 

---

## Getting Started: Setting up the repo locally

### Prerequisites
- Python ≥ 3.10
- Git 
- It is recommend to set up a virtual environment for this repository, but this is, of course, optional.

### Step 1: Clone mescal-vanilla-studies
In your console, navigate to the directory in which you want to clone this repo. Then perform the clone:
```bash
git clone https://github.com/helgeesch/mescal-vanilla-studies.git
```

### Step 2: Add submodules
```bash
cd mescal-vanilla-studies
git submodule update --init
```
The folder `submodules/` should now include the respective packages.

### Step 3: Configure submodules as source root
#### PyCharm Configuration
If you're using PyCharm, ensure that the submodule directories are properly recognized as part of the source code by setting them as "Sources Root":

1. In PyCharm's Project Explorer, locate the submodule directories:
   - `submodules/mescal`
   - `submodules/mescal-pypsa`
2. Right-click on each of the directories above.
3. Select Mark Directory as -> Sources Root.


#### VSCode Configuration
In Visual Studio Code, you can add the submodules to the python.analysis.extraPaths setting:
1. Open your project folder.
2. Create (or modify) .vscode/settings.json:
    ```json
    {
        "python.analysis.extraPaths": [
          "submodules/mescal",
          "submodules/mescal-pypsa"
        ]
    }
    ```

#### Jupyter Notebook Configuration
If you work with Jupyter, extend the sys.path directly in your notebook:
```python
import sys
sys.path.append("submodules/mescal")
sys.path.append("submodules/mescal-pypsa")
```

### Step 4: Install requirements
```bash
pip install -r requirements.txt
pip install -r submodules/mescal/requirements.txt
pip install -r submodules/mescal-pypsa/requirements.txt
```

---

## Creating a New Study

The vanilla repo comes with a generic folder structure template for new studies. You can check out the folder structure in [study_structure.py](vanilla/study_structure.py).

The fastest way to set up a new study from the template layout is to simply run:
```bash
python -m vanilla.new_study studies/study_123_your_name
```
This will create a new folder with the template structure in the studies directory.

If you follow this structure, you can make use of the PathManager class for easy navigation between study-specific paths.

---

## Attribution and Licenses

This project is primarily licensed under the LGPL License - see the LICENSE file for details.

### Third-party assets:
- PyPSA and Scigrid-DE example network: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14824654.svg)](https://doi.org/10.5281/zenodo.14824654) - [MIT License]
- GeoJSON of DE control areas: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7530196.svg)](https://doi.org/10.5281/zenodo.7530196) - [CC BY 4.0]

The example notebooks use these assets for demonstration purposes.

---

## Contributing

Contributions to improve examples or add new ones are welcome! Please feel free to submit a pull request or open an issue to discuss potential enhancements.

---

## Contact

For questions or feedback about MESCAL or these example studies, don't hesitate to get in touch!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/helge-e-8201041a7/)
