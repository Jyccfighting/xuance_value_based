import xuance
runner = xuance.get_runner('ddqn',
                       'classic_control',  # 可选：classic_control、box2d、atari。
                       'MountainCar-v0',  # 可选：CartPole-v1、Acrobot-v1、MountainCar-v0 等。
                       "./DoubleDQN/DoubleDQN_MountainCar-v0.yaml",  # 请确保 my_config.yaml 的路径正确。
                       )
runner.run(mode='benchmark') 