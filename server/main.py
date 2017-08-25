import logging
import dill
import pandas as pd
from flask import Flask, request
from werkzeug.exceptions import BadRequest

application = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")


def build_model(model_path):
    with open(model_path, "rb") as f:
        model = dill.load(f)
    return model


def launch_model(model, request):
    try:
        features_as_dict = request.get_json()
        features_as_df = pd.io.json.json_normalize(features_as_dict)

        logger.debug("Predicting {}".format(features_as_df))
        binary_predictions = model.predict(features_as_df)

        detected_zones = str(binary_predictions[0])
    except Exception as e:
        logger.exception("Error in pipeline")
        raise BadRequest(description=e.message)

    return detected_zones


@application.route("/predict", methods=["POST"])
def handle_autozone_request():
    global model
    return launch_model(model, request)


if __name__ == "__main__":
    try:
        model = build_model("pipeline.pk")
        application.run()
    except KeyboardInterrupt:
        logger.exception("Shutting down")
    except Exception, e:
        logger.exception("Error in initialization chain")
