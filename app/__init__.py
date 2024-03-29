"""Creates the main program of the """
import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command

class App:
    """The main function of the program"""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(App, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.commandList = [] # pylint: disable=invalid-name
        self.load_plugins()
    def configure_logging(self):
        """Configures logging based on config files and environment variables"""
        logging_conf_path = self.get_environment_variable("LOGGINGCONF",'logging.conf')
        logging_file_name = self.get_environment_variable("LOGGINGPATH",'log')
        logging_level = self.get_environment_variable("LOGGING","INFO")

        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s',filename=logging_file_name)
        if logging_level:
            logger = logging.getLogger()
            logger.setLevel(logging_level)
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Loads environment variables into a settings variable"""
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var, default=None):
        """Returns a environment variable by name"""
        if not self.settings.get(env_var):
            return default
        return self.settings.get(env_var)

    def load_plugins(self):
        """Loads plugins from a pre-determined directory"""
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning("Plugins directory '%s' not found.",plugins_path)
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                    self.commandList.append(plugin_name)
                except ImportError as e:
                    logging.error("Error importing plugin %s: %s", plugin_name, e)

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Registering function"""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info("Command '%s' from plugin '%s' registered.",plugin_name,plugin_name)
    def start(self):
        """Starting function"""
        print("Application started. Type 'exit' to exit.")
        print("Type 'menu' to list all commands.")
        logging.info("Application started. Type 'exit' to exit.")
        logging.info("Type 'menu' to list all commands.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                logging.info("Input: %s", cmd_input)
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)
                try:
                    if len(cmd_input.split(" ")) > 1:
                        split = cmd_input.split(" ")
                        self.command_handler.execute_command(split[0],list(filter(lambda x: not x.isspace(),split[1:])))
                    else:
                        self.command_handler.execute_command(cmd_input.strip())
                except KeyError:
                    logging.error("Unknown command: %s", cmd_input)
                    sys.exit(1)
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")
if __name__ == "__main__":
    app = App()
    app.start()
