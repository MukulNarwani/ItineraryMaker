

#cliController
class controller():
    
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.start_app()

    def start_app(cls):
        # event=cls.view.start()
        # if event == 'add':
        #     cls.view.add
        # elif event=='edit':
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
    def list_handler():
        pass
    def add_handler():
        pass
    def update_handler():
        pass
    def delete_handler():
        pass
#Netcontroller


from . import model,view,textview
