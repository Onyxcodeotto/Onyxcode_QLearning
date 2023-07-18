from src.q_learning import Model

test = Model(100 , 100, 0.005, 0.5)
test.train()
test.autoplay()
