from BFS_Sudoku import BFS_solve

print ("\nEnter values for Sudoku 6x6 grid in this format (enter 0 if the space is blank):")
print ("\n[x1,x2,x3,x4,x5,x6]\n[x7,x8,x9,x10,x11,x12]\n[x13,x14,x15,x16,x17,x18]\n[x19,x20,x21,x22,x23,x24]\n[x25,x26,x27,x28,x29,x30]\n[x31,x32,x33,x34,x35,x36]")
      
x1 = int(input("\nenter x1: "))
x2 = int(input("enter x2: "))
x3 = int(input("enter x3: "))
x4 = int(input("enter x4: "))
x5 = int(input("enter x5: "))
x6 = int(input("enter x6: "))
x7 = int(input("enter x7: "))
x8 = int(input("enter x8: "))
x9 = int(input("enter x9: "))
x10 = int(input("enter x10: "))
x11 = int(input("enter x11: "))
x12 = int(input("enter x12: "))
x13 = int(input("enter x13: "))
x14 = int(input("enter x14: "))
x15 = int(input("enter x15: "))
x16 = int(input("enter x16: "))
x17 = int(input("enter x17: "))
x18 = int(input("enter x18: "))
x19 = int(input("enter x19: "))
x20 = int(input("enter x20: "))
x21 = int(input("enter x21: "))
x22 = int(input("enter x22: "))
x23 = int(input("enter x23: "))
x24 = int(input("enter x24: "))
x25 = int(input("enter x25: "))
x26 = int(input("enter x26: "))
x27 = int(input("enter x27: "))
x28 = int(input("enter x28: "))
x29 = int(input("enter x29: "))
x30 = int(input("enter x30: "))
x31 = int(input("enter x31: "))
x32 = int(input("enter x32: "))
x33 = int(input("enter x33: "))
x34 = int(input("enter x34: "))
x35 = int(input("enter x35: "))
x36 = int(input("enter x36: "))

gridSolve = [[x1,x2,x3,x4,x5,x6],
      [x7,x8,x9,x10,x11,x12],
      [x13,x14,x15,x16,x17,x18],
      [x19,x20,x21,x22,x23,x24],
      [x25,x26,x27,x28,x29,x30],
      [x31,x32,x33,x34,x35,x36]]

for row in gridSolve:
      print (row)

BFS_solve(gridSolve)