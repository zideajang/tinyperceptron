
from tinyperceptron.wrapper.base import OpenMMLabDetWrapper,ModelWrapperConfig


model_wrapper_config = ModelWrapperConfig(name="openmmlab", endpoint="http://192.168.24.207:5600")

openmmlab_detection_wrapper = OpenMMLabDetWrapper({
    "name":"openmmlab", 
    "endpoint":"http://192.168.24.207:5600"
})

openmmlab_detection_wrapper.detect("/home/user/tinyperceptron/data/cat.png","fast_rcnn",0.5)