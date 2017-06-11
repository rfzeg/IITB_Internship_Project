#!/usr/bin/env python
import rospy
from project.srv import direction,directionRequest,directionResponse
from project.srv import dirturn,dirturnRequest,dirturnResponse
from random import randint

## second step on vertex visit has to be done here
##finally should have a list of next turns at vertices.
rospy.init_node("direction_service_node")


def callback(request):
    check=request.check
    resp=directionResponse()
    




    ###Choosing which direction to go
    while True:
            i=randint(0,2)
            if check[i]>range_threshold:
                break

    
    if i==0:
       resp.response="L"

    elif i==1:
        resp.response="F"
    elif i==2:
         resp.response="R"
         
    return resp



range_threshold=3
while not rospy.is_shutdown():
    rospy.Service('/direction_service_server',direction,callback)
    rospy.spin()