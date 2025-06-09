import os
from neo4j_models.question_classifier import QuestionClassifier

print("=== 开始路径测试 ===")
try:
    qc = QuestionClassifier()
    print("=== 测试成功 ===")
except Exception as e:
    print(f"测试失败: {str(e)}")
    print("请检查：")
    print("1. 项目目录结构是否正确")
    print("2. 数据文件是否存在于指定位置")
    print("3. 文件权限是否正常")