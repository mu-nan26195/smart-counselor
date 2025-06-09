# smart-counselor
# 🎓 智能辅导员系统

[![Vue](https://img.shields.io/badge/Vue-3.3-green)](https://vuejs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-blue)](https://flask.palletsprojects.com/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.11-purple)](https://neo4j.com/)

基于知识图谱的校园智能咨询系统，支持20+学生常见问题自动解答

## 🌟 在线体验
- 前端演示：[GitHub Pages](https://你的用户名.github.io/smart-counselor)
- API文档：[Swagger UI](https://你的后端部署地址/docs)

## 🛠️ 技术栈
| 模块       | 技术                 |
|------------|----------------------|
| 前端       | Vue3 + Element Plus  |
| 后端       | Flask + Py2neo       |
| 数据库     | Neo4j 知识图谱       |
| 部署       | Vercel + GitHub Pages|

## 🚀 本地运行
### 后端服务
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 前端开发
```bash
cd frontend
npm install
npm run dev
```

## 📦 项目结构
```
smart-counselor/
├── backend/          # Flask后端API
├── frontend/         # Vue3前端SPA
├── data/             # 知识图谱数据集
└── docs/             # 设计文档
```

## 📌 核心功能
- 自然语言问题分类
- 知识图谱语义查询
- 实时对话交互界面
- 多终端响应式设计


## 📄 许可证
[MIT License](LICENSE)