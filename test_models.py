import model_manager
import game

model_dir = "models/best_model_14-19-34/"

seekers = model_manager.manager(1)
hiders = model_manager.manager(1)

for i in range(0, 100,10):
    print("Running generation", i, "...")
    seekers.load(f"{model_dir}/seeker{i}.npz")
    hiders.load(f"{model_dir}/hider{i}.npz")
    game.run(seekers[0], hiders[0], True)
    print("Done")