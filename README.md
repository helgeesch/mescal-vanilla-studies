[![Python >=3.10](https://img.shields.io/badge/python-≥3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# MESQUAL vanilla studies <img src="https://raw.githubusercontent.com/helgeesch/mesqual/refs/heads/main/assets/logo_no_text_no_bg.svg" width="70" height="70" alt="logo">

## Overview

**MESQUAL** (Modular Energy Scenario Comparison Analysis Library) is a Python framework for post-processing and analyzing energy systems data from any platform, with a focus on multi-scenario processing, scenario comparison, KPI calculation, and plotly / folium (map) visualizations.  

This vanilla studies repository demonstrates MESQUAL's capabilities through practical examples and serves as a template architecture for organizing energy modeling studies. 

The repo integrates the foundation package [mesqual](https://github.com/helgeesch/mesqual), and the interface packages [mesqual-pypsa](https://github.com/helgeesch/mesqual-pypsa), [mesqual-plexos](https://github.com/helgeesch/mesqual-plexos) (to be released) as submodules. 

Visit the foundation package's README to find out more about the the [MESQUAL value proposition](https://github.com/helgeesch/mesqual) or dive into the hands-on example studies in this repo to see MESQUAL in action.

---

## Example Studies

Here is a list of all studies and examples currently part of the mesqual-vanilla-studies repo.

### Study 01: Intro to MESQUAL ([link](studies/study_01_intro_to_mesqual))
The intro study primarily uses a PyPSA example network to introduce the MESQUAL modules and framework. Click on the title of the study to see the full overview.

### Study 02: Plexos Example ([link](studies/study_02_plexos_example))
This study demonstrates how to use MESQUAL with Plexos simulation outputs, showing the platform-agnostic nature of the framework. 
It includes examples of loading PLEXOS data, performing common analyses, and visualizing results using the same patterns established in Study 01.

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

### Step 1: Clone mesqual-vanilla-studies
In your console, navigate to the directory in which you want to clone this repo. Then perform the clone:
```bash
git clone https://github.com/helgeesch/mesqual-vanilla-studies.git
cd mesqual-vanilla-studies
```

### Step 2: Install sister packages or add them as submodules
### Option A: Install submodules from Git with pip (easy for consumers)
```bash
pip install git+https://github.com/helgeesch/mesqual.git
pip install git+https://github.com/helgeesch/mesqual-pypsa.git
```

### Option B: Local dev with submodules (for active development)
#### B.1: Add submodules under your repo:
Make sure your console is in the mesqual-vanilla-studies folder and then initialize all submodules with
```bash
git submodule update --init
```
The folder `submodules/` should now include the respective packages.

#### B.2: Install in editable mode so that any code changes “just work”:
```bash
pip install -e ./submodules/mesqual
pip install -e ./submodules/mesqual-pypsa
```

#### B.3 (optional): IDE tip
If you want full autocomplete and go-to-definition in PyCharm/VS Code, mark submodules/mesqual (and any other submodule) as a Sources Root in your IDE. This is purely for dev comfort and won’t affect other users.

### Step 4: Install requirements
```bash
pip install -r requirements.txt
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

For questions or feedback about MESQUAL or these example studies, don't hesitate to get in touch!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/helge-e-8201041a7/)
