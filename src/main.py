import os
from microservice import app

__author__ = "IBM Cloud Managed Application Services"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
