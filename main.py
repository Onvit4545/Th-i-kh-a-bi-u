from datetime import datetime
from win10toast import ToastNotifier
import pandas as pd
toaster = ToastNotifier()

class Event:
    def __init__(self,title,start_time,end_time,typeh):
        
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.typeh = typeh
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
    def check(self):
        if self.start_time < datetime.now():
            return True
class Lich:     
    def __init__(self):
        self.event_list=[]
    def add_event(self,event):
        
        if self.event_list ==[]:
            self.event_list.append(event)
        else:
            print(event.typeh)
            if event.typeh =='hẹn':
                for i in range(len(self.event_list)):    
                    if self.event_list[i].start_time == event.start_time:
                        print(f'Hẹn {event.title} bị trùng')        
    
                    else:
                        self.event_list.append(event)
                    
            else:

                for i in self.event_list:    
                        
                    if i.start_time <= event.end_time or i.end_time >= event.start_time:
                        print(f'Sự kiện {event.title} bị trùng')
                        continue
                        
                    else:
                        self.event_list.append(event)

    def show_event(self):
        return self.event_list
    def delete_event(self):
        self.event_list.pop(0)

lich=Lich()
df = pd.read_csv('du_lieu.csv')
for i in range(len(df)):
    tg=df['Time'][i].split(':')
    
    event = Event(df['Title'][i],datetime(2025,int(df['Month'][i]),int(df['Day'][i]),int(tg[0]),int(tg[1])),datetime(2025,int(df['Month'][i]),int(df['Day'][i]),int(tg[0]),int(tg[1])),'hẹn')
    lich.add_event(event)
def nhap(dong_moi):
    type_event = input('Mời bạn nhập loại thông báo:').lower()
    title =input('Nhập tiêu đề:')
    if title =='x':
        return 'x'
    ngay = int(input('Nhập ngày:'))
    thang =int(input('Nhập tháng:'))
    
    tg =input('Nhập thời gian (dấu":") :')
    dong_moi.loc[len(dong_moi)] = [title,thang,ngay,tg,type_event]
    tg=tg.split(':')
    event = Event(title,datetime(2025,thang,ngay,int(tg[0]),int(tg[1])),datetime(2025,thang,ngay,int(tg[0]),int(tg[1])),type_event)
    lich.add_event(event)
    
    return dong_moi


dong_moi = pd.DataFrame(columns=['Title','Month','Day','Time','Type'])

dong_moi1=pd.DataFrame(columns=['Title','Month','Day','Time','Type'])


while True:
    dong_moi = nhap(dong_moi)
    
    if isinstance(dong_moi,pd.DataFrame)==False:
        df = pd.concat([df, dong_moi1], ignore_index=True)
        break
    dong_moi1=dong_moi

while True:
    try:
        
        if lich.show_event()[0].check():
            toaster.show_toast("Thông báo", lich.show_event()[0].title, duration=5)
            lich.delete_event()
            df = df.drop(0).reset_index(drop=True)
        print(1)
    except:
        print('Không còn đặt hẹn')

        break
    df.to_csv("du_lieu.csv", index=False)



 
