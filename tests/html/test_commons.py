from unittest import TestCase
from tests import asset_path
from libextract.html import get_etree


FOO_ASSET = asset_path('full_of_foos.html')


class TestGetEtree(TestCase):
    def setUp(self):
        with open(FOO_ASSET, 'rb') as fp:
            self.etree = get_etree(fp)

    def runTest(self):
        divs = self.etree.xpath('//body/article/div')
        assert all(k.text == 'foo.' for k in divs)
        assert len(divs) == 9
