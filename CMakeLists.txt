cmake_minimum_required(VERSION 3.5.1)
project(pycctag) 

# +++++++++++++ CCTag 3rd party ++++++++++++++++++++++++++++
find_package(CCTag CONFIG REQUIRED
	     PATHS /home/yuancaimaiyi/文档/CCTag/build/src/generated
	     NO_DEFAULT_PATH
)# set the path includes CCTagConfig.cmake
# opencv
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# +++++++++++++ pybind11 ++++++++++++++++++++++++++++
add_subdirectory(pybind11) #cmakelists.txt and pybind11-2.5.0(or another version) folder are in same directory

# ++++++++++++++ adding files to target ++++++++++++++++++++++
pybind11_add_module(pycctag pycctag.cpp)
target_include_directories(pycctag PUBLIC ${CCTAG_INSTALL}/include/cctag)
target_link_libraries(pycctag PUBLIC CCTag ${OpenCV_LIBS})
SET( CMAKE_CXX_FLAGS "-std=c++11 -O3")
