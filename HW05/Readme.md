# "Forcast of house prizing"
## author: Thomas M. Rudolf

The product is not ready not. I could not import the module
**predict_house_prices.py** with the mayority of functions.

*Título de tu proyecto:* Forcast of house prizing 

*Explicar qué hace:*
The product takes information about a house (number of rooms, number o
bath rooms, car space, garden, location, etc) and estimates the value.

*Dependencias:* The product needs several python libraries: pandas and
sklearn. 

*Inputs/Outputs:* Inputs (categorical): The categorical inputs
can be found in data/categorical_cols_train.txt and the numerical imputs
in data/numerical_cols_train.txt

*Estructura del repo:*

``` plaintext
.
├── Dockerfile.inference
├── Dockerfile.train
├── LICENSE
├── Makefile
├── Readme.md
├── copilot_recomandacions.docx
├── data
│   ├── data_description.txt
│   ├── inference
│   │   └── house_price_model.pkl
│   ├── prep
│   │   ├── categorical_cols_train.txt
│   │   ├── numerical_cols_train.txt
│   │   ├── x_train.csv
│   │   ├── x_valid.csv
│   │   ├── y_train.csv
│   │   └── y_valid.csv
│   └── raw
│       ├── sample_submission.csv
│       ├── test.csv
│       └── train.csv
├── docs
│   ├── Makefile
│   ├── build
│   │   ├── doctrees
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   ├── intro.doctree
│   │   │   ├── modules.doctree
│   │   │   ├── prep.doctree
│   │   │   └── train.doctree
│   │   └── html
│   │       ├── _sources
│   │       │   ├── index.rst.txt
│   │       │   ├── intro.rst.txt
│   │       │   ├── modules.rst.txt
│   │       │   ├── prep.rst.txt
│   │       │   └── train.rst.txt
│   │       ├── _static
│   │       │   ├── alabaster.css
│   │       │   ├── basic.css
│   │       │   ├── custom.css
│   │       │   ├── doctools.js
│   │       │   ├── documentation_options.js
│   │       │   ├── file.png
│   │       │   ├── language_data.js
│   │       │   ├── minus.png
│   │       │   ├── plus.png
│   │       │   ├── pygments.css
│   │       │   ├── searchtools.js
│   │       │   └── sphinx_highlight.js
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── intro.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── prep.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       └── train.html
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py
│       ├── docu_python
│       ├── index.rst
│       ├── intro.rst
│       ├── modules.rst
│       ├── prep.rst
│       ├── src
│       │   ├── prep.py
│       │   └── train.py
│       └── train.rst
├── environments.yml
├── logs
│   └── results.log
├── main.py
├── src
│   ├── __init__.py
│   ├── inference.py
│   ├── predict_house_prices.py
│   ├── prep.py
│   └── train.py
└── test
    └── import pandas as pd.py
```

*Cómo se ejecuta tu producto de datos:* 
To run the product you need to install **Docker Desktop** (https://docs.docker.com/get-started/get-docker/)

*Cómo instalarlo:* You don´t have to install anything than the *Docker Desktop*. Once the installed you have to run:

to train the  model: 
 - docker build -t train_imaage -f Dockerfile.train .
to execute the model:
docker build -t train_imaage -f Dockerfile.inference .

*casos licencia:* GNU
