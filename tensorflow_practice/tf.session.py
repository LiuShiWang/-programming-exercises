# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:30:02 2018

@author: Afini
"""

#会话机制
'''
import tensorflow as tf
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a+b
print(result)
'''
#输出结果为：Tensor("add:0", shape=(2,), dtype=float32)     

#使用会话的两种模式。
#first 当程序异常退出时，关闭会话的函数可能就不会被执行从而导致资源泄露。
'''
import tensorflow as tf
sess = tf.Session()
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a+b   
result = sess.run(result)
sess.close()
print(result)
'''
#second with自动释放所有资源，取缔了sess.close()
'''
import tensorflow as tf

sess = tf.Session()
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a+b  
 
with tf.Session() as sess:
    result = sess.run(result)
print(result)
'''        