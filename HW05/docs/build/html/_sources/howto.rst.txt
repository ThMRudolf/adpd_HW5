Installation and how to use this project:
==========================================

1. Clone Repository

.. code-block:: console

    $ git clone https://github.com/ThMRudolf/adpd_HW5.git

2. Launch Application via Docker: Docker *train mode* (Dockerfile.train)

.. code-block:: console

   $ FROM continuumio/miniconda3
   $ WORKDIR /usr/src/app
   $
   $ COPY ../main.py .
   $ COPY ../src ./src
   $ COPY ../data ./data
   $ COPY ../environments.yml .
   $
   $ RUN conda env create -f environments.yml 
   $ RUN conda clean --all -y
   $
   $ ENV PATH /opt/conda/envs/arquitectura/bin:$PATH
   $
   $ ENTRYPOINT ["python", "main.py"]
   $ CMD ["--input","data/prep", "--output", "data/inference/house_pricing_model.pkl" ]
 
to train the  model:

.. code-block:: console

   $ docker build -t train_image -f Dockerfile.train .


3. Validate Application Docker *inference mode* (Dockerfile.inference)

.. code-block:: console

   $ FROM continuumio/miniconda3
   $ WORKDIR /usr/src/app
   $
   $ COPY ../src/inference.py .
   $ COPY ../src ./src
   $ COPY ../data/inference ./data/inference
   $ COPY ../environments.yml .
   $
   $ RUN conda env create -f environments.yml 
   $ RUN conda clean --all -y
   $
   $ ENV PATH /opt/conda/envs/arquitectura/bin:$PATH
   $
   $ ENTRYPOINT ["python", "inference.py"]
   $ CMD ["--input", "data/inference/house_pricing_model.pkl", "--output", "data/inference/results.csv" ]

to execute the model:

.. code-block:: console
   
   $ docker build -t train_image -f Dockerfile.inference .