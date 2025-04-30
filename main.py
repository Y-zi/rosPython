from time import sleep

from roslibpy import Message, Ros, Topic, Service, ServiceRequest


# 获取初始化状态
def getInitStatus(message):
    print("获取初始化状态 : {}".format(message['data']))

# #获取急停状态
def getEmergencyStatus(message):
    print("获取急停状态 : {}".format(message['data']))

# 获取充电状态
def getChargeStatus(message):
    print("获取充电状态 : {}".format(message['data']))

# 获取电量状态
def getPowerNum(message):
    print("获取电量状态 : {}".format(message['data']))

# 获取导航状态
def getNavigationStatus(message):
    print("获取导航状态 : {}".format(message['data']))

# 获取地图更新状态
def getWallUpdate(message):
    print("获取地图更新状态 : {}".format(message['data']))


if __name__ == '__main__':
    client = Ros(host='10.7.5.88', port=9090)
    client.run()
    print('Is ROS connected?', client.is_connected)
    # 接收topic -----------------------------------------------------
    # 创建监听机器初始化消息
    InitStatus_sub_ = Topic(client, '/androidmsg_initstatus', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getInitStatus)

    #获取急停状态
    InitStatus_sub_ = Topic(client, '/androidmsg_emergencystatus', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getEmergencyStatus)

    #获取充电状态
    InitStatus_sub_ = Topic(client, '/androidmsg_chargestatus', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getChargeStatus)

    #获取电量状态
    InitStatus_sub_ = Topic(client, '/power_report', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getPowerNum)

    #获取导航状态
    InitStatus_sub_ = Topic(client, '/androidmsg_navigationstatus', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getNavigationStatus)

    #获取地图更新状态
    InitStatus_sub_ = Topic(client, '/wall_update', 'std_msgs/Int16')
    InitStatus_sub_.subscribe(getWallUpdate)


    # 发布topic-------------------------------------------------------------------------
    # # 发布导航点指令
    # talker = Topic(client, '/navi_targetgoal', 'map_msgs/TargetGoal')
    # talker.publish(Message({'floor_id': 1,'map_id':2,'point_id':3}))
    #
    # # 停止运动
    # talker = Topic(client, '/navi_stop', 'std_msgs/Int16')
    # talker.publish(Message({'data': 5}))
    #


    # 调用service --------------------------------------------------------------------------
    # 获取地图信息
    getMapInfo = Service(client, '/get_maps', 'std_srvs/Trigger')
    getMapInfo_request = ServiceRequest()
    result = getMapInfo.call(getMapInfo_request)
    print('获取地图信息 response: {}'.format(dict(result)))

    # # 切换指定地图
    # service = Service(client, '/publish_map', 'map_msgs/PublishMap')
    # request = ServiceRequest({'type': 1, 'floor_id': 2,'map_id':3})
    # result = service.call(request)
    # print('切换指定地图  response: {}'.format(result))





    while True:
        # 速度控制移动
        pub_vel = Topic(client, '/cmd_vel', 'geometry_msgs/Twist')
        twist_msg = {
            'linear': {
                'x': 0.0,  # 线速度 x 方向 0.0 m/s
                'y': 0.0,
                'z': 0.0
            },
            'angular': {
                'x': 0.0,
                'y': 0.0,
                'z': 0.6  # 角速度 z 方向 0.3 rad/s
            }
        }
        pub_vel.publish(Message(twist_msg))
        sleep(0.01)
        pass