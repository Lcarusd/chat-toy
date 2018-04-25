# coding: utf-8


class Tools(object):

    @staticmethod
    def to_unicode(string, encoding='utf-8'):
        """
        将字符串转换为Unicode
        """
        if isinstance(string, str):
            return string.decode(encoding)
        elif isinstance(string, unicode):
            return string
        else:
            raise Exception('Unknown Type')
