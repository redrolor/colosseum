from tests.utils import W3CTestCase

class TestInlineTableWidth(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'inline-table-width-'))
