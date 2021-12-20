from subprocess import run, Popen, PIPE

# 具体参考《python 自动化办公》05课
cmd1 = ["ls", '.']
return_code = run(cmd1)
# 退出状态码，一个为 0 的退出码表示进程运行正常
print(return_code)
print('------------------')
# 使用Popen获取程序运行结果
with Popen(cmd1, shell=True, stdout=PIPE, stderr=PIPE, encoding="utf-8") as fs:
    fs.wait(2)
    # 通过communicate  将PIPE 中的内容读取出来。
    files = fs.communicate()[0]

print(files)
