'''

制表符 换行符 字符串处理函数
'''
message='  hello  mypython '
print("\tmessage")
print("\nmessage")
# lrstrip rstrip 去除字符串中开头和末尾的空白字符  strip 去掉两边所有空白字符
print(message.rstrip())
print(message.lstrip())
print(message.strip())
'''
注意单引号 ‘ 在 单双引号字符中的区别
”  ’  “   双引号中 ‘ 被认为是字符
’ ’ ‘  单引号中 被认为是 前一个’ 结尾
'''
message2="it's  my sister"
#message3='in's my sister '  解释器 会认为是多个字符串
