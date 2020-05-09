import unittest
from immutable import *


class MyTestCase(unittest.TestCase):

    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(HashMap()), 0)
        self.assertEqual(size(put(HashMap(), 1, 2)), 1)

    def test_put(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(put(put(HashMap(), 1, 2), 2, 3)), {1: 2, 2: 3})

    def test_get(self):
        self.assertEqual(get(put(HashMap(), 1, 2), 1), 2)
        self.assertEqual(get(put(HashMap(), 3, 4), 3), 4)

    def test_size(self):
        self.assertEqual(size(HashMap()), 0)
        self.assertEqual(size(HashMap({'3': 23})), 1)
        self.assertEqual(size(HashMap({'3': 23, '4': 323})), 2)

    def test_del_(self):
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(del_(put(HashMap(), 1, 2), 1)), {})

    def test_to_dict(self):
        self.assertEqual(to_dict(None), {})
        self.assertEqual(to_dict(put(HashMap(), 1, 2)), {1: 2})
        self.assertEqual(to_dict(put(put(HashMap(), 1, 2), 2, 3)), {1: 2, 2: 3})

    def test_from_dict(self):
        test_data = {1: 2, 2: 3, 3: 4}
        self.assertEqual(to_dict(HashMap(test_data)), test_data)

    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(put(HashMap(), 1, 2)), [2])
        self.assertEqual(to_list(put(put(HashMap(), 1, 2), 2, 3)), [2,3])

    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(to_dict(mconcat(put(HashMap(), 1, 2), None)), to_dict(put(HashMap(), 1, 2)))
        self.assertEqual(to_dict(mconcat(None, put(HashMap(), 1, 2))), to_dict(put(HashMap(), 1, 2)))

    def test_map(self):
        self.assertEqual(to_dict(map(HashMap(), str)), {})
        self.assertEqual(to_dict(map(put(HashMap(), 1, 2), str)), {1: '2'})

    def test_reduce(self):
        self.assertEqual(reduce(HashMap(), lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce(HashMap({'3': 23, '4': 323}), lambda st, e: st + e, 0), 346)

    def test_iter(self):
        table = HashMap({1: 123, 2: 333, 3: 23, 4: 323})
        tmp = {}
        for e in table:
            tmp[e.key] = e.value
        self.assertEqual(to_dict(table), tmp)
        i = iter(HashMap())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()