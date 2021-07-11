import logging
import time
from flask_restplus import Resource, Namespace, reqparse
from src.search.query_analysis import QueryAnalysis
from src.search.context import QueryAnalysisConf, InputArgs, OutputArgs

logging.basicConfig(level=logging.DEBUG)
api = Namespace("search", description="搜索接口")
doc_parser = api.parser()
doc_parser.add_argument(InputArgs.query, type=str, help="用户请求", required=True)
doc_parser.add_argument(InputArgs.uid, type=int, help="用户id", required=True)
context = QueryAnalysisConf("./config/operator.yaml")


@api.doc(parser=doc_parser)
@api.route("/", doc={"description": "获得搜索结果"})
class Search(Resource):
    def get(self):
        return {"success": 1}

    def post(self):
        start = time.time()
        req_parser = reqparse.RequestParser()
        req_parser.add_argument(InputArgs.query, type=str)
        req_parser.add_argument(InputArgs.uid, type=int)
        args = req_parser.parse_args()
        logging.debug(args)
        qa = QueryAnalysis(context, args.get(InputArgs.query, ""))
        seg_ws = qa.analyse()
        end = time.time()
        cost = round((end - start) * 1000, 2)
        response_dict = Search.gen_response(seg_ws, cost)
        return response_dict

    @staticmethod
    def gen_response(seg_ws, cost):
        """
        拼接响应dict
        :param seg_ws: 分词，list(SegmentW)
        :param cost: 耗时
        :return: 响应
        """
        data = []
        for segw in seg_ws:
            cur_dict = {'segment': segw.segment, 'weight': segw.weight}
            data.append(cur_dict)
        response_dict = {
            OutputArgs.data: data,
            OutputArgs.cost: cost,
            OutputArgs.errno: 0,
            OutputArgs.msg: ""
        }
        return response_dict
