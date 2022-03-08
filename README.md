# Doctor Fees Prediction Using DVC
It is general file structure that can be used for DVC implementation.

## STEPS -

### STEP 01- Create a repository by using template repository or you can create the folder by using template.py

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE & activate the env
```bash
conda create --prefix ./env python=3.7 -y
```
AND
```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05- Initialize the dvc project
```bash
dvc init
```

### Step 06- To add the data in dvc project
```bash
dvc add <data_path_with_extension>
```

### STEP 07- To run python file or dvc stage
```bash
python src/<file_name_with_extension>
```
OR
```bash
dvc repro
```

### Step 08- Commit The Code In Repository & Check The Ci-Cd pipeline


### Step 09- To run the setup.py File
```bash
pip install -e .
```

### Step 10- To run tox file
```bash
tox
```

### Step 11- To run tox file after updating requirements.txt file
```bash
tox -r
```

### Step 12- To create the package of your src file 
```bash
python setup.py sdist bdist_wheel
```