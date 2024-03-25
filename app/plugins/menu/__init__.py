from app.commands import Command
import logging
import os
import pkgutil


class MenuCommand(Command):
    def getList(self):
        arr = []
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    arr.append(plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")
        return arr
    def execute(self):
        commands = self.getList()
        string = "\n"

        string += '-----------------\n'
        string += 'List of Commands: \n'
        for command in commands:
            string += " > " + command + "\n"
        string += f'-----------------'
        print(string)
        logging.info(string)