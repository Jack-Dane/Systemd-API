# Systemd Hello World API
This project is a simple example of how systemd works at running an application. 

The API runs on port 8000 and has only one endpoint at root that will return hello world. 

## Setup

### Create the virtual environment

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

### Generate the config template

1. `source venv/bin/activate`
2. `python generate_template.py`

By default, the `generate_template.py` file will use the current user running the command to run the systemd process. 
A `--user <username>` argument can be parsed to the `generate_template` script if you want to use a different user.  

### Setup the Systemd application

1. `chmod +x run.sh` - with the user running the process in the previous step
2. `sudo cp config/hello_world_api.service /etc/systemd/system/`

## Starting the API Service

`systemctl start hello_world_api.service`

If you make changes or copy the file again, you should run `systemctl daemon-reload` after making the changes. 

