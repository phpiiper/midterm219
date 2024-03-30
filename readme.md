# Python Calculator

## Project Submission

### .env configurations
* ENVIRONMENT 

Type of environment program is run in

* LOGGING 

The level of logging to appear on the console

* LOGGINGPATH 

The log save file path

* LOGGINGCONF 

The log config file path to look for

* DATACOLUMNS 

The CSV save file columns

* HISTORYFILENAME 

The history save file path

* DATADIRNAME 

The save folder file path

### Design Patterns Utilized

* [Facade Pattern](app/__init__.py)

The App class is utilized to be the between point of the user and the code/execution.

* [Command Patterns](app/plugins)

The plugins folder contains commands that are dynamically loaded in for the user to use in the REPL.

* [Factory Method / Strategy Patterns](app/plugins)

The basic arithmetic functions (add, subtract, divide, multiply) are all based on each other. In general, all of the plugins use the Commmand class as a basis as the design.

* [Singleton](app/__init__.py)

The App class was changed to make sure that only one can be instantiated at a time whenever it is called.

### Environment Variables
[View .env](.env)

Environment variables were used to easily customize parts of the program. For example, the level of logging and the file location of it can be customized.

### Logging Examples

[View Logs](logs/logs.log)

Logs were used to show how the program ran, and to spot any errors. Depending on the level, the logs would print accordingly.

### LBYL & EAFP

[Try/Catch - EAFP](app/plugins/divide/__init__.py)

The divide command attempts to divide numbers, however ensures that a proper handling of all possible cases (with except), to make sure the program can still run as intended.

[If/Else - LBYL](app/__init__.py)

The REPL utilized uses two different strucures to execute commands, in which either one or two inputs are valid. The operations use two (one for operation name and the other for the values) while the other commands use one (just the name). It first figures out which type it is based on its input.

### Demo Video
[Demo Video](Project.mp4)

