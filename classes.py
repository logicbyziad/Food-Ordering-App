class otlob_app:

    def __init__(self):
        self.admins = {}
        self.customers = {}
        self.sellers = {}

class user:
    users_counter = 0

    def __init__(self, username):
        self.username = username
        user_counter += 1

    def report(self):
        pass


class admin(user):
    admin_counter = 0

    def __init__(self):
        admin_counter += 1
        pass

    def report(self):
        pass
    
    def add(self, username, type, app):        
        
        if (type == "customer"):
            if (username in app.customers):
                return -1
            else:
                new_user = customer(username)
                app.customers[username] = new_user

        elif(type == "seller"):
            if (username in app.sellers):
                return -1
            else:    
                new_user = seller(username)
                app.sellers[username] = new_user
        else:
            return 1
        
    def remove(self, username, type, app):        
        
        if (type == "customer"):
            if (username not in app.customers):
                return -1
            else:
                del app.customers[username]

        elif(type == "seller"):
            if (username not in app.sellers):
                return -1
            else:    
                del app.sellers[username]

        else:
            return 1

    ## Todo: Complete Edit Function    
    def edit(self):
        pass




class customer(user):

    def __init__(self):
        self.active_orders = []
        self.previous_orders = []
        self.address = ""

    def report(self):
        pass


class seller(user):

    def __init__(self):
        self.products = []

    def report(self):
        pass


class order:

    def __init__(self):
        self.id = 0
        self.products = []
        self.active = False
        self.date = ""
        self.customer_address = ""
        self.customer_id = 0


class product:

    pass

###################################################################

myapp = otlob_app()
