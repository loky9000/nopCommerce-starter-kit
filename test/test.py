import os

from qubell.api.testing import *

@environment({
    "default": {},
})
class nopCommerceStarterKit(BaseComponentTestCase):
    name = "nopCommerce-starter-kit"
    meta = "https://raw.github.com/qubell-bazaar/nopCommerce-starter-kit/master/meta.yml"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]
    @classmethod
    def timeout(cls):
        return 60

    @instance(byApplication=name)
    @values({"nopCommerce.url": "siteurl"})
    def test_site(self, instance, siteurl):
        import pycurl
        from StringIO import StringIO
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, siteurl)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        assert 'nopCommerce' in body        
