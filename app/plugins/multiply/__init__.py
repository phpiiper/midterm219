#pylint: disable=duplicate-code
"""Command to Multiply"""
import logging
from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.save import SaveOperation

class MultiplyCommand(Command):
    """Performs the multiply operation"""
    def operation(self,a,b): #pylint: disable=invalid-name
        """Performs a given operation"""
        return a * b
    def reiterate_list(self,op_list):
        """Reiterates a list of nums to perform an operation"""
        result = op_list[0]
        while len(op_list) != 1:
            try:
                result = self.operation(result,op_list[1])
                op_list = op_list[1:]
            except: # pylint: disable=bare-except
                return InvalidOperation
        return result
    def execute(self,args): # pylint: disable=arguments-differ
        """Executes the function"""
        opname = "multiply"
        try:
            arg_list = list(map(Decimal, args))
            res = self.reiterate_list(arg_list)
            print(res)
            logging.info("Command '%s' executed with arguments: %s and returned value '%s'",opname,args,res)
            SaveOperation([opname,args])
        except InvalidOperation:
            print("Error: InvalidOperation")
            valid_list = list(filter(lambda x: x.isnumeric(), args))
            invalid_list = list(filter(lambda x: not x.isnumeric(), args))
            logging.error("Command '%s' Error - Invalid number input: %s does not include valid numbers.",opname,args)
            if len(valid_list) > 0:
                logging.error("Command '%s' Error - Valid numbers: %s",opname,valid_list)
            logging.error("Command '%s' Error: Invalid numbers: %s",opname,invalid_list)
        except Exception as e: # pylint: disable=broad-exception-caught
            print("Error: Exception - " + e)
            logging.error("Command '%s' Error: An error occurred: %s",opname,e)
