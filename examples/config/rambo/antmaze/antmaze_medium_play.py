from ..base import base_params
from copy import deepcopy

params = deepcopy(base_params)
params.update({
    'domain': 'antmaze',
    'task': 'medium-play-v0',
    'exp_name': 'antmaze_medium_play'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/antmaze-medium-play-v0',
    'rollout_length': 5,
    'adversary_loss_weighting': 0,
    'rollout_random': True
})
