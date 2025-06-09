#!/usr/bin/env python3
# coding: utf-8
import os
import ahocorasick as pyahocorasick

class QuestionClassifier:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
        # 特征词路径（使用绝对路径）
        self.department_path = os.path.join(project_root, 'data', 'department.txt')
        self.staff_path = os.path.join(project_root, 'data', 'staff.txt')
        self.policy_path = os.path.join(project_root, 'data', 'policy.txt')
        
        # 调试输出
        print(f"项目根目录: {project_root}")
        print(f"院系文件路径: {self.department_path}")
        print(f"文件存在: {os.path.exists(self.department_path)}")
        
        # 验证路径
        if not os.path.exists(self.department_path):
            raise FileNotFoundError(f"无法找到文件，请检查路径: {self.department_path}")
        
            
        # 加载特征词
        self.department_wds = [i.strip() for i in open(self.department_path, encoding='utf-8') if i.strip()]
        self.staff_wds = [i.strip() for i in open(self.staff_path, encoding='utf-8') if i.strip()]
        self.policy_wds = [i.strip() for i in open(self.policy_path, encoding='utf-8') if i.strip()]
        
        self.region_words = set(self.department_wds + self.staff_wds + self.policy_wds)
        
        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()
        
        # 问句疑问词
        self.office_qwds = ['办公室', '在哪', '位置', '哪里', '办公地点']
        self.phone_qwds = ['电话', '联系方式', '怎么联系', '手机号']
        self.head_qwds = ['系主任', '主任', '负责人', '谁负责']
        self.graduation_qwds = ['毕业', '怎么毕业', '毕业要求']
        self.exam_qwds = ['挂科', '补考', '不及格']
        self.retake_qwds = ['重修', '重考']
        self.conflict_qwds = ['课程冲突', '时间冲突']
        self.score_qwds = ['成绩', '分数', '考试成绩']
        self.elective_qwds = ['公选课', '选修课', '通识课']
        self.dorm_qwds = ['宿舍', '室友', '换宿舍']
        self.leave_qwds = ['请假', '请假流程']
        self.credit_qwds = ['第二课堂', '三大学分', '创新创业', '社会实践', '素质拓展']
        self.counselor_qwds = ['辅导员', '班主任', '导师']  
        self.fail_qwds = ['挂科', '不及格', '补考', '重修']  
        self.learning_difficulty_qwds = ['学习难度', '课程难', '听不懂', '学习课程有难度']
        self.speech_fear_qwds = ['公开演讲', '上台发抖', '演讲恐惧']
        self.inferiority_qwds = ['自卑', '比同学差', '觉得自己差']
        self.breakup_qwds = ['失恋', '学不进去']
        self.insomnia_qwds = ['失眠', '睡不着']
        self.time_balance_qwds = ['平衡学生会', '时间分配']
        self.repair_qwds = ['空调坏了', '报修']
        self.canteen_qwds = ['食堂异物', '吃出异物']
        self.pe_test_qwds = ['体测不及格', '体测补考']
        self.lost_card_qwds = ['学生证丢了', '身份证丢了']
        self.bike_theft_qwds = ['车被偷', '自行车被盗']
    def classify(self, question):
        data = {}
        school_dict = self.check_school(question)
        print(f"【分类调试】输入问题: '{question}'")
        print(f"【分类调试】识别实体: {school_dict}")
        if not school_dict:
            return {}
        data['args'] = school_dict
        types = []
        for type_ in school_dict.values():
            types += type_
            
        question_types = []
        school_dict = self.check_school(question)
        print(f"【分类调试】输入问题: '{question}'")  # test
        print(f"【分类调试】识别实体: {school_dict}")  # test
    
        if not school_dict:
            print("【分类调试】未识别到有效实体")  # test
            return {"【分类调试】未识别到有效实体"}

        # 办公室位置
        if self.check_words(self.office_qwds, question) and ('staff' in types):
            question_type = 'staff_office'
            question_types.append(question_type)
            
        # 电话查询
        if self.check_words(self.phone_qwds, question) and ('staff' in types):
            question_type = 'staff_phone'
            question_types.append(question_type)
            
        # 系主任查询
        if self.check_words(self.head_qwds, question) and ('department' in types):
            question_type = 'department_head'
            question_types.append(question_type)
            
        # 毕业要求
        if self.check_words(self.graduation_qwds, question):
            question_type = 'graduation_requirement'
            question_types.append(question_type)
            
        # 补考
        if self.check_words(self.exam_qwds, question) and not self.check_words(self.retake_qwds, question):
            question_type = 'makeup_exam'
            question_types.append(question_type)
            
        # 重修
        if self.check_words(self.retake_qwds, question):
            question_type = 'retake_course'
            question_types.append(question_type)
            
        # 课程冲突
        if self.check_words(self.conflict_qwds, question):
            question_type = 'course_conflict'
            question_types.append(question_type)
            
        # 成绩问题
        if self.check_words(self.score_qwds, question):
            question_type = 'score_problem'
            question_types.append(question_type)
            
        # 公选课
        if self.check_words(self.elective_qwds, question):
            question_type = 'elective_course'
            question_types.append(question_type)
            
        # 宿舍问题
        if self.check_words(self.dorm_qwds, question):
            question_type = 'dorm_problem'
            question_types.append(question_type)
            
        # 请假流程
        if self.check_words(self.leave_qwds, question):
            question_type = 'leave_procedure'
            question_types.append(question_type)
            
        # 学习困难
        if self.check_words(self.learning_difficulty_qwds, question):
            question_types.append('learning_difficulty')

        # 演讲恐惧
        if self.check_words(self.speech_fear_qwds, question):
            question_types.append('speech_fear')

        # 自卑心理
        if self.check_words(self.inferiority_qwds, question):
            question_types.append('inferiority')

        # 失恋问题
        if self.check_words(self.breakup_qwds, question):
            question_types.append('breakup')

        # 失眠问题
        if self.check_words(self.insomnia_qwds, question):
            question_types.append('insomnia')

        # 时间平衡
        if self.check_words(self.time_balance_qwds, question):
            question_types.append('time_balance')

        # 宿舍报修
        if self.check_words(self.repair_qwds, question):
            question_types.append('dorm_repair')

        # 食堂投诉
        if self.check_words(self.canteen_qwds, question):
            question_types.append('canteen_complaint')

        # 体测问题
        if self.check_words(self.pe_test_qwds, question):
            question_types.append('pe_test')

        # 证件丢失
        if self.check_words(self.lost_card_qwds, question):
            question_types.append('lost_card')

        # 车辆被盗
        if self.check_words(self.bike_theft_qwds, question):
            question_types.append('bike_theft')
        # 第二课堂学分
        if self.check_words(self.credit_qwds, question):
            if '三大学分' in question or '怎么获得' in question:
                question_type = 'earn_credits'
            else:
                question_type = 'second_class'
            question_types.append(question_type)
            
        data['question_types'] = question_types
        return data

    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.department_wds:
                wd_dict[wd].append('department')
            if wd in self.staff_wds:
                wd_dict[wd].append('staff')
            if wd in self.policy_wds:
                wd_dict[wd].append('policy')
        return wd_dict

    def build_actree(self, wordlist):
        actree = pyahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    def check_school(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i:self.wdtype_dict.get(i) for i in final_wds}
        return final_dict

    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False