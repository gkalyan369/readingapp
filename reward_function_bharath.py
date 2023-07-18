def reward_function(params):

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels = params['all_wheels_on_track']
    speed = params['speed']
    steps=params['steps']
    progress=params['progress']
    min_speed = 2
    min_steering=18
    steering=abs(params['steering_angle'])

    marker_1 = 0.01 * track_width
    marker_2 = 0.08 * track_width
    marker_3 = 0.2 * track_width
    marker_4 = 0.3 * track_width
    marker_5 = 0.5 * track_width    

    total=10
    reward=1
    if (steps % 100) == 0and progress > (steps/total) * 100 :
         reward += 10.0

    if distance_from_center <= marker_1 and all_wheels and speed > min_speed+1:
        reward = reward + 1.0
    elif distance_from_center <= marker_1 and all_wheels and speed > min_speed:
        reward = reward + 0.8        

    elif distance_from_center <= marker_2 and all_wheels and speed > min_speed:
        reward = reward + 0.6
        
    elif distance_from_center <= marker_2 and all_wheels and speed > min_speed+1:
        reward = reward + 0.5

    elif distance_from_center <= marker_3 and all_wheels :
        reward = reward + 0.2

    elif distance_from_center <= marker_4 and all_wheels :
        reward = reward + 0.1

    elif distance_from_center <= marker_5 and all_wheels:
        reward = reward + 0.001

    else:
        reward = 1e-3 

    if steering > min_steering:
        reward *= 0.8

    return float(reward)