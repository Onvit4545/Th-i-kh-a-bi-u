from datetime import datetime

class Event:
    def __init__(self,title,start_time,end_time):
        
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
    def duration(self):
        duration = self.end_time-self.start_time
        return duration
    def notify(self):
        if datetime.now() < self.start_time:
            return 'Sắp bắt đầu'
        elif datetime.now() > self.end_time:
            return 'Hết Hạn'
        else:
            return 'Đang diễn ra'
class Lich:     
    def __init__(self):
        self.event_list=[]
    def add_event(self,event):
        if self.event_list ==[]:
                self.event_list.append(event)
        else:
            for i in self.event_list:         
                if i.start_time <= event.end_time or i.end_time <= event.start_time:
                    print(f'Sự kiện {event.title} bị trùng')
                    continue
                    
                else:
                    self.event_list.append(event)

    def show_event(self):
        return self.event_list

lich=Lich()
event1 = Event('gi1do',datetime(2025, 6, 12, 14, 30),datetime(2025, 6, 16, 15, 20))
event2 = Event('gi2do',datetime(2025, 6, 12, 14, 30),datetime(2025, 6, 16, 15, 20))

lich.add_event(event1)
lich.add_event(event2)
for i in lich.show_event():  
    print(i.notify())
