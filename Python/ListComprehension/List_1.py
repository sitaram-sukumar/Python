temps = [230, 734, 153, 683, 373];
new_temp = [t/10 for t in temps if t>400];
print(new_temp);

new_temp1 = [t/10 if t>400 else 0 for t in temps]
print(new_temp1);