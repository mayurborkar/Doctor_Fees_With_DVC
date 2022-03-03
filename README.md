# DVC-Template
It is general file structure that can be used for DVC implementation.

## STEPS -

### STEP 01- Create a repository by using template repository

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

### STEP 06- Commit and push the changes to the remote repository