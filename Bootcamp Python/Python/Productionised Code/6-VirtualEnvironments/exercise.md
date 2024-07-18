
- Create two new virtual environments with the details below: 
1. - Name: `datasci` 
   - Installs: jupyter, numpy, pandas, matplotlib, scikit-learn

2. - Name: `webdev`
   - Installs: jupyter, requests, fastapi, uvicorn, pytest

- For both virtual environments, freeze the requirements into a text file (You can use different names for their requirements files, for example, `datasci_requirements.txt` and `webdev_requirements.txt`). The name `requirements.txt` is just a convention used for describing a particular project's requirements. 

- Create two new Python scripts populated with one import line in each, shown below. Activate the `datasci` virtual environment, and execute both scripts, what do you notice? 
Now deactivate `datasci`, activate `webdev`, and execute both scripts, what do you notice? 


```Python
# script1.py
import matplotlib.pyplot as plt

```

```Python 
# script2.py
import requests

```

