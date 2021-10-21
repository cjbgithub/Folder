# -*- coding:utf-8 -*-
import os
import time
import shutil
import getpass
import subprocess


def get_revision_set(revision_set):
    """ 获取对应历史记录 """
    set_add = set()

    set_mod = set()
    set_del = set()
    for version in revision_set:
        # 1.获取version版本更改文件列表的svn命令
        strings = "svn log -r " + version + " -v url"
        # print(strings)

        # 2.执行命令
        proc = subprocess.Popen(strings.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        # 3.按新增（add）、修改（modify）、删除（delete）分组
        for line_one in (str(stdout)).split('\\r\\n'):
            line_one = line_one.split(' (from')[0]
            if line_one.startswith("   A ") and line_one.count(".") == 1:
                set_add.add(line_one.replace("   A ", ""))
            if line_one.startswith("   M ") and line_one.count(".") == 1:
                set_mod.add(line_one.replace("   M ", ""))
            if line_one.startswith("   D "):
                line_one = line_one.replace("   D ", "")
                if line_one.count(".") == 0:
                    for del_dir in set_add:
                        if del_dir.count(line_one) == 1:
                            set_del.add(del_dir)
                    for del_dir in set_mod:
                        if del_dir.count(line_one) == 1:
                            set_del.add(del_dir)
                if line_one.count(".") == 1:
                    set_del.add(line_one)
    # 修改列表去除新增列表中包含的文件及删除列表中包含的文件
    list_mod = list(set_mod - set_add - set_del)
    # 新增修改去除删除列表中包含的文件
    list_add = list(set_add - set_del)
    list_del = list(set_del)
    list_add.sort()
    list_mod.sort()
    list_del.sort()

    return list_add, list_mod, list_del


def save_2_file(line_his):
    """ 复制文件 """
    # 当前日期YYYYMMDD
    dir_time = time.strftime('%Y%m%d', time.localtime(time.time()))
    # 增量包文件
    package_file = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\CJB' + dir_time + 'YSXTQX\\ysxtqx\\'

    temp = line_his[27:].replace('/', '\\').replace('.java', '.class')
    if temp.startswith("webapp"):
        temp = temp[7:]
    elif temp.startswith("java"):
        temp = "WEB-INF\\classes\\" + temp[5:]
    elif temp.startswith("resources"):
        temp = "WEB-INF\\classes\\" + temp[10:]
    else:
        return
    # 目标文件夹不存在，则创建文件夹
    base_dir = os.path.dirname(package_file + temp)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    # 复制文件
    shutil.copy(output_directory + temp, package_file + temp)
    # print(package_file + temp)


def add_deal_content(history):
    """ 正式发布列表整理 """
    history = list(history)
    history.sort()
    print('add+moi: ' + str(len(history)))
    for item in history:
        deal_line = item[27:].replace('/', '\\').replace('.java', '.class') + '\n'
        if deal_line.startswith("java"):
            deal_line = deal_line[5:]
        elif deal_line.startswith("resource"):
            deal_line = deal_line[10:]
        elif deal_line.startswith("webapp\WEB-INF\pages"):
            deal_line = deal_line[21:]
        else:
            deal_line = deal_line[7:]
        logfile.write(deal_line)
    pass


# 1.安装python
# 2.安装ipython：pip install ipython[all]
# 3.修改编译文件路径，用'\\'代替'\'
# 4.idea->version control->repository->多选->右键->copy reversion number
# 5.项目路径下cmd运行文件：get_change_list.py
if __name__ == "__main__":
    """ 主函数 """
    # =======A.项目编译输出路径======
    output_directory = "targetDirectory"

    # ========B.版本列表============
    # revisions = "8739 8740"
    revisions = "8793"
    revision_list = revisions.split()

    # 获取历史记录
    added, modified, deleted = get_revision_set(revision_list)

    # svn更新列表文件
    log_file = "C:\\Users\\" + getpass.getuser() + "\\Desktop\\ysxtqx_log_File.txt"
    # 创建文件，打开文件，清空文件
    if os.path.exists(log_file):
        os.remove(log_file)
    logfile = open(log_file, 'a')

    dir_time = time.strftime('%Y%m%d', time.localtime(time.time()))
    logfile.write(
        '收件人:  email\n'
        '抄送人:  email\n'
        '主体：YSQX资政测试增量 YSQX资政正式增量\n'
        '您好：\n'
        '这是YSQX外网测试增量发布文件：CJB' + dir_time + 'YSXTQX-测试，附件包括增量代码包及模版文件；请注意查收！\n'
        '这是YSXTQX外网正式增量发布文件：CJB' + dir_time + 'YSXTQX-正式，附件包括增量代码包、软件更新发布确认单；请注意查收！\n'
        '一、修改内容：\n'
        '  ---\n'
        '二、涉及修改文件：\n'
    )

    for line in added:
        logfile.write("A " + line + "\n")
        save_2_file(line)

    for line in modified:
        logfile.write("M " + line + "\n")
        save_2_file(line)

    for line in deleted:
        logfile.write("D " + line + "\n")

    # 正式发布列表
    logfile.write('\n正式发布列表\n')
    add_deal_content(set(added) | set(modified))
    logfile.close()

    print('add sum: ' + str(len(added)))
    print('moi sum: ' + str(len(modified)))
    print('del sum: ' + str(len(deleted)))
