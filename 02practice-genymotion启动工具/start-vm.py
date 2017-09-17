import subprocess
import sys
import os

CACHE_FILE = os.path.join(sys.path[0], 'vms.ini')

SPLITTER = "###"

# GENYSHELL_PATH = os.path.join("D:", "Program Files", "Genymobile", "Genymotion")
GENYSHELL_PATH = "D://Program Files//Genymobile//Genymotion"


def get_vm_list():
    ori_cwd = os.getcwd()
    os.chdir(GENYSHELL_PATH)
    result = subprocess.check_output("genyshell.exe -c \"devices list\"", shell=True)
    os.chdir(ori_cwd)
    # result = subprocess.check_output("echo Id ddd", shell=True)
    result = result.decode("ASCII")
    # print(result)
    lines = result.split("\r\n")
    find_data = False
    vms = []
    for line in lines:
        if not find_data and line.strip().startswith("---"):
            find_data = True
            continue
        if find_data:
            datas = line.split("|")
            vm = datas[len(datas) - 1].strip()
            if len(vm.strip()) > 0:
                vms.append(vm)
    return vms


def cache_vm_list(vm_list):
    f = open(CACHE_FILE, 'w')
    f.write(SPLITTER.join(vm_list))


def read_cache_vm_list():
    try:
        f = open(CACHE_FILE, 'r')
        line = f.readline()
        if line.index(SPLITTER) != -1:
            return line.split(SPLITTER)
    except:
        pass
    return []


def get_vm_list_and_cache():
    vms = get_vm_list()
    cache_vm_list(vms)
    return vms


def open_vm(vm_name):
    ori_cwd = os.getcwd()
    os.chdir(GENYSHELL_PATH)
    # subprocess.call(["player.exe", "--vm-name ", vm_name]) #wait
    subprocess.Popen(["player.exe", "--vm-name ", vm_name])  # no wait
    os.chdir(ori_cwd)


# test
if __name__ == "__main1__":
    open_vm("Custom Phone - 6.0.0 - API 23 - 768x1280")


def read_a_char():
    return input()


def start_vm(num):
    try:
        num = int(num)
    except:
        print_no_newline('invalid num:')
        return False
    if type(num) is not int or (num < 0 or num >= len(vms)):
        print_no_newline('invalid num:')
    else:
        open_vm(vms[num])
        return True
    return False


def print_no_newline(str):
    sys.stdout.write(str)
    sys.stdout.flush()


# main
if __name__ == "__main__":
    vms = read_cache_vm_list()

    if len(vms) == 0 or (len(sys.argv) > 1 and sys.argv[1] == "refresh"):
        vms = get_vm_list_and_cache()

    # no vms open genymotion.exe
    if len(vms) == 0:
        print("No devices that can be used!")
        os.system("start " + GENYSHELL_PATH + "genymotion.exe")
    else:
        print("choose a vm:")
        for i, vm in enumerate(vms):
            print("  %d . %s" % (i, vm))
        print_no_newline('enter num (enter r/R to refresh vm list):')
        ch = read_a_char()
        if ch == 'r' or ch == 'R':
            print_no_newline('refreshing...')
            get_vm_list_and_cache()
            print(' done!')
            while not start_vm(ch):
                ch = read_a_char()
        else:
            while not start_vm(ch):
                ch = read_a_char()
