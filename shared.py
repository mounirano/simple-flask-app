from flask_restful import reqparse

args_error_messages = {
    "str": "this field cannot be empty and it must be a string!",
    "int": "this field cannot be empty and it must be a integer!"
}


def get_help_message_by_type(arg_type: str, required: bool):
    if required:
        return args_error_messages[arg_type]


def create_parser(arguments):
    parser = reqparse.RequestParser()
    for arg in arguments:
        arg['help'] = get_help_message_by_type(arg['type'].__name__, arg['required'])
        if arg['type'].__name__ == 'dict':
            parser.add_argument(
                arg['name'],
                type=arg['type'],
                required=arg['required'],
                help=arg['help'],
                action="append"
            )
        else:
            parser.add_argument(arg['name'], type=arg['type'], required=arg['required'], help=arg['help'])
    return parser
