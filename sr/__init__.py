import sr
from simulator.sim_robot import SimRobot
from simulator.simulator import Simulator


zone = 0


def init_sim():
    """
    Initialise the simulator
    :return: the running Simulator object
    """
    config = {"game": "smallpeice-2016"}
    # Run the simulator in the background
    return Simulator(config, background=True)


def robot_gen(zone):
    """
    Initialise the robot
    :return: a function to call Robot() on
    """
    def robot():
        print "Starting robot..."
        with sim.arena.physics_lock:
            robot_object = SimRobot(sim)
            robot_object.zone = zone
            robot_object.location = sim.arena.start_locations[zone]
            robot_object.heading = sim.arena.start_headings[zone]
            return robot_object

    return robot

print "Starting simulator..."
# Set up the simulator
sim = init_sim()
# set up the new Robot() function
Robot = robot_gen(zone)
