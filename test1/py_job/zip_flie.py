
import  os
import zipfile

'''解压文件'''
# def zip_to_file(zip_file,target_file):
#     with zipfile.ZipFile(zip_file,"r") as zpfile:
#         for file in zpfile.namelist():
#             zpfile.extract(file,target_file)

# zip_to_file("a4f2279c-9fd6-40ed-a3f9-a8cc47f17c14.zip","信")

'''解压文件夹下的多个压缩文件'''
# def file_zip_file(file):
#     for files in os.listdir(file):
#         print(files)
#         if files.split('.')[1]=='zip':
#             zip_file=zipfile.ZipFile(files)
#             for file_zip in zip_file.namelist():
#                 target_file=file.split('.')[0]
#                 zip_file.extract(file_zip,target_file)
#         else:
#             continue
#
# file_zip_file("22222")


def file_to_zip(dir_path):
    with zipfile.ZipFile(dir_path+".zip","w",zipfile.ZIP_DEFLATED) as wfile:
        for files ,undiir_file,two_files in os.walk(dir_path):
            for file in two_files:
                fpath=os.path.join(files,file)
                wfile.write(fpath)

# file_to_zip("22222")


aa='afagag.aaeee'
print(aa.split('.')[-1])

