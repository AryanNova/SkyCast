from app import createApp
from dotenv import load_dotenv
import os
load_dotenv()
app=createApp()
if __name__=="__main__":
    is_debug=os.getenv('FLASK_DEBUG')=="1"
    app.run(debug=is_debug)
