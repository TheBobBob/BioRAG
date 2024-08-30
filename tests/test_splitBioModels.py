import unittest

from splitBioModels import splitBioModels

class Testing(unittest.TestCase):
    def test_split(self):
        data_path = r"C:\Users\navan\Downloads\BioModelsRAG\BioModelsRAG\2data"
        data = splitBioModels(directory=data_path)
        #import pdb;pdb.set_trace()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data)>0)

if __name__ == '__main__':
    unittest.main()