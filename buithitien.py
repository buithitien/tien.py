def chucnang5():
   n=int(input('Nhập tổng số môn học:'))
   diem= []
   heso= []
   def nhapdiem(n):
       for i in range(1,n+1):
           print('Điểm môn thứ',i,'là:')
           diem.append(float(input()))
           print('Hệ số thứ',i,'là:')
           heso.append(float(input()))
   def tinhdiem(diem,heso):
       tong=0
       t=0
       print('Tổng số môn là:',n)
       for i in range(0,n):
           tong=tong+diem[i]*heso[i]
           t+=heso[i]
       print('Tổng hệ số của',n,'môn là:',t)
       print('Điểm trung bình của',n,' môn  là:',(tong/t))
   nhapdiem(n)
   tinhdiem(diem,heso)
chucnang5()
