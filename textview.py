class TextView():
    
    def __init__(self) -> None:
        pass
    def start(cls) -> str:
        return input('what would you like to do? (list, add, update, delete)')
    def error(cls, error,err_input=None):
        match error:
            case 'unmatch':
                print(f'{err_input} does not match expected input')