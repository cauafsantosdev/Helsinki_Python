# Write your solution here:

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
                break
        else:
            raise ValueError ("id not found")
        
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError ("programmer not found")

        finished_list = [task for task in self.finished_orders() if task.programmer == programmer]
        finished_tasks = len(finished_list)
        finished_workload = sum(task.workload for task in finished_list)
        
        unfinished_list = [task for task in self.unfinished_orders() if task.programmer == programmer]
        unfinished_tasks = len(unfinished_list)
        unfinished_workload = sum(task.workload for task in unfinished_list)

        return (finished_tasks, unfinished_tasks, finished_workload, unfinished_workload)


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)