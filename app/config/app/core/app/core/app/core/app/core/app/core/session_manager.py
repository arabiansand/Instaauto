import os


class SessionManager:
    SESSION_DIR = "data/sessions"

    @classmethod
    def session_path(cls, username):
        return os.path.join(cls.SESSION_DIR, f"{username}.json")
