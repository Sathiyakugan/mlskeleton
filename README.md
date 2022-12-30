# mlskeleton

A Python package that generates a folder structure for machine learning/deep learning projects.

## Installation

To install the package, run the following command:
```bash
pip install mlskeleton
```

## Usage

To generate the folder structure, run the following command:
```bash
mlskeleton /path/to/root/folder
```

This will create the following folder structure at the specified root folder path:


```bash
project_name/
|
|- data/
|   |- raw/
|   |   |- raw_data_file_1.csv
|   |   |- raw_data_file_2.csv
|   |   ...
|   |
|   |- processed/
|   |   |- processed_data_file_1.csv
|   |   |- processed_data_file_2.csv
|   |   ...
|
|- models/
|   |- model_1.pkl
|   |- model_2.pkl
|   ...
|
|- notebooks/
|   |- data_exploration.ipynb
|   |- model_training.ipynb
|   |- model_evaluation.ipynb
|   ...
|
|- src/
|   |- data/
|   |   |- data_processing.py
|   |   |- data_cleaning.py
|   |   ...
|   |
|   |- features/
|   |   |- feature_extraction.py
|   |   |- feature_selection.py
|   |   ...
|   |
|   |- models/
|   |   |- model_training.py
|   |   |- model_evaluation.py
|   |   ...
|   |
|   |- visualization/
|   |   |- visualizations.py
|   |   ...
|   |
|   |- utils/
|   |   |- utils.py
|   |   ...
|
|   |- tests/
|   |   |- test_data.py
|   |   |- test_features.py
|   |   |- test_visualization.py
|   |   |- test_models.py
|   |   |- test_utils.py
|   |   ...
|
|-- reports/
|   |-- figures/
|   |-- presentations/
|   |-- papers/
|
|- .gitignore
|- requirements.txt
|- README.md
```
Explanation:

- **`data`**: This folder should contain all the data required for the project, both raw and processed. It is a good idea to keep the raw data separate from the processed data to make it clear which data has been transformed in some way and how.
- **`models`**: This folder should contain the trained machine learning models, saved in a format that allows them to be easily loaded and used (e.g. using the **`pickle`** library in Python).
- **`notebooks`**: This folder should contain Jupyter notebooks used for data exploration, model training, model evaluation, and any other analysis.
- **`src`**: This folder should contain the source code for the project, organized into subfolders for data processing,features, model training and evaluation, visualization, etc.
  - **`src/data/`**: This folder should contain code for loading and interacting with the data.
  - **`src/features/`**: This folder should contain code for generating features from the data.
  - **`src/models/`**: This folder should contain code for building and training machine learning models.
  - **`src/visualization/`**: This folder should contain code for creating visualizations of the data and model performance.
  - **`src/utils/`**: This folder should contain utility code that is used by other parts of the project.
  - **`tests/`**: This folder should contain test scripts or modules for testing the code in the **`src/`** directory.
- **`reports/`**: This folder should contain any figures, presentations, or papers that are created as part of the project.
- **`.gitignore`**: This file should contain a list of file and folder names that should be ignored by Git (e.g. large data files that should not be committed to the repository).
- **`requirements.txt`**: This file should contain a list of the libraries and packages required to run the code in the project, so that they can be easily installed by someone else who wants to run the code.
- **`README.md`**: This file should contain a brief description of the project and instructions for how to set up and run the code.

## Contributing
If you want to contribute to the package, please follow the guidelines in the `CONTRIBUTING.md` file.

## License

The package is licensed under the MIT License. See the `LICENSE` file for more information.
