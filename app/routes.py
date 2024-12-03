from flask import Blueprint, render_template

# 創建 Blueprint（模組化管理路由）
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')  # 渲染首頁模板
