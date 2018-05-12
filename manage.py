# manage.py

import os


from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import DB, create_app
from app import models


#config_name = os.getenv('APP_SETTINGS')
config_name = "DEVELOPMENT"
app = create_app(config_name)
migrate = Migrate(app, DB)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()