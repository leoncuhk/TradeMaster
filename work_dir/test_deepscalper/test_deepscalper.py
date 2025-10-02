act = dict(
    action_dim=3,
    dims=(
        64,
        32,
    ),
    explore_rate=0.25,
    state_dim=82,
    type='QNet')
agent = dict(
    batch_size=64,
    clip_grad_norm=3.0,
    gamma=0.9,
    max_step=12345,
    repeat_times=1,
    reward_scale=1,
    soft_update_tau=0,
    state_value_tau=0.005,
    type='AlgorithmicTradingDQN')
agent_name = 'deepscalper'
batch_size = 64
cri = None
data = dict(
    backward_num_day=5,
    data_path='data/algorithmic_trading/BTC',
    forward_num_day=5,
    tech_indicator_list=[
        'high',
        'low',
        'open',
        'close',
        'adjcp',
        'zopen',
        'zhigh',
        'zlow',
        'zadjcp',
        'zclose',
        'zd_5',
        'zd_10',
        'zd_15',
        'zd_20',
        'zd_25',
        'zd_30',
    ],
    test_dynamic='-1',
    test_dynamic_path=
    'data/algorithmic_trading/BTC/Market_Dynamics_Model/BTC/test_labeled_slice_and_merge_model_3dynamics_minlength12_quantile_labeling.csv',
    test_path='data/algorithmic_trading/BTC/test.csv',
    train_path='data/algorithmic_trading/BTC/train.csv',
    type='AlgorithmicTradingDataset',
    valid_path='data/algorithmic_trading/BTC/valid.csv')
dataset_name = 'BTC'
environment = dict(type='AlgorithmicTradingEnvironment')
loss = dict(type='MSELoss')
loss_name = 'mse'
net_name = 'deepscalper'
optimizer = dict(lr=0.001, type='Adam')
optimizer_name = 'adam'
task_name = 'algorithmic_trading'
trainer = dict(
    batch_size=64,
    buffer_size=1000000.0,
    epochs=1,
    horizon_len=128,
    if_discrete=True,
    if_keep_save=True,
    if_off_policy=True,
    if_over_write=False,
    if_remove=False,
    if_save_buffer=False,
    num_threads=8,
    seeds_list=(42, ),
    type='AlgorithmicTradingTrainer',
    work_dir='work_dir/test_deepscalper')
transition = dict(type='Transition')
work_dir = 'work_dir/test_deepscalper'
