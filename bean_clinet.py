#coding:utf-8

import json

import beanstalkc

'''
生产者
连接通道，向通道put任务
'''
def product():
	# 连接服务器
	beanstalk = beanstalkc.Connection(host='123.56.190.65', port=11300)
	# 使用bmi通道
	beanstalk.use('bmi')

	# 准备数据
	obj={}
	obj['height'] = 180
	obj['weight'] = 75
	encodedjson = json.dumps(obj)
	# 将数据放入通道
	beanstalk.put(encodedjson)

'''
消费者
连接通道，从通道获取任务，得到参数，处理
'''
def consumer():
	# 连接服务器
	beanstalk = beanstalkc.Connection(host='123.56.190.65', port=11300)

	# 定义来自哪个通道
	beanstalk.watch('bmi')

	# 获取一个job
	job = beanstalk.reserve()

	# 解析job，得到参数:
	data = json.loads(job.body) 
	#data['height'] :180
	#data['weight'] :75
	job.delete()
	#处理调用函数数据
	result = bmi(data['height'],data['weight'])
	print result

# 计算bmi指数
def bmi(height,weight):
	return weight*10000/(height*height)


def main():
	product()

	consumer()


if __name__ == '__main__':
	main()	