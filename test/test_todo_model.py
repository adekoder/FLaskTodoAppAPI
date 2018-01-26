from test import Todo, BaseAppApiTest

class TestTodoModel(BaseAppApiTest):

    def test_todo_model(self):
        todo = Todo()
        todo.todo_id = '122'
        todo.todo_task = 'will go to sch'
        todo.status = 'completed'
        todo.user_id = '12323'
        self.assertEqual(None,todo.save())
