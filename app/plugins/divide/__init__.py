import logging
from app.commands import Command
from app.save import SaveOperation
from decimal import Decimal, InvalidOperation

class DivideCommand(Command):
    def operation(self,a,b):
        return a / b
    def reiterateList(self,list):
        result = list[0]
        while len(list) != 1:
            result = self.operation(result,list[1])
            list = list[1:]
        return result
    def execute(self,args):
        opname = "divide"
        try:
            argList = list(map(Decimal, args))
            res = self.reiterateList(argList)
            print(res)
            logging.info("Command \'" + opname + "\' executed with arguments: " + str(args) + " and returned value \"" + str(res) + "\"")
            SaveOperation([opname,args])
        except InvalidOperation:
            print(f"Error: InvalidOperation")
            validList = list(filter(lambda x: x.isnumeric(), args))
            invalidList = list(filter(lambda x: not x.isnumeric(), args))
            logging.error(f"Command '{opname}' Error - Invalid number input: {args} does not include valid numbers.")
            if len(validList) > 0:
                logging.error(f"Command '{opname}' Error - Valid numbers: {validList}")
            logging.error(f"Command '{opname}' Error: Invalid numbers: {invalidList}")
        except ZeroDivisionError:
            print(f"Error: ZeroDivisionError")
            logging.error(f"Command '{opname}' Error: Division by zero.")
        except Exception as e:
            print(f"Error: Exception - {e}")
            logging.error(f"Command '{opname}' Error: An error occurred: {e}")

