# This code is an interactive way of running the python code in the simulator
import argparse
import os
import threading

import sys
import yaml

from sim_robot import SimRobot
from simulator import Simulator
import vision

default_config = "/games/smallpeice-2016.yaml"

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config',
                    type=argparse.FileType('r'),
                    default=os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + default_config))
parser.add_argument('robot_scripts',
                    type=argparse.FileType('r'),
                    nargs='*')
args = parser.parse_args()

def read_file(fn):
    with open(fn, 'r') as f:
        return f.read()

robot_scripts = args.robot_scripts
prompt = "Enter the names of the Python files to run, separated by commas: "
while not robot_scripts:
    robot_script_names = raw_input(prompt).split(',')
    if robot_script_names == ['']: continue
    robot_scripts = [read_file(s.strip()) for s in robot_script_names]

with args.config as f:
    config = yaml.load(f)

sim = Simulator(config, background=False)

class RobotThread(threading.Thread):
    def __init__(self, zone, script, *args, **kwargs):
        super(RobotThread, self).__init__(*args, **kwargs)
        self.zone = zone
        self.script = script
        self.setDaemon(True)

    def run(self):
        def robot():
            with sim.arena.physics_lock:
                robot_object = SimRobot(sim)
                robot_object.zone = self.zone
                robot_object.location = sim.arena.start_locations[self.zone]
                robot_object.heading = sim.arena.start_headings[self.zone]
                return robot_object

        # inject the vision code so the robot has access to the rest of the simulator
        sys.modules['sr'] = vision
        # inject Robot as an initialised SimRobot
        exec self.script in {'Robot': robot}


# Run the robot in a different thread.
threads = []
for zone, robot in enumerate(robot_scripts):
    thread = RobotThread(zone, robot)
    thread.start()
    threads.append(thread)

# Run the simulator
sim.run()

# In pycharm, threads die after the main thread executes