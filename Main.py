import os
current_desitination = os.getcwd()  # if not defined , will create folders in current location
filename = 'fold_list.txt'
container =[]
def read_level_name(filename,container):
    temp_folder_level_name=[]
    with open(filename,'r',encoding='utf-8') as f :
        lines =f.readlines()
        current_level=0
        for line in lines:
            current_address =os.getcwd()
            level =line.count('\t')
            name =line.split('\t')[-1].strip('\n')
            try:
                temp_folder_level_name[level]=name
            except  :
                temp_folder_level_name.append(name)
            s='\\'
            if level==0:
                foldername=name
            else :
                foldername=s.join(temp_folder_level_name[:level])+'\\'+name
            container.append(foldername)

def create_folder(container):
    for folder in container:
        try:
            os.mkdir(folder)
        except :
            print("folder {} existing".format(folder))
def run():
    read_level_name(filename,container)
    create_folder(container)
if __name__ == "__main__":
    print("默认文件列表.txt文件 和 目标文件夹存放地址与当前脚本文件地址相同")
    change_or_not = input("更改输入文件列表和 目标文件夹的地址 ？ Y or N :")
    if change_or_not.upper() == "Y":
        destination_folder = input ("目标文件夹存放地址 ，拷贝完整路径 ：")
        current_destination =os.chdir(destination_folder)
        filename = input("输入文件夹列表， .txt 文件,包含文件名称 ：拷贝完整路径 ：")
    run()
    print("文件夹已经创建")
    input ("按任意键退出")
    
