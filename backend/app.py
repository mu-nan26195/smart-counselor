from flask import Flask, request, jsonify
from flask_cors import CORS
from neo4j_models.chatbot_graph import ChatBotGraph
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化聊天机器人
chatbot = ChatBotGraph()

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({
                'code': 400,
                'message': '问题不能为空',
                'data': None
            })
        
        logger.info(f"收到问题: {question}")
        answer = chatbot.chat_main(question)
        
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': {
                'question': question,
                'answer': answer
            }
        })
        
    except Exception as e:
        logger.error(f"处理问题时出错: {str(e)}")
        return jsonify({
            'code': 500,
            'message': f'服务器错误: {str(e)}',
            'data': None
        })

@app.route('/api/health')
def health_check():
    return jsonify({
        'code': 200,
        'message': '服务运行正常',
        'data': None
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)