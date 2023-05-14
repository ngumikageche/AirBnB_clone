#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_review = Review()
my_review.place_id = "kinoo54"
my_review.user_id = "54143"
my_review.text = "Hapo nyumba ni chap na worth"
my_review.save()
print(my_review)

