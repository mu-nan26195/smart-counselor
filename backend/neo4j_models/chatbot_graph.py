#!/usr/bin/env python3
# coding: utf-8
from neo4j_models.question_classifier import *
from neo4j_models.question_parser import *
from neo4j_models.answer_search import *

class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        print(f"\n=== 处理问题: '{sent}' ===")
        
        # 1. 问题分类
        res_classify = self.classifier.classify(sent)
        print(f"分类结果: {res_classify}")
        
        if not res_classify:
            print("无法分类的问题")
            return "抱歉，这个问题超出了我的理解范围"
        
        # 2. SQL解析
        res_sql = self.parser.parser_main(res_classify)
        print(f"生成的查询: {res_sql}")
        
        # 3. 搜索答案
        final_answers = self.searcher.search_main(res_sql)
        print(f"搜索结果: {final_answers}")
        
        # 4. 结果处理
        if not final_answers:
            if res_classify.get('question_types'):
                print("识别到问题类型但无答案")
                return "关于这个问题，我暂时没有足够的信息，建议咨询教务处或辅导员"
            else:
                print("完全未知的问题类型")
                return "抱歉，我还没学会回答这个问题"
        
        return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('学生:')
        answer = handler.chat_main(question)
        print('智能辅导员:', answer)