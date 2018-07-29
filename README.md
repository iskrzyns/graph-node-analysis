[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/MTDzi/graph-node-analysis/master)


You can either create an Anaconda Environment on your local machine:
```
conda env create -f environment.yml
```

or run the notebooks using Binder (click the badge above).

---

If you're not using conda, you can create an environment like so:
```
python3 -m venv gna_env
source gna_env/bin/activate
```
and install the dependencies using `pip`:
```
pip install -r requirements.txt
```
and then run
```
jupyter-notebook
```
