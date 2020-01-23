import os

os.chdir(r'E:\Desktop\SERIES\RAISING DION S01')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_name = f_name[15:]
#    f_season, f_no, f_names = f_name.split(' ')
#    f_no = f_no[4:]
    nf = '{}{}'.format(f_name, f_ext)
    os.rename(f, nf)
