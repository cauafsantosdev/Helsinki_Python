# Write your solution here

class Task:
    task_id = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task.task_id += 1

        self.__description = description
        self.__workload = workload
        self.__programmer = programmer
        self.__is_finished = "NOT FINISHED"
        self.__id = Task.task_id

    @property
    def description(self):
        return self.__description
    
    @property
    def workload(self):
        return self.__workload
    
    @property
    def programmer(self):
        return self.__programmer
    
    @property
    def id(self):
        return self.__id

    def is_finished(self):
        if self.__is_finished == "NOT FINISHED":
            return False
        return True
    
    def mark_finished(self):
        self.__is_finished = "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {self.__is_finished}"
    

class OrderBook:
    def __init__(self):
        self.__orders = []

    def all_orders(self):
        return self.__orders
    
    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def add_order(self, description: str, programmer: str, workload: int):
        self.__orders.append(Task(description, programmer, workload))
    
    def programmers(self):
        return list(set(task.programmer for task in self.__orders))
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return True
        else:
            print("erroneous input")
        
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            print("erroneous input")
            return None
        else:
            finished_list = [task for task in self.finished_orders() if task.programmer == programmer]
            finished_tasks = len(finished_list)
            finished_workload = sum(task.workload for task in finished_list)
            
            unfinished_list = [task for task in self.unfinished_orders() if task.programmer == programmer]
            unfinished_tasks = len(unfinished_list)
            unfinished_workload = sum(task.workload for task in unfinished_list)

            return (finished_tasks, unfinished_tasks, finished_workload, unfinished_workload)


class OrderBookApplication:
    def __init__(self):
        self.__order_book = OrderBook()

    def add_order(self):
        try:
            description = input("description: ")
            data = input("programmer and workload estimate: ").split()
            programmer = data[0]
            workload = int(data[1])

            self.__order_book.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")

    def finished_id(self):
        try:
            task_id = input("id: ")
            task_id = int(task_id)

            if self.__order_book.mark_finished(task_id):
                print("marked as finished")
        except:
            print("erroneous input")

    def search_programmer(self):
        programmer = input("programmer: ")
        status = self.__order_book.status_of_programmer(programmer)

        if status != None:
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def menu(self):
        print("""commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer""")
        
    def execute(self):
        self.menu()

        while True:
            option = int(input("\ncommand: "))

            if option == 0:
                break

            elif option == 1:
                self.add_order()

            elif option == 2:
                finished = self.__order_book.finished_orders()

                if len(finished) == 0:
                    print("no finished tasks")
                
                for order in finished:
                    print(order)

            elif option == 3:
                unfinished = self.__order_book.unfinished_orders()
                
                for order in unfinished:
                    print(order)

            elif option == 4:
                self.finished_id()

            elif option == 5:
                programmers = self.__order_book.programmers()

                for programmer in programmers:
                    print(programmer)
            
            elif option == 6:
                self.search_programmer()


app = OrderBookApplication()
app.execute()