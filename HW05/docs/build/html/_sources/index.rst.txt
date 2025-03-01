.. HomeWork05 documentation master file, created by
   sphinx-quickstart on Wed Feb 26 12:59:39 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HomeWork05 documentation: Model to predict Housing Prices
=========================================================

In this home work (HW) I am trying to put the former results into a docker environment and deliver the "first data product".


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   intro
   modules

How to use this project:
========================
The project can be run in docker. The only softare need is **Docker Desktoop**. (https://docs.docker.com/get-started/get-docker/)

Docker *train mode* (Dockerfile.train)
--------------------------------------
Dockerfile: 
FROM continuumio/miniconda3
WORKDIR /usr/src/app

COPY ../main.py .
COPY ../src ./src
COPY ../data ./data
COPY ../environments.yml .

RUN conda env create -f environments.yml 
RUN conda clean --all -y

ENV PATH /opt/conda/envs/arquitectura/bin:$PATH

ENTRYPOINT ["python", "main.py"]
CMD ["--input","data/prep", "--output", "data/inference/house_pricing_model.pkl" ]


to train the  model: 
 - docker build -t train_image -f Dockerfile.train .

Docker *inference mode* (Dockerfile.inference)
----------------------------------------------
Dockerfile:

FROM continuumio/miniconda3
WORKDIR /usr/src/app

COPY ../src/inference.py .
COPY ../src ./src
COPY ../data/inference ./data/inference
COPY ../environments.yml .

RUN conda env create -f environments.yml 
RUN conda clean --all -y

ENV PATH /opt/conda/envs/arquitectura/bin:$PATH

ENTRYPOINT ["python", "inference.py"]
CMD ["--input", "data/inference/house_pricing_model.pkl", "--output", "data/inference/results.csv" ]

to execute the model:
 - docker build -t train_image -f Dockerfile.inference .