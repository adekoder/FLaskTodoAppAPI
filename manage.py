from app import create_app
from flask_script import Manager
app = create_app('development')

manager = Manager(app)

@manager.command
def runtest():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=1).run(tests)

if __name__ == "__main__":
    manager.run()
