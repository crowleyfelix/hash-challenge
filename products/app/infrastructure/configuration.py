import os

def get_config():
    env = os.environ

    return {
        "port": env.get("PORT")
    }