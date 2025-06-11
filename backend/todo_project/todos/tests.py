from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    def setUp(self):
        Todo.objects.create(title="Test Todo", description="This is a test todo item.")

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEquals( expected_object_name, 'first todo item')
        expected_object_name= f"{todo.title} "

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
         expected_object_name = f"{todo.body}"
        self.assertEquals( expected_object_name, "a body here")