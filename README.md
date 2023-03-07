# holec-fastredis-lab
This is me learning to work with Redis

# Getting startet
Create virtualenvironment and install aioredis

```
python3.11 -m venv ./.venv
source ./.venv

pip install aioredis

or 

pip install -r requirements.txt
```
# Development
If you want to work on this the following steps need to be done

```
source ./.venv
pip install -r dev-requirements.txt
```

# Upgrade packages
This repository uses pip-tools to better manage the requirements. 
Input file for pip-tools is requirements.in, requirments.txt is always generated!
```
source ./venv
pip-compile --upgrade
```
