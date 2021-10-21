# -*- coding:utf-8 -*-
import re
import os
import subprocess

# os.system('svn diff -r 6830:6840 --summarize https://10.1.8.191/svn/shyycg_src/YSXT/trunk/ysxt')


def run(project_dir, date_from, date_to, search_key, file_name):
    """  处理log """
    log_dic = {}

    try:
        os.chdir(project_dir)  # 定位当前目录到项目路径
    except Exception as result:
        raise result

    # 获取分支
    branch_list = get_branches()

    for branch in branch_list:
        # 查看分支信息
        branch_list = deal_branch(branch)
        branch_list = list(set(branch_list))
        '''
        for item in branch_list:
            if item not in log_dic:
                log_dic[item] = branch_list[item]
            else:
                log_dic[item] += branch_list[item]
        '''
        save_2_file(file_name, branch_list)


def get_branches():
    """ 获取分支信息 """
    branch_list = []
    try:
        cmd_svn_remote = 'git remote show origin'
        # 打开子进程
        proc = subprocess.Popen(cmd_svn_remote.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 获取查询结果
        stdout, stderr = proc.communicate()
        # 信息不为空时进行分割获取分支集合
        if bool(stdout):
            tmp_str = stdout.decode().split('Local ref configured')[0]
            try:
                tmp_str = tmp_str.split('Remote branches:\n')[1]
            except Exception:
                tmp_str = tmp_str.split('Remote branch:\n')[1]
            branches = tmp_str.split('\n')
            for branch in branches[0:-1]:
                if re.search(' tracked', branch) is not None:
                    branch = branch.replace('tracked', '').strip(' ')
                    branch_list.append(branch)
        else:
            print("Can't get any branch!")
    except Exception:
        if bool(branch_list):
            print("Can't get any branch!")
        raise
    return branch_list


def deal_branch(branch):
    """ 处理分支 """
    '''
    # 切换到branch分支
    try:
        os.system('git checkout ' + branch)
    except Exception as result:
        print(result)
    '''
    cmd_git_log = "git log --stat --name-status".split()
    proc = subprocess.Popen(cmd_git_log, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    log_branch_dic = deal_lines(stdout.decode())
    return log_branch_dic


def deal_lines(stdout):
    log_dic = []
    for line in stdout.split('commit'):
        if re.search("0800", line) is not None:
            tmp_line = line.split("0800")[1]
            log_dic += tmp_line.split('\n')
    return log_dic


def save_2_file(filename, branch_list):
    new_file = open(file_name, 'w')
    for item in branch_list:
        if not item.startswith('    ') and bool(item):
            new_file.write(item + '\n')
    new_file.close()


if __name__ == "__main__":
    """ 定义参数并调用run() """
    project_dir = "./"
    date_from = ""
    date_to = ""
    search_key = ""
    file_name = "logfile.txt"
    run(project_dir, date_from, date_to, search_key, file_name)
