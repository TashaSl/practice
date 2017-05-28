'''
Given six real numbers – a, b, c, d, e, f. Solve the following system of linear equations:
a*x + b*y = e
c*x + d*y = f
Output format
If the system has no solution, then the program should print a single number 0.
If the system has infinitely many solutions, each of which looks like y=kx+b, then the program should print the number 1, and then the values k and b.
If the system has a single solution (x0, y0), then the program should print the number 2, and then the values x0 and y0.
If the system has infinitely many solutions that look like x=x0 with any y, then the program should output the number 3, and then the value x0.
If the system has infinitely many solutions that look like y=y0 with any x, then the program should output the number 4, and then the value y0.
If any pair of numbers (x,y) is a solution, the program should output the number 5.
'''
a, b, c, d, e, f = list(map(lambda x: float(input()), range(6)))
arr = ['5' if (a,b,c,d,e,f) == (0,0,0,0,0,0) else None,
       '4 '+str(e/b) if (a,c,d,f) == (0,0,0,0) and b!=0 else None,
       '4 '+str(f/d) if (a,b,c,e) == (0,0,0,0) and d!=0 else None,
       '3 '+str(e/a) if (b,c,d,f) == (0,0,0,0) and a!=0 else None,
       '3 '+str(f/c) if (a,b,d,e) == (0,0,0,0) and c!=0 else None,
       '1 '+str(-a/b)+' '+str(e/b) if (c,d,f) == (0,0,0) and a!=0 and b!=0 else None,
       '1 '+str(-c/d)+' '+str(f/d) if (a,b,e) == (0,0,0) and c!=0 and d!=0 else None,
       '4 '+str(e/b) if (a,c) == (0,0) and b!=0 and d!=0 and e/b == f/d else None,
       '3 '+str(e/a) if (b,d) == (0,0) and a!=0 and c!=0 and e/a == f/c else None,
       '2 '+str(e/a) + ' '+str(f/d) if (b,c) == (0,0) and a!=0 and d!=0 else None,
       '2 '+str(f/c) + ' '+str(e/b) if (a,d) == (0,0) and c!=0 and b!=0 else None,
       '2 '+str((f - d*e/b)/c)+' '+str(e/b) if a == 0 and b!=0 and c!=0 and d!=0 else None,
       '2 '+str(e/a)+' '+str((f-c*e/a)/d) if b==0 and a!=0 and c!=0 and d!=0 else None,
       '2 '+str((e - b*f/d)/a)+' '+str(f/d) if c == 0 and a!=0 and b!=0 and d!=0 else None,
       '2 '+str(f/c)+' '+str((e-a*f/c)/b) if d==0 and a!=0 and b!=0 and c!=0 else None,
       '1 '+str(-a/b)+' '+str(e/b) if a!=0 and b!=0 and c!=0 and d!=0 and a*d-b*c == 0 and a*f-c*e == 0 else None,
       '2 '+str((e-b*(a*f-c*e)/(a*d-b*c))/a)+' '+str((a*f-c*e)/(a*d-b*c)) if a!=0 and
       b!=0 and c!=0 and d!=0 and a*d-b*c != 0 else None]
result = list(filter(lambda x: x, arr))
print(result[0]) if result else print(0)
