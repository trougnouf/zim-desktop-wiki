from zim.formats import get_format, COLOR
from zim.parse import ParseTree

class TestColorFeature(tests.TestCase):

    def setUp(self):
        self.format = get_format('wiki')

    def testColorParsing(self):
        # Test parsing color syntax
        wiki = '{{color:red|This is red text}}'
        tree = self.format.Parser().parse(wiki)
        self.assertEqual(tree[0].tag, 'p')
        self.assertEqual(tree[0][0].tag, COLOR)
        self.assertEqual(tree[0][0]['value'], 'red')
        self.assertEqual(tree[0][0].text, 'This is red text')

    def testColorDumping(self):
        # Test dumping color syntax
        tree = ParseTree().fromstring('''
            <?xml version='1.0' encoding='utf-8'?>
            <zim-tree>
                <p>
                    <color value="blue">This is blue text</color>
                </p>
            </zim-tree>
        ''')
        wiki = self.format.Dumper().dump(tree)
        self.assertEqual(''.join(wiki), '{{color:blue|This is blue text}}')

    def testColorRoundTrip(self):
        # Test round-trip parsing and dumping
        wiki = '{{color:green|This is green text}}'
        tree = self.format.Parser().parse(wiki)
        dumped_wiki = self.format.Dumper().dump(tree)
        self.assertEqual(''.join(dumped_wiki), wiki)
