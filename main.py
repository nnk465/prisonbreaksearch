import os
import re

cwd = os.getcwd()
scripts_dir = os.path.join(cwd, 'scripts')
l = []

for season_entry in os.scandir(scripts_dir):
    if season_entry.is_dir():
        season_path = season_entry.path
        for episode_entry in os.scandir(season_path):
            if episode_entry.is_file():
                name = episode_entry.name
                l.append(episode_entry.path)
while True:
    al = []
    search = re.sub(r'[^a-zA-Z&éçà123546789,.\'\"]', '', input().lower())
    if search == "999":
        al = []
        print(999)
    elif not al:
        for season_entry in os.scandir(scripts_dir):
            for episode_entry in os.scandir(season_entry.path):
                with open(episode_entry.path, "r+") as ep:
                    script = ep.read()
                    if search in script:
                        pos = script.find(search)
                        print(f"trouvé dans, l'épisode {episode_entry.name}, {season_entry.name},"
                              f"\n -->position: {pos}/{len(script)}")
                        al.append(episode_entry.path)
    else:
        for season_entry in os.scandir(scripts_dir):
            for episode_entry in os.scandir(season_entry.path):
                if episode_entry.path in al:
                    with open(episode_entry.path, "r+") as ep:
                        script = ep.read()
                        if search in script:
                            pos = script.find(search)
                            print(f"trouvé dans, l'épisode {episode_entry.name}, {season_entry.name},"
                                  f"\n -->position: {pos}/{len(script)}")
                        else:
                            al.remove(episode_entry.path)
