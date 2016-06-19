#coding:utf-8

import json

import beanstalkc



if __name__ == '__main__':
	'''
	Basic Operations
	基本操作
	'''
	# Connect
	# 连接服务器
	beanstalk = beanstalkc.Connection(host='123.56.190.65', port=11300)

	# See all tubes:
	# 查看打印所有通道
	print beanstalk.stats_tube('bmi')

	# Switch to the default (tube):
	# 选择使用哪个通道，这里选择default
	beanstalk.use('default')
	beanstalk.watch('default')
	
	# To enqueue a job:
	#　传入一个参数
	beanstalk.put('job_one')

	# To receive a job:
	job = beanstalk.reserve()

	# print a job:
	print job.body

	# Delete the job: 
	job.delete()
#-----------------------------
	# To enqueue a job:
	#　传入一个json格式
	obj={}
	obj['height'] = 180
	obj['weight'] = 75
	encodedjson = json.dumps(obj)

	beanstalk.use('bmi')
	beanstalk.watch('bmi')

	beanstalk.put(encodedjson)

	# To receive a job:
	job = beanstalk.reserve()

	# print a job:
	data = json.loads(job.body) 
	print data
	print data['height']

	# Delete the job: 
	job.delete()
