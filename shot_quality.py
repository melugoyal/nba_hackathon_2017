from ShotParser import load_shots
import pickle

defender_distance_range = 2
shot_distance_range = 3

class ShotQuality:
  def __init__(self):
    #pickle.dump(load_shots(), open('shot_data.pkl', 'wb'))
    self.shots = pickle.load(open('shot_data.pkl', 'rb'))
#    self.shots = {201939: ['a']}

  def shot_quality(self, player_id, defender_distance, shot_distance, shot_value):
    shots = self.shots[player_id]
    lb_def_dist = max(defender_distance - defender_distance_range, 0) # lower bound for defender distance
    ub_def_dist = defender_distance + defender_distance_range # upper bound for defender distance
    lb_shot_dist = max(shot_distance - shot_distance_range, 0)
    ub_shot_dist = shot_distance + shot_distance_range
    shot_count = 0
    made = 0
    dist_hist = dict()
    for shot in shots:
      if shot.defender_distance >= lb_def_dist and shot.defender_distance <= ub_def_dist:
        if shot.shot_distance >= lb_shot_dist and shot.shot_distance <= ub_shot_dist:
          #print shot.shot_distance
          #print shot.defender_distance
          shot_count += 1
          if shot.made:
            made += 1
    #print shot_count
    #print made
    if shot_count == 0:
      return 0.5*shot_value
    #print float(made)/shot_count
    ev = float(made)/shot_count * shot_value
    return ev

#shotQuality = ShotQuality()
#print shotQuality.shot_quality(201939, 0, 23, 3)
