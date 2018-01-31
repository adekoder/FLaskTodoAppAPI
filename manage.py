from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app('development')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def runtest():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()
