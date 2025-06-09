#!/usr/bin/env python3
# coding: utf-8
from py2neo import Graph

class AnswerSearcher:
    def __init__(self):
        try:
            self.g = Graph(
                "bolt://localhost:7687",
                auth=("neo4j", "12345678"),  
                secure=False  
            )
            test_result = self.g.run("RETURN '连接成功' AS message").data()
            print("Neo4j连接测试:", test_result)
            
        except Exception as e:
            print("连接失败:", str(e))
            print("请检查：")
            print("1. Neo4j服务是否正在运行")
            print("2. 密码是否正确（注意大小写）")
            print("3. 防火墙是否允许7687端口通信")
            raise

    def search_main(self, sqls):
        final_answers = []
        print(f"【查询调试】待执行查询: {sqls}")  # test
        for sql_ in sqls:
            print(f"执行查询: {sql_['sql']}")  # test
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    def answer_prettify(self, question_type, answers):
        if not answers:
            return "未找到相关信息，请咨询辅导员或教务处"
        
        if question_type == 'staff_office':
            return f"{answers[0]['m.name']}的办公室在：{answers[0]['m.office']}"
            
        elif question_type == 'staff_phone':
            return f"{answers[0]['m.name']}的电话是：{answers[0]['m.phone']}"
            
        elif question_type == 'department_head':
            return f"{answers[0]['m.name']}的系主任是{answers[0]['n.name']}老师"
            
        elif question_type == 'graduation_requirement':
            return "参照自己本专业的培养方案，梳理清楚有关必修课、专业任选课、专业限选课、公共课等方面的学分要求，需要在毕业前全部通过才可以毕业"
            
        elif question_type == 'makeup_exam':
            return "课程挂科需要等到开学后前两周内参加补考"
            
        elif question_type == 'retake_course':
            return "补考成绩不及格需要报名重修，报名重修的时间为每学期开学的前两周"
            
        elif question_type == 'retake_fail':
            return "重修考试成绩依然不及格需要继续报名重修，并且重修没有补考机会"
            
        elif question_type == 'course_conflict':
            return "课程冲突需要凭课程表办理免听手续"
            
        elif question_type == 'score_problem':
            return "考试成绩有问题需要等到开学后第一时间联系任课老师，必要时期可线上联系"
            
        elif question_type == 'elective_course':
            return "公选课学分，建议查询自己专业对应的培养方案，找到通识课应修学分。通识课选课在每学期开学后的两周内进行选课。"
            
        elif question_type == 'dorm_problem':
            return "与室友闹矛盾了想换宿舍，及时和辅导员沟通调解，但由于学校床位紧张，得不到及时满足，建议专注自己的个人发展"
            
        elif question_type == 'leave_procedure':
            return "学生请假流程：若请假期间内有课，需要联系任课老师并在今日校园内线上请假并交由辅导员审批；若请假时间内无课，可在今日校园内线上请假，并交由辅导员审批。"
            
        elif question_type == 'second_class':
            return "第二课堂的三大学分是：创新创业学分、社会实践学分、素质拓展学分"
            
        elif question_type == 'earn_credits':
            return "三大学分获得方式：按照学分文件，积极参加创新课程、创新比赛，参加寒暑假社会实践，学习盗梦空间并获得素质拓展类的相关证书"
            
        elif question_type == 'learning_difficulty':
            return "学习课程有难度，建议上课认真听讲，下课及时总结，若无效，可学习B站或慕课等线上资源辅助理解。"

        elif question_type == 'speech_fear':
            return "害怕公开演讲是正常现象，哈佛调查显示85%的优秀演讲者初期更恐惧。建议增加发言机会，逐步提升自信心。"

        elif question_type == 'inferiority':
            return "自卑是深度思考者的常见特征。爱因斯坦曾因成绩差退学，JK罗琳被拒稿12次。建议每天完成3件小事（如教会同学1个技巧、整理专业动态、运动15分钟）提升掌控感。"

        elif question_type == 'breakup':
            return "失恋是人生的小挫折，未来仍漫长。若无法自我排解，请及时联系老师或朋友谈心。"

        elif question_type == 'insomnia':
            return "失眠建议：固定作息时间，按计划推进任务，避免睡前使用电子设备。"

        elif question_type == 'time_balance':
            return "时间分配建议：50%精力给专业课核心知识，30%给学生会不可替代工作，20%培训新人处理机械化事务。"

        elif question_type == 'dorm_repair':
            return "宿舍报修问题：若线上报修未解决，直接联系宿管阿姨协助处理。"

        elif question_type == 'canteen_complaint':
            return "食堂异物处理：1.要求退款（窗口协商）；2.要求赔偿+道歉（找经理）；3.彻查卫生（校长信箱）。"

        elif question_type == 'pe_test':
            return "体测不及格可申请补测或替代项目，总分≥60分即可毕业。参考《国家学生体质健康标准》。"

        elif question_type == 'lost_card':
            return "证件丢失：1.学生证联系辅导员按院系流程补办；2.身份证考试前可开在校证明。建议平时保管好证件。"

        elif question_type == 'bike_theft':
            return "车辆被盗：立即拨打校内报警电话7355110，并联系辅导员协助。"
        else:
            return answers[0]['m.info'] if answers else "抱歉，我暂时无法回答这个问题"