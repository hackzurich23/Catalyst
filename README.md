## Installation

```bash
pip install -r requirements.txt  
```

## ENV
the project is using the gpt-3.5-turbo-16k-0613 model. To get access to it, specify your OPENAI_API_KEY in the .env file


## Launch backend

in the root directory (in timeline):
```bash
python backend/app.py  
```

## Deployment
### Backend
To have access to all the required packages you need to activate the venv like this:
```bash
cd project/timeline
source myvenv/bin/activate
```
To serve flask backend in the debug mode:
```bash
python backend/app.py
```

The API is accessible by the external id of the VM + :3000 
