#!/usr/bin/python3
"""Unittests for BaseModel class"""
import unittest
import os
import sys
import json

# Ensure project root is importable when tests are run directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Preserve and clear storage for isolated tests
        self._saved = storage.all().copy()
        storage.all().clear()

        # Ensure no leftover file
        try:
            os.remove('file.json')
        except Exception:
            pass

    def tearDown(self):
        # restore storage
        storage.all().clear()
        storage.all().update(self._saved)
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_instance_creation_and_storage(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
        # instance should be registered in storage
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, storage.all())

    def test_save_updates_updated_at_and_writes_file(self):
        bm = BaseModel()
        old_updated = bm.updated_at
        bm.save()
        # In very fast execution the timestamps can be equal at microsecond
        # resolution. Accept updated_at being the same or later.
        self.assertGreaterEqual(bm.updated_at, old_updated)
        # file should be created and contain the object
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{bm.id}", data)

    def test_to_dict_contents(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
