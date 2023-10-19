# rest-endpoints-fastapi
a brief test

To run (windows):

Install Python.

Launch cmd (NOT powershell terminal as script running in powershell is forbidden by default).

Clone the repository.

cd to the cloned directory.

Activate the virtual environment:

venv\Scripts\activate

Note on linux the command to activate a venv is as follows:

source ./venv/bin/activate

Install the pre-requisites:

py -m pip install -r requirements.txt

Run the restful API server...

py -m uvicorn main:app --reload

Test:

Repeatedly call: 127.0.0.1:8000


