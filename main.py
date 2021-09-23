total_mins = input()

# Changes Visual Clock
def clock(minute, hr, cur_time, total_seq):
    for i in range (int(total_mins) + 1):
        cur_time = ''
        
        if minute == 60:
            
            if hr == 12:
                hr = 1
            else:
                hr += 1
            cur_time = str(hr) + '00'
            
            if check_seq(cur_time, hr):
                total_seq += 1
            
            minute = 0
        elif (minute >= 0 and minute <= 9):
            cur_time = str(hr) + '0' + str(minute)
            
            if check_seq(cur_time, hr):
                total_seq += 1
            
            minute += 1
        else:
            cur_time = str(hr) + str(minute)
            
            if check_seq(cur_time, hr):
                total_seq += 1
            
            minute += 1
    return total_seq

# Checks If Arthimetic Sequence
def check_seq(cur_time, hr):
    dif_2_1 = int(cur_time[2]) - int(cur_time[1])
    dif_1_0 = int(cur_time[1]) - int(cur_time[0])
    if hr >= 1 and hr <= 9:
        if (dif_2_1 == dif_1_0):
            return True
        else:
            return False
    else:
        dif_3_2 = int(cur_time[3]) - int(cur_time[2])
        if (dif_3_2 == dif_2_1 == dif_1_0):
            return True
        else:
            return False

# Begin With and Print
print(clock(0, 12, '', 0))