class TextView():
    
    def __init__(self) -> None:
        pass
    
    def start(cls) -> str:
        return input('what would you like to do? (list, add, update, delete)')
    
    def error(cls, error,err_input=None):
        match error:
            case 'unmatch':
                print(f'{err_input} does not match expected input')
                
    def list_objective(cls) -> dict:
        list_objective=input('countries, country or city? ').lower().strip().split(' ')
        match list_objective[0]:
            case 'countries':
                return {}
            case 'country':
                return {'country':list_objective[1]} 
            case 'city':
                return {'city':list_objective[1]} 
        return list_objective