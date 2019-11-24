import unittest
from io import StringIO

from customout import CustomOutBase, end_filter, stdout_temp

temp = ""


class CustomOutTest(unittest.TestCase):
    def test_stdout_temp(self):

        class __Stringify(CustomOutBase):
            @end_filter
            def write(self, s: str) -> int:
                global temp
                temp = s
                return len(temp)

        @stdout_temp(__Stringify())
        def __printer(s: str):
            print(s)

        ans = "test"
        __printer(ans)
        self.assertEqual(temp, ans)
