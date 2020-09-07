import os
import shutil
import time
from multiprocessing import Process


# tt = time.time()
# def run(count_num):
n = 0
while True:
    if n == 1:
        break
    for i in range(1, 9):
        print(i, n)
        i = str(i)
        path_xml = "D:\\img_" + i
        filelist = os.listdir(path_xml)
        path = "D:\\img_" + i + "\\"
        img = "D:\\openpose\\img_" + i + "\\"

        # tt = time.time()
        # s = time.localtime(tt)
        # t = str(s.tm_year) + str(s.tm_mon).zfill(2) + str(s.tm_mday) + str(s.tm_hour) + str(s.tm_min)
        # t = '202007201105'

        for files in filelist[:300]:
            name = os.path.splitext(files)[0]
            hz = os.path.splitext(files)[1]
            # print(name[0:14],type(name))
            if hz == '.jpg':
                copy_img = path + name + '.jpg'
                new_img = img + name + '.jpg'
                shutil.move(copy_img, new_img)
        os.chdir("D:\\openpose")

        a1 = 'openposedemo.exe --render_pose 0 --display 0 --image_dir img_' + i + ' --write_json out_' + i
        # a2 = 'bin\openposedemo.exe --render_pose 0 --display 0 --image_dir img_8 --write_json out_8'
        # openposedemo.exe --image_dir 1 --write_json 1_out --display 0 --render_pose 0

        os.system(a1)

        dir = "D:\\openpose\\img_" + i
        shutil.rmtree(dir)
        os.mkdir(dir)
    n += 1


# if __name__ == '__main__':
#     p1 = Process(target=run, args=(1,))
#     # p2 = Process(target=run, args=(3,))
#     p3 = Process(target=run, args=(5,))
#     # p4 = Process(target=run, args=(7,))
#     s = time.time()
#     p1.start()
#     # p2.start()
#     p3.start()
#     # p4.start()
#     p1.join()
#     # p2.join()
#     p3.join()
#     # p4.join()
#     print('~~~~~~~~~~~~~~~~')
#     e = time.time()
#     print(e-s)
# ss = time.time()
# print(ss-tt)




