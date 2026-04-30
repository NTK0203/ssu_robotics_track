from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.utils.nucleus import get_assets_root_path
from isaacsim.robot.wheeled_robots.robots import WheeledRobot
from isaacsim.core.utils.types import ArticulationAction
import numpy as np

STOP = np.array([0.0, 0.0])
GO = np.array([5.0, 5.0])
BACK = np.array([-5.0, -5.0])
LEFT = np.array([0.0, 5.0])
RIGHT = np.array([5.0, 0.0])

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        self._elapsed_time = 0.0
        return

    def setup_scene(self):
        world = self.get_world()
        world.scene.add_default_ground_plane()
        assets_root_path = get_assets_root_path()
        jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
        self._jetbot = world.scene.add(
            WheeledRobot(
                prim_path="/World/Fancy_Robot",
                name="fancy_robot",
                wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
                create_robot=True,
                usd_path=jetbot_asset_path,
            )
        )
        return

    async def setup_post_load(self):
        self._world = self.get_world()
        self._jetbot = self._world.scene.get_object("fancy_robot")
        self._jetbot.get_articulation_controller = self._jetbot.get_articulation_controller()
        self._elapsed = 0.0

        self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
        return

    def send_robot_actions(self, step_size):
        self._elapsed_time += step_size
        if self._elapsed_time < 3.0:
            velocities = BACK
        elif self._elapsed_time < 8.0:
            velocities = STOP
        elif self._elapsed_time < 12.0:
            velocities = LEFT
        elif self._elapsed_time < 15.0:
            velocities = GO
        else:
            velocities = STOP   
        self._jetbot.apply_wheel_actions(
            ArticulationAction(joint_positions=None,
                                joint_efforts=None,
                                joint_velocities=velocities))
        return
