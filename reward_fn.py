def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
   
    # Read input parameters
    track_width = params['track_width']
    speed=params['speed']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])
    steering_angle = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    TOTAL_NO_STEPS = 250
    steps = params['steps']
   
   

    # Calculate 3 markers that are at varying distances away from the center line
    # marker_1 = 0.1 * track_width
    # marker_2 = 0.25 * track_width
    # marker_3 = 0.5 * track_width
   
    # # Give higher reward if the car is closer to center line and vice versa
    # if distance_from_center <= marker_1:
    #     reward = 2.0
    # elif distance_from_center <= marker_2:
    #     reward = 0.5
    # elif distance_from_center <= marker_3:
    #     reward = 0.1
    # else:
    #     reward = 1e-3  # likely crashed/ close to off track
   
    marker_1 = 0.10 * track_width
    marker_2 = 0.20 * track_width
    marker_3 = 0.30 * track_width
    marker_4 = 0.40 * track_width
    marker_5 = 0.50 * track_width
   
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1 and all_wheels_on_track:
        reward = 5.0
    elif distance_from_center <= marker_2 and all_wheels_on_track:
        reward = 3.5
    elif distance_from_center <= marker_3 and all_wheels_on_track:
        reward = 3
    elif distance_from_center <= marker_4 and all_wheels_on_track:
        reward = 2.5
    elif distance_from_center <= marker_5 and all_wheels_on_track:
        reward = 2
    else:
        reward = 1e-3  # likely crashed/ close to off track
       
    if progress == 90:
        reward += 2;
    if progress == 100:
        reward += 5;
       
    # Positive reward if the car is in a straight line going fast
    if abs_steering < 0.1 and speed == 3.7:
        reward *= 3.8
   
    # Reward for staying inside the track
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward+=5
       
    if not all_wheels_on_track:
        reward = 1e-3
   
    if  steering_angle == -30 or steering_angle == 30  and speed == 2:
        reward *= 1.5
    if steering_angle == -10 or steering_angle == 10 and speed == 3.70:
        reward *= 1.5
    if steering_angle == -20 or steering_angle == 20 and speed == 2.50:
        reward *= 1.5
   
    if (steps % 100) == 0 and progress > (steps / TOTAL_NO_STEPS)*100 :
        reward = reward + 15
       
    return float(reward)
