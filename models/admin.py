import hashlib
from utils import (
    log,
)

from models import Mongua
from flask_wxapp import gen_3rd_session_key
from models.session import SessionAdmin
from flask import (
    request,
)


class Admin(Mongua):
    # 子类必须实现 _fields 类方法来定义字段
    @classmethod
    def _fields(cls):
        fields = [
            ('name', str, ''),
            ('password', str, ''),
            ('salt', str, 'salt')
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form, **kwargs):
        """
        new 是给外部使用的函数
        这是继承覆盖父类的方法, 因为要重写 password
        """
        m = super().new(form)
        m.password = m.salted_password(form.get('password', ''))
        m.save()
        return m

    def blacklist(self):
        b = [
            '_id',
            'password',
            'salt',
        ]
        return b

    def salted_password(self, password):
        salt = self.salt
        hash1 = hashlib.md5(password.encode('ascii')).hexdigest()
        hash2 = hashlib.md5((hash1 + salt).encode('ascii')).hexdigest()
        return hash2

    def update_password(self, password):
        self.password = self.salted_password(password)
        self.save()

    def validate_auth(self, form):
        username = form.get('name', '')
        password = form.get('password', '')
        username_equals = self.name == username
        password_equals = self.password == self.salted_password(password)
        if username_equals and password_equals:
            s = SessionAdmin.new(session_id=gen_3rd_session_key(), user_id=self.id)
            return s.session_id
        return None

    @classmethod
    def is_valid_login(cls, session_id):
        return SessionAdmin.is_valid_login(session_id)

    @classmethod
    def find_by_openid(cls, openid):
        """
        用 openid 查找，没有就新建一个
        :param openid: 
        :return: 
        """
        u = cls.find_one(openid=openid)
        if u is None:
            u = cls.new({
                "openid": openid,
            })
        # log(u)
        return u

    @classmethod
    def current_admin(cls):
        session_id = request.cookies.get('Session-id', None)
        admin_id = SessionAdmin.id_from_sessionid(session_id)
        return cls.get(admin_id)


def test():
    Admin.new(dict(name='chen', password='123'))


if __name__ == '__main__':
    test()


