# ML in prod
A python predictive system design.

## Building the pipeline
- `cd training`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python training.py`


## Running the server
- If you did the previous steps then: `cd ../; deactivate`
- `cd server`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python main.py`


## Making online predictions
Once the server is running you can send features via POST requests and then recieve the corresponding prediction (0 or 1).
You can find an example of the request body in `server/post.json`
