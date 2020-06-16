'''
输入命令装饰器,用于创建和保存命令
'''

cmds = {}

def command(name):
    def decorater(func):
        cmds[name] = func
        return func

    return decorater