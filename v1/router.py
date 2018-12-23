# coding: utf-8
from v1 import wsgi


class ControllerTest(object):
    def __init__(self):
        print ("ControllerTest!!!!")
    def test(self,req):
          print("req",req)
          return {
            'name': "test",
            'properties': "test"
        }

    def test_v2(self, req):
        print("req", req)
        return {
            'name': "test_v2",
            'properties': "test_v2"
        }

class MyRouterApp(wsgi.Router):
      '''
      app
      '''
      def __init__(self,mapper):
          controller = ControllerTest()
          mapper.connect('/test',
                         controller=wsgi.Resource(controller),
                         action='test',
                         conditions={'method': ['GET']})
          mapper.connect('/test_v2',
                         controller=wsgi.Resource(controller),
                         action='test_v2',
                         conditions={'method': ['GET']})
          super(MyRouterApp, self).__init__(mapper)