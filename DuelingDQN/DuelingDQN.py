import xuance
runner = xuance.get_runner('dueldqn',
                       'classic_control',  # 可选：classic_control、box2d、atari。
                       'Acrobot-v1',  # 可选：CartPole-v1、Acrobot-v1、MountainCar-v0 等。
                       "./DuelingDQN/DuelingDQN_Acrobot-v1.yaml",  # 请确保 my_config.yaml 的路径正确。
                       )
runner.run(mode='benchmark')