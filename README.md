# ML in prod
A python predictive system design.

## Building the pipeline
```bash
$ cd training
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python training.py
```

## Running the server
- If you did the previous steps then:
```bash
$ cd ../; deactivate
$ cd server
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

## Making online predictions
Once the server is running you can send features via POST requests and then receive the corresponding prediction (0 or 1).
You can find an example of the request body in `server/post.json`:
```bash
$ curl -H "Content-Type: application/json" -X POST --data @post.json http://localhost:5000/predict
```

