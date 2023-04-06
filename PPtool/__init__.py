import importlib
import subprocess

from .method import get_method

# 检查是否安装了PPshare
try:
    importlib.import_module('PPshare')
    print('检测到您的环境中已经安装了PPshare，可以正常使用PPtool')
except ImportError:
    # 如果未安装，则提示用户安装PPshare
    print('您的环境中没有配置PPshare，只有在安装了PPshare之后才能完整使用PPtool。')
    choice = input('是否需要安装PPshare？（y/n）').strip().lower()
    if choice == 'y':
        # 使用pip安装PPshare
        subprocess.check_call(['pip', 'install', 'PPshare'])
        print('安装成功！您已经可以正常使用PPtool了')
    else:
        print('取消安装PPshare。')

df = get_method('企业')
print(df)