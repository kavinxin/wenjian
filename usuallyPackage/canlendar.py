import calendar
cal=calendar.calendar(2018,w=0,l=1,c=0);
print(cal);
print(calendar.isleap(2019));
print(calendar.leapdays(1984,2018));
print(help(calendar.leapdays));
print(calendar.month(2018,9));
w,k=calendar.monthrange(2018,9);
print(w);
print(k);
print(help(calendar._locale));
calendar.prcal(2018);
calendar.prmonth(2018,3);
print(calendar.prweek(2018,9,16));