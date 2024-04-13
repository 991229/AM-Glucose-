# systolic_peak
if train.iloc[i, 1] > train.iloc[i-10, 1] and train.iloc[i, 1] > train.iloc[i+10, 1] and train.iloc[i, 1] > train.iloc[i+5, 1] and train.iloc[i, 1] > train.iloc[i-5, 1] and train.iloc[i, 1] > train.iloc[i+1, 1] and train.iloc[i, 1] > train.iloc[i-1, 1]:
    systolic_peak_row = i
    systolic_peak_value = train.iloc[i, 1]  
    if bottom_row != 0 and  0 < (systolic_peak_row - bottom_row) < 15:
        #print("i:", systolic_peak_row, " ", bottom_row-systolic_peak_row, " ", "s_peak_value:", train.iloc[i, 1]-bottom_value, "Peak:", train.iloc[i, 1], "bottom:", bottom_value)
        systolic_peak.append(train.iloc[i, 1] - bottom_value)
        systolic_peak_ratio.append((train.iloc[i, 1] - bottom_value)/bottom_value)
        cofficient_rise.append((systolic_peak_value-bottom_value)/(systolic_peak_row-bottom_row)) 
    #print("sys_row:", systolic_peak_row)
    #print("bottom_row:", bottom_row)
    
# dicrotic_notc
if train.iloc[i, 1] < train.iloc[i-6, 1] and train.iloc[i, 1] < train.iloc[i+6, 1] and train.iloc[i, 1] > train.iloc[i+12, 1]:
    if bottom_row != 0 and  10 < (i - bottom_row) < 30:
        dicrotic_notch.append(train.iloc[i, 1] - bottom_value)
        dicrotic_notch_ratio.append((train.iloc[i, 1] - bottom_value)/bottom_value)
    
# diastolic_peak
if train.iloc[i, 1] > train.iloc[i+10, 1] and train.iloc[i, 1] > train.iloc[i-5, 1] and train.iloc[i, 1] < train.iloc[i-12, 1] and train.iloc[i, 1] > train.iloc[i+1, 1] and train.iloc[i, 1] > train.iloc[i-1, 1]:
    if bottom_row != 0 and  15 < (i - bottom_row) < 30:
        diastolic_peak.append(train.iloc[i, 1] - bottom_value)
        diastolic_peak_ratio.append((train.iloc[i, 1] - bottom_value)/bottom_value)
        #print("i:", i, " ", bottom_row-i, " ", "d_peak:", train.iloc[i, 1]-bottom_value)
    diastolic_peak_row = i
    if systolic_peak_row != 0: #and diastolic_peak_row - systolic_peak_row :
        DEIT.append(diastolic_peak_row - systolic_peak_row)  # DEIT = 收缩峰到舒张峰的时长
    
#bottom
if train.iloc[i, 1] < train.iloc[i-15, 1] and train.iloc[i, 1] < train.iloc[i+15, 1] and train.iloc[i, 1] < train.iloc[i+1, 1] and train.iloc[i, 1] < train.iloc[i-1, 1] and train.iloc[i, 1] < train.iloc[i+3, 1] and train.iloc[i, 1] < train.iloc[i-3, 1]:
    bottom.append(train.iloc[i, 1])
    #print("i:", i, " ", bottom_row-i, " ", "d_peak:", train.iloc[i, 1])
    if i-bottom_row > 25:
        pulse_width.append((i - bottom_row)) 
    bottom_row = i
    bottom_value = train.iloc[i, 1]
    if systolic_peak_row != 0 and (bottom_row-systolic_peak_row) < 40:
        cofficient_decline.append((bottom_value-systolic_peak_value)/(bottom_row-systolic_peak_row)) 



systolic_peak_value = mean(systolic_peak)*1E-5
diastolic_peak_value = mean(diastolic_peak)*1E-5
dicrotic_notch_value = mean(dicrotic_notch)*1E-5
bottom_value = mean(bottom)
cofficient_decline_value = mean(cofficient_decline)*1E-5
cofficient_rise_value = mean(cofficient_rise)*1E-5
pulse_width_value = mean(pulse_width)
DEIT_value = mean(DEIT)
glucose_feature = [systolic_peak_value, (-1)*mean(systolic_peak_ratio), diastolic_peak_value, (-1)*mean(diastolic_peak_ratio), dicrotic_notch_value, (-1)*mean(dicrotic_notch_ratio), (-1)*bottom_value, cofficient_decline_value, cofficient_rise_value, pulse_width_value, DEIT_value]
49608e-07, 7.034268239496963e-08, 6.166454970578142e-08, -2.960737312207584e-06, -4.443200467156757e-09, 1.5841253689241132e-08, 34.125, 13.263157894736842]

