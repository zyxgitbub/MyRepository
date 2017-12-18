# coding:utf-8  
import os  
  
file = open(os.path.abspath('.')+'/output.py','w')  
list_cn = ['中文','测试']  
list_en = ['chinese','test']  
  
file.write('********* write list *********\n')  
# 这里的中文列表将输出utf-8编码而不是期望的中文  
file.write(str(list_cn)+'\n')  
file.write(str(list_en)+'\n')  
  
file.write('********* write *********\n')  
for item in list_cn:  
    file.write('%s\n\n' % item)  
  
file.write('********* write reduce *********\n')  
file.write(reduce(lambda x, y: x + '\n\n' + y + '\n\n',list_cn))  
  
file.write('********* writelines *********\n')  
file.writelines('%s\n\n' % item for item in list_cn)  
  
file.write('********* print >> *********\n')  
for item in list_cn:  
    print >> file,'%s\n' % item  
  
file.close() 
