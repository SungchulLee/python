import random

event_list = ['데스크 1 빔', '데스크 2 빔', '데스크 3 빔', '손님', '손님', '손님', '손님', '손님', '손님', '손님']

q = []
d1 = []
d2 = []
d3 = []

print('대기열', q)
print('데스크 1', d1)
print('데스크 2', d2)
print('데스크 3', d3)
print()

current_queue_number = 100
for i in range(101,109+1):
    
    event = random.choice(event_list) 
    print('이벤트 발생 :', event)
    
    if event == '손님':
        
        current_queue_number = current_queue_number + 1
        q.append(f'대기번호 {current_queue_number}')
        
        if len(d1) == 0:
            popped_item = q.pop(0)
            d1 = [popped_item]
        elif len(d2) == 0:
            popped_item = q.pop(0)
            d2 = [popped_item]
        elif len(d3) == 0:
            popped_item = q.pop(0)
            d3 = [popped_item]
            
    elif event == '데스크 1 빔':
        d1 = []
        try:
            popped_item = q.pop(0)
            d1 = [popped_item]
        except:
            pass
        
    elif event == '데스크 2 빔':
        d2 = []
        try:
            popped_item = q.pop(0)
            d2 = [popped_item]
        except:
            pass
            
    elif event == '데스크 3 빔':
        d3 = []
        try:
            popped_item = q.pop(0)
            d3 = [popped_item]
        except:
            pass
    
    print('대기열', q)
    print('데스크 1', d1)
    print('데스크 2', d2)
    print('데스크 3', d3)
    print()