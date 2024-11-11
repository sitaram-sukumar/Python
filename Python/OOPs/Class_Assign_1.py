from MaxSizeList import MaxSizeCustomList as MCL;

a = MCL(3);
b = MCL(1);
a.push('hey');
a.push('hi');
a.push("let's");
a.push('go');

b.push('hey');
b.push('hi');
b.push("let's");
b.push('go');

print(a.get_lst());
print(b.get_lst());
