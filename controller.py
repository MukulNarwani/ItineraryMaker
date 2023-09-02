

#cliController
class controller():
    
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.start_app()

    def start_app(cls) -> None:
        while(input("Quit? (y/n) ") =='n' ):
            event=cls.view.start()
            match event:
                case 'list':
                    cls.list_handler()
                case 'add':
                    cls.add_handler()
                case 'update':
                    cls.update_handler()
                case 'delete':
                    cls.delete_handler()
                case _:
                    cls.view.error('unmatch',event)
    def list_handler(cls):
        try:
            list_obj=cls.view.list_objective()
        except:
            cls.view.error('unmatch',list_obj)
            pass
        cls.model.list_handler(**list_obj)
    def add_handler(cls):
        cls.model.add_handler()
    def update_handler(cls):
        cls.model.update_handler()
    def delete_handler(cls):
        cls.model.delete_handler()
#Netcontroller


from . import model,view,textview
