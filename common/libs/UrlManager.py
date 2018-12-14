class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buidStaticUrl(path):
        ver = "%s"%(222222)
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)
