import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creatingdirectory.'+directory)

createFolder("/Users/kyungjunkim/Downloads/ICN_LAX/2003")


#---------2004 -> 2003-----------#
ex_file_path = "/Users/kyungjunkim/Downloads/ICN_LAX/2003"
file_path = "/Users/kyungjunkim/Downloads/ICN_LAX/2004"
file_names = os.listdir(file_path)
for name in file_names:
    if len(name) == 20:
        src = os.path.join(file_path, name)
        name = name[:10] + "2003" + name[14:]
        dst = os.path.join(file_path, name)
        os.rename(src, dst)
        shutil.move(dst, ex_file_path)
    elif len(name) == 21:
        if int(name[15:17]) <= 31:
            src = os.path.join(file_path, name)
            name = name[:10] + "2003" + name[14:]
            dst = os.path.join(file_path, name)
            os.rename(src, dst)
            shutil.move(dst, ex_file_path)

#------------2005 -> 2004------------#
ex_file_path = "/Users/kyungjunkim/Downloads/ICN_LAX/2004"
file_path = "/Users/kyungjunkim/Downloads/ICN_LAX/2005"
file_names = os.listdir(file_path)
for name in file_names:
    if len(name) == 20:
        src = os.path.join(file_path, name)
        name = name[:10] + "2004" + name[14:]
        dst = os.path.join(file_path, name)
        os.rename(src, dst)
        shutil.move(dst, ex_file_path)
    elif len(name) == 21:
        if int(name[15:17]) <= 31:
            src = os.path.join(file_path, name)
            name = name[:10] + "2004" + name[14:]
            dst = os.path.join(file_path, name)
            os.rename(src, dst)
            shutil.move(dst, ex_file_path)


