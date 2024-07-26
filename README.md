# California Housing Model

## Overview
This machine learning model webapp was created from the preloaded sklearn california housing dataset to test out webapps using streamlit.
In these files we train and fine tune the model and preform data preprocessing to create a stacking regressor out of mulitple regresison models such as xgboost, random forest, support vector machine, and normal gradient boosted regressors.

These are then written out to create a webapp hosted and created by streamlit where users can provide inputs to see what the predicted home price would be.

## Contents
- [Overview](#overview)
- [Directory Structure](#directory-structure)
  - [docs](#docs)
  - [models](#models)
  - [text](#text)
  - [utils](#utils)
  - [app.py](#app.py)
  - [requirements.txt](#requirementstxt)
  - [train.ipynb](#trainipynb)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Directory Structure
The project is organized as follows:

### Docs
This folder contains readme images and other images that can be found on the webapp.

### Models
Folder containing the models used during inference when users provide feature inputs.

### Text
Text files that are used in creating summaries and other information in the webapp.

### Utils
Uitlity functions to process and scale the data before inference.

### App.py
Main python file that runs to create the webapp and load the model.

### Requirements.txt 
Requirements file for repodiciblity with the used libaries such as sklearn, xgboost, streamlit, etc

### Train.ipynb
Jupyter notebook where the model is trained.

## Installation

To install the needed libraries run the line below:

    pip install -r requirements.txt

## Usage

To run this webapp locally do the following command when in the project directory:

    streamlit run app.py


