#!/usr/bin/env python3
# coding: utf-8

class QuestionPaser:
    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)
        return entity_dict

    def parser_main(self, res_classify):
        print(f"【解析调试】收到分类结果: {res_classify}")  # test
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            
            if question_type == 'staff_office':
                sql = self.sql_transfer(question_type, entity_dict.get('staff'))
                
            elif question_type == 'staff_phone':
                sql = self.sql_transfer(question_type, entity_dict.get('staff'))
                
            elif question_type == 'department_head':
                sql = self.sql_transfer(question_type, entity_dict.get('department'))
                
            elif question_type in ['graduation_requirement', 'makeup_exam', 'retake_course', 
                                  'retake_fail', 'course_conflict', 'score_problem', 
                                  'elective_course', 'dorm_problem', 'leave_procedure',
                                  'second_class', 'earn_credits','learning_difficulty', 'speech_fear', 'inferiority', 
    'breakup', 'insomnia', 'time_balance', 'dorm_repair',
    'canteen_complaint', 'pe_test', 'lost_card', 'bike_theft']:
                sql = ["MATCH (m:Policy) WHERE m.name='{0}' RETURN m.name, m.info".format(question_type)]
                
            if sql:
                sql_['sql'] = sql
                sqls.append(sql_)
        return sqls

    def sql_transfer(self, question_type, entities):
        if not entities:
            return []
            
        sql = []
        if question_type == 'staff_office':
            sql = ["MATCH (m:Staff) WHERE m.name='{0}' RETURN m.name, m.office".format(i) for i in entities]
            
        elif question_type == 'staff_phone':
            sql = ["MATCH (m:Staff) WHERE m.name='{0}' RETURN m.name, m.phone".format(i) for i in entities]
            
        elif question_type == 'department_head':
            sql = ["MATCH (m:Department)-[r:has_head]->(n:Staff) WHERE m.name='{0}' RETURN m.name, n.name".format(i) for i in entities]
            
        return sql