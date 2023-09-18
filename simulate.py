import time
import os

import model_manager
import game

seekers = model_manager.manager(300)
hiders = model_manager.manager(300)

current_time = time.strftime("%H-%M-%S", time.localtime())
print("Time:", time.strftime("%H:%M:%S", time.localtime()))
print("Date:", time.strftime("%d/%m/%Y", time.localtime()))
best_model_dir = f"models/best_model_{current_time}"
os.mkdir(best_model_dir)

for generation in range(100):
    seekers.mutate_models(10)
    hiders.mutate_models(10)

    if generation % 10 == 0:
        s = seekers.get_models()[-1]
        h = hiders.get_models()[-1]
        t = game.run(s, h, True)
        print(f"Seeker:, {-t}")
        print(f"Hider:, {t}")
        s.save(f"{best_model_dir}/seeker{generation}")
        h.save(f"{best_model_dir}/hider{generation}")

    # Run the seekers and hiders
    seeker_fitness = []
    hider_fitness = []
    for seeker, hider in zip(seekers, hiders):
        runtime = game.run(seeker, hider)
        seeker_fitness.append(-runtime)
        hider_fitness.append(runtime)

    if generation == 0:
        seekers.set_fitness(seeker_fitness)
        hiders.set_fitness(hider_fitness)
    else:
        seekers.update_fitness(seeker_fitness)
        hiders.update_fitness(hider_fitness)

    # Sort the seekers and hiders by fitness
    # get the best 100 seekers and hiders
    seekers.get_n_best_models(100)
    hiders.get_n_best_models(100)

    # Print status
    print("Generation", generation)

    # print the best hider and seeker fitness for this generation
    # print("S: ", seekers.get_n_best_models(1)[0].get_fitness()[0])
    # print("H: ", hiders.get_n_best_models(1)[0].get_fitness()[0])

    # print("Seekers:", seekers_fitness)
    # print("Hiders:", hiders_fitness)
    # print("Seekers:", seekers)
    # print("Hiders:", hiders)

# seekers.get_n_best_models(1)
# hiders.get_n_best_models(1)
# seekers.save("models/best_seeker")
# hiders.save("models/best_hider")
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Time:", current_time)
print("Date:", time.strftime("%d/%m/%Y", time.localtime()))
