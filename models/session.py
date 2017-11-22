from . import Mongua
from datetime import datetime


class SessionAdmin(Mongua):
    # 子类必须实现 _fields 类方法来定义字段
    # TODO expire
    @classmethod
    def _fields(cls):
        fields = [
            ('session_id', str, ''),
            ('user_id', str, ''),
            # ('session_key', str, ''),
            ('utcNow', datetime.utcnow, datetime.utcnow())
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def id_from_sessionid(cls, session_id):
        s = cls.find_one(session_id=session_id)
        return s.json().get('user_id')

    @classmethod
    def is_valid_login(cls, session_id):
        s = cls.find_one(session_id=session_id)
        if s is not None:
            return True
        else:
            return False
