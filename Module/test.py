#import module module_test
import sys
sys.path.append('./abc')
import module_test
#goi ham da duoc dinh nghia trong module
module_test.print_func()

#import module time
import time
 
#in ra tất cả các mục trong thư viện time
print(dir(time))