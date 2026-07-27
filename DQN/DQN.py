import xuance
runner = xuance.get_runner('dqn',
                       'classic_control',  # 可选：classic_control、box2d、atari。
                       'CartPole-v1',  # 可选：CartPole-v1、Acrobot-v1、MountainCar-v0 等。
                       "my_config.yaml",  # 请确保 my_config.yaml 的路径正确。
                       )
runner.run(mode='train')  # 或使用 runner.benchmark()