#!/usr/bin/python3
import sys
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.my_number = 89
        self.my_model.name = 'My First Model'

    def test_save(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(my_model_dict['name'], 'My First Model')
        self.assertEqual(my_model_dict['id'], self.my_model.id)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
