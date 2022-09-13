# Facilitated Machine Learning with images using pre-trained Vision Transformers

This Tutorial is part of the 2022 Summer School "[Application of Machine Learning in Plant Sciences](https://www.plantsciences.uzh.ch/en/teaching/summerschool.html)" organised by the Zurich-Based Plant Science Center.

## Abstract

This hands-on programming session will be about Vision Transformers pre-trained with the DINO method. We will use these models to convert images to lower-dimensional representations that enable the usage of shallow machine learning models for downstream tasks such as classification or clustering. This procedure can be superior to other approaches when the number of available training samples is small or when no GPUs for training Deep Neural Networks are available. We will demonstrate the method by classifying fruit quality based on public image data sets. Participants are welcome to experiment with their own data sets during the session. We will work with Python/Jupyter, PyTorch, and scikit-learn.

## Setup

This project should work with all newer Python versions(>=3.7). It was tested with version `3.8.9`.

If you want to run the notebooks in your local environment, make sure to install the required libraries: `pip install -r requirements.txt`
Google Colab should already have all dependencies installed.

## Data

This project requires a data folder (containing a small image data set and other precalculated files).
Please download the folder from here and place it in your project (root): https://drive.google.com/drive/folders/1id2pRwUE7lA0H_7XZgm2aNnQ9N89JbBw?usp=sharing

## Table of Content / Schedule

- General Introduction (15min)
- Part 1: Data Preparation
  - Introduction (10min)
  - Exercise / Programming (15min)
- Part 2: Dimensionality Reduction / Visualisation
  - Introduction (10min)
  - Exercise / Programming (15min)
- Part 3: Classification
  - Introduction (10min)
  - Exercise / Programming (15min)
  