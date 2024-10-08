# Write your solution here:

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < 23:
                    self.hours += 1
                else:
                    self.hours = 0

    def set(self, new_hours: int, new_minutes: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        
if __name__ == "__main__":
    clock = Clock(10, 10, 58)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)