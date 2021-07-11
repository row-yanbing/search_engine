from typing import List
from dataclasses import dataclass

from src.search.context import QueryAnalysisConf


@dataclass
class SegmentW:
    segment: str = ""
    weight: float = 0.0


class QueryAnalysis:
    def __init__(self, context: QueryAnalysisConf, query: str):
        self.query = query
        self.__context = context

    def analyse(self):
        """
        query分析入口
        :return: 分析结果
        """
        segments = self.__seg()
        seg_ws = self.__term_weighting(segments)
        return seg_ws

    def __seg(self):
        """
        分词
        :return: 分词结果
        """
        return self.query.split()

    def __term_weighting(self, segments: List) -> List:
        """
        词权接口
        :param segments: 分词结果
        :return: list(分词-权重)
        """
        seg_ws = []
        for segment in segments:
            weight = self.__context.core_w if len(segment) > 2 else self.__context.other_w
            cur_segw = SegmentW(segment, weight)
            seg_ws.append(cur_segw)
        return seg_ws
