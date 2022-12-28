
import os
import pytest

if __name__ == '__main__':
    pytest.main(['-vs','--alluredir=./temp'])#生成allure报告
    os.system('allure generate ./temp -o ./report --clean')
    #os调用system   allure generate是固定语法   ./temp表示找到你的临时报告，如果临时报告是当前文件下的其他名字如aaa，那么就是./aaa
    #-o表示输出的意思   ./report表示输出到当前的report目录下   --clean表示清空./report原来有的报告，注意是clean，不是clear
