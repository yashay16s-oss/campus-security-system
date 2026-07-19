import os
from app import app, socketio, init_db

init_db()

port = int(os.environ.get('PORT', 5000))
print(f'🚀 ScratchXI starting on port {port}')
socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)