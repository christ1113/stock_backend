class Config:
    SECRET_KEY = 'your_secret_key'  # 用於加密會話數據
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'  # SQLite 資料庫路徑
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 關閉資料庫修改追蹤
