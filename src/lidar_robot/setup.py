import os
from glob import glob
from setuptools import find_packages,setup 

package_name= "lidar_robot"


setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=["test"]),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/'+ package_name]),
        ('share/'+package_name,['package.xml']),
        (os.path.join('share',package_name,'launch'), glob('launch/*.py')),
        (os.path.join('share',package_name,'worlds'), glob('worlds/*.sdf')),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='2D mobile robot with lidar in Gazebo Harmonic',
    license='Apache-2.0',
    entry_points={
        'console_scripts':[
            'lidar_reader = lidar_robot.lidar_reader:main',
            'obstacle_avoider = lidar_robot.obstacle_avoider:main',
        ],
    },
)
