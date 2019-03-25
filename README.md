


# Setup-the-data-folder

If you desire to run the analyses you **MUST** setup the data folder as follows, before doing anything else.

Download the data in this [link](https://drive.google.com/open?id=1-oG5-kBt9xQ3Li4PEexpiA9_7RZhRM1f) and unzip it inside the **data** directory. The structure should be maintained like this:


    ├── data
        ├── raw                    <- Data from the link above.
            ├── winequality.csv    <- Wine's data csv.

# How to install?

You can do it by using the [Docker option](#by-using-docker) or [Manually installing dependencies on Python 3.6](#by-manually-installing).

## By using docker

You may not want to install everything by hand. It is not that hard, but you just may not want it. If so, you can use docker to faster deploy the service and see the results in a containerized set of notebooks.

**Requirements: Install docker first!**: 1 - [install docker CE according to you OS](https://docs.docker.com/install/linux/docker-ce/ubuntu/). 2 - [install docker compose](https://docs.docker.com/compose/install/).

Build the image and run the image. Use `docker-compose` to in two lines build and run both services, the notebook mirror and the rest api.

```shell
docker-compose build
docker-compose up 
```

There is a `MAKEFILE` which automates the processes. Use:
- `make build` to build all containers at once (the notebook and the API); 
- `make notebook` to run the notebok inside a docker container;

### The jupyter notebook

Go to [http://127.0.0.1:8888](http://127.0.0.1:8888) to bring up a jupyter notebook interface inside the solution. You might need to autenticate your usage the first you build it. To do it, copy the **token** given in the shell as exhibited bellow:

<img src="imgs/docker-shell.png" alt="drawing" width="1200"/>

And it is all set :)

> WARNING: the data folder [must be set](#setup-the-data-folder) since it is not inserted inside the consider, rather it is mapped to the local volume.


# Answers

Most of the findigs are inside the notebooks. They are:
 - [Analyses 01](notebooks/analyses-01.ipynb): it contains the statistical sampling of the out-of-sample test data. 10% of data is held to out to used only onced, before model deployment. Stratified cross-validation has been used. Two chunks of the original dataset are generated here: `winequality_10.csv` and `winequality_90.csv`.

  - [Analyses 02](notebooks/analyses-02.ipynb): The exploratory analyses are made here! Incosistences have been cleaned as well. We also highlight the most relevant features, which are: `alcohol` and `volatile acidity`. We used two techniques: ANOVA and Random Forest, and by that we ratifies our initial hypothesis that the feature `type` ought to be removed from the model development, since it could add human bias towards the classification.

  - [Analyses 03](notebooks/analyses-02.ipynb): This is the model selection notebook. We make use of several classiers, that have different point of views.