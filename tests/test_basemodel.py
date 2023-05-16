import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

        def setUp(self):
            self.base_model = BaseModel()

        def test_attributes(self):
                self.assertIsInstance(self.base_model.id, str)
                self.assertIsInstance(self.base_model.created_at, datetime)
                self.assertIsInstance(self.base_model.updated_at, datetime)

        def test_str_method(self):
                expected_str = "[BaseModel] ({}) {}".format(
                        self.base_model.id, self.base_model.__dict__)
                self.assertEqual(str(self.base_model), expected_str)

        def test_save_method(self):
                prev_updated_at = self.base_model.updated_at
                self.base_model.save()
                self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

        def test_to_dict_method(self):
                base_model_dict = self.base_model.to_dict()
                self.assertIsInstance(base_model_dict, dict)
                self.assertIn('__class__', base_model_dict)
                self.assertEqual(base_model_dict['__class__'], 'BaseModel')
                self.assertIn('id', base_model_dict)
                self.assertEqual(base_model_dict['id'], self.base_model.id)
                self.assertIn('created_at', base_model_dict)
                self.assertEqual(base_model_dict['created_at'],
                self.base_model.created_at.isoformat())
                self.assertIn('updated_at', base_model_dict)
                self.assertEqual(base_model_dict['updated_at'],
                self.base_model.updated_at.isoformat())

        def test_to_dict_deserialization(self):
                                                                                                                                                                                                                    base_model_dict = self.base_model.to_dict()
                                                                                                                                                                                                                    new_base_model = BaseModel(**base_model_dict)
                                                                                                                                                                                                                    self.assertIsInstance(new_base_model, BaseModel)
                                                                                                                                                                                                                    self.assertEqual(new_base_model.id, self.base_model.id)
                                                                                                                                                                                                                    self.assertEqual(new_base_model.created_at, self.base_model.created_at)
                                                                                                                                                                                                                    self.assertEqual(new_base_model.updated_at, self.base_model.updated_at)
                                                                                                                                                                                                                    
        def test_to_dict_json_serialization(self):
                                                                                                                                                                                                                            base_model_dict = self.base_model.to_dict()
                                                                                                                                                                                                                            json_data = json.dumps(base_model_dict)
                                                                                                                                                                                                                            self.assertIsInstance(json_data, str)
                                                                                                                                                                                                                            
        def test_to_dict_json_deserialization(self):
                base_model_dict = self.base_model.to_dict()
                json_data = json.dumps(base_model_dict)
                new_base_model_dict = json.loads(json_data)
                new_base_model = BaseModel(**new_base_model_dict)
                self.assertIsInstance(new_base_model, BaseModel)
                self.assertEqual(new_base_model.id, self.base_model.id)
                self.assertEqual(new_base_model.created_at, self.base_model.created_at)
                self.assertEqual(new_base_model.updated_at, self.base_model.updated_at)

                
if __name__ == '__main__':
        unittest.main()
                                                                                                                                                                                                                                                                                                                                                                            
