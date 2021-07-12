import os
import yaml
from flask import Flask
from flask_restplus import Resource, Api
from flask_cors import CORS
from src.views.search_view import api as search_api

SERVICE_CONF_PATH = os.path.realpath("./config/service.yaml")
with open(SERVICE_CONF_PATH, "r") as fr:
    service_conf = yaml.safe_load(fr)
IP = service_conf.get("ip", "0.0.0.0")
PORT = service_conf.get("port", 8888)


def create_app():
    app = Flask(__name__)
    app.config["IP"] = IP
    app.config["PORT"] = PORT
    return app


app = create_app()
CORS(app, supports_credentials=True)
api = Api(app, title="搜索服务API", version="1.0", description="搜索引擎API")
api.add_namespace(search_api)


@api.route("/", doc={"description": "搜索服务API"})
class Index(Resource):
    def get(self):
        return {}


if __name__ == "__main__":
    app.run(host=app.config["IP"], port=app.config["PORT"])
