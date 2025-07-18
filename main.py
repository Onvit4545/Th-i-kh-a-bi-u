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
        
        if isinstance(self.start_time, str):
            self.start_time = datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")

        
        return self.start_time < datetime.now()

class Lich:     
    def __init__(self):
        self.event_list=[0]
    def add_event(self,event):
        
        typeh = event.typeh
        
        if self.event_list ==[] or self.event_list[len(self.event_list)-1]==0:
            if typeh=='hẹn':
                self.event_list.insert(0,event)
            else:
                self.event_list.append(event)
        else:
            a=True
            if typeh =='hẹn':
                for i in range(len(self.event_list)):    
                    if self.event_list[i]==0:
                        break
                    if self.event_list[i].start_time == event.start_time:
                        print(f'Hẹn {event.title} bị trùng')     
                        return False
                
                
                self.event_list.insert(0,event)
                        
                    
            else:

                for i in range(len(self.event_list)-1,0,-1):  
                    
                    if self.event_list[i]==0:
                        break
                    if event.start_time <= self.event_list[i].end_time or event.end_time >= self.event_list[i].start_time:
                        print(f'Sự kiện {event.title} bị trùng')
                        return False
                        
                self.event_list.append(event)
        
        
        return True
    def show_event(self):
        return self.event_list
    def delete_event(self):
        self.event_list.pop(0)

lich=Lich()
df = pd.read_csv('du_lieu.csv')
for i in range(len(df)):
    event = Event(df['Title'][i],df['Start'][i],df['End'][i],df['Type'][i])
    lich.add_event(event)
def nhap(dong_moi):
    type_event = input('Mời bạn nhập loại thông báo:').lower()
    title =input('Nhập tiêu đề:')
    if title =='x':
        return 'x'
    ngay = int(input('Nhập ngày bắt đầu:'))
    thang =int(input('Nhập tháng bắt đầu:'))
    tg =input('Nhập thời gian bắt đầu (dấu":"):').split(':')
    if type_event=='sự kiện':
        ngay1 = int(input('Nhập ngày kết thúc:'))
        thang1 =int(input('Nhập tháng kết thúc:'))
        tg1 =input('Nhập thời gian kết thúc (dấu":") :').split(':')
        date2=datetime(2025,ngay1,thang1,int(tg1[0]),int(tg1[1]))
        
    
    date1=datetime(2025,thang,ngay,int(tg[0]),int(tg[1]))
    date2=''
    if type_event=='sự kiện':
        date2=datetime(2025,thang,ngay,int(tg[0]),int(tg[1]))
    event = Event(title,date1,date2,type_event)
    

    a=lich.add_event(event)
    if a:
        dong_moi.loc[len(dong_moi)] = [title,date1,date2,type_event]
    return dong_moi


dong_moi = pd.DataFrame(columns=['Title','Start','End','Type'])

dong_moi1 = pd.DataFrame(columns=['Title','Start','End','Type'])


while True:
    dong_moi = nhap(dong_moi)
    
    if isinstance(dong_moi,pd.DataFrame)==False:
        df = pd.concat([df, dong_moi1], ignore_index=True)
        break
    dong_moi1=dong_moi
df.to_csv("du_lieu.csv", index=False)
while True:
    print(lich.show_event()[0].check())
    try:     
        if lich.show_event()[0].check():
            toaster.show_toast("Thông báo", lich.show_event()[0].title, duration=5)
            lich.delete_event()
            df = df.drop(0).reset_index(drop=True)
            df.to_csv("du_lieu.csv", index=False)


        
    except:
        print('Không còn đặt hẹn')
        df.to_csv("du_lieu.csv", index=False)

        break
    



 
