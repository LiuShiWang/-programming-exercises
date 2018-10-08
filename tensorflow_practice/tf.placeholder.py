#tensorflow常用生成函数
#tf.zeros 产生全为0的数组,tf.ones全为1，fill数字填充，constan常数
'''
import tensorflow as tf 
number = tf.zeros([2, 3])
one = tf.ones([2, 3])    
fill = tf.fill([2, 3],9)
constant = tf.constant([1,2,3])
with tf.Session() as sess:
    number = sess.run(number)
    one = sess.run(one)
    fill = sess.run(fill)
    constant = sess.run(constant)
    print(number)
    print(one)
    print(fill)
    print(constant)
'''

#通过变量实现神经网络的参数并实现前向传播的过程
   
'''
import tensorflow as tf
#声明w1，w2两个变量，这里还通过seed参数设定随机种子
#保证每次运行得到的结果是相同的
w1 = tf.Variable(tf.random_normal((2,3),stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal((3,1),stddev=1,seed=1))
x = tf.constant([[0.7,0.9]])
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.Session()
#不能直接通过sess.sun(y)来获取y的值
#因为w1和w2都还没有运行初始化过程
sess.run(w1.initializer)
sess.run(w2.initializer)
print(sess.run(y))
sess.close()
'''
#通过placeholder实现前向传播算法    
'''
x = tf.placeholder(tf.float32,shape(1,2),name='input')
a = tf.matmul(x,w1)
y = tf.matmul(a,w2)
sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)
print(sess.run(y,feed_dict = {x:[[0.7,0.9]]}))
'''

















