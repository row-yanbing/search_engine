import yaml


class Constant:
    CORE_W = "core_w"
    DEFAULT_CORE_W = 1.2
    OTHER_W = "other_w"
    DEFAULT_OTHER_W = 0.6


class InputArgs:
    query = "query"
    uid = "uid"


class OutputArgs:
    data = "data"
    cost = "cost"
    errno = "errno"
    msg = "message"


class QueryAnalysisConf:
    def __init__(self, conf_path):
        with open(conf_path, "r") as fr:
            qa_conf = yaml.safe_load(fr)
        self.core_w = qa_conf.get(Constant.CORE_W, Constant.DEFAULT_CORE_W)
        self.other_w = qa_conf.get(Constant.OTHER_W, Constant.DEFAULT_OTHER_W)
