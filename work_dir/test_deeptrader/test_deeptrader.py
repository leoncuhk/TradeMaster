act = dict(
    K_l=10,
    N=29,
    dropout=0.2,
    kernel_size=2,
    num_channels=[
        12,
        12,
        12,
    ],
    num_inputs=16,
    type='AssetScoringNet')
act_net = dict(
    K_l=None,
    N=None,
    dropout=0.2,
    kernel_size=2,
    num_channels=[
        12,
        12,
        12,
    ],
    num_inputs=None,
    type='AssetScoringNet')
agent = dict(
    gamma=0.99,
    memory_capacity=1000,
    policy_update_frequency=500,
    type='PortfolioManagementDeepTrader')
agent_name = 'deeptrader'
cri = dict(
    K_l=10,
    N=29,
    dropout=0.2,
    kernel_size=2,
    num_channels=[
        12,
        12,
        12,
    ],
    num_inputs=16,
    type='AssetScoringValueNet')
cri_net = dict(
    K_l=None,
    N=None,
    dropout=0.2,
    kernel_size=2,
    num_channels=[
        12,
        12,
        12,
    ],
    num_inputs=None,
    type='AssetScoringValueNet')
data = dict(
    data_path='data/portfolio_management/dj30',
    initial_amount=100000,
    length_day=10,
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
    test_dynamic_path='data/portfolio_management/dj30/test_with_label.csv',
    test_path='data/portfolio_management/dj30/test.csv',
    train_path='data/portfolio_management/dj30/train.csv',
    transaction_cost_pct=0.001,
    type='PortfolioManagementDataset',
    valid_path='data/portfolio_management/dj30/valid.csv')
dataset_name = 'dj30'
environment = dict(type='PortfolioManagementDeepTraderEnvironment')
loss = dict(type='MSELoss')
loss_name = 'mse'
market = dict(hidden_size=12, n_features=16, type='MarketScoringNet')
market_net = dict(hidden_size=12, n_features=None, type='MarketScoringNet')
net_name = 'deeptrader'
optimizer = dict(lr=0.001, type='Adam')
optimizer_name = 'adam'
task_name = 'portfolio_management'
trainer = dict(
    epochs=1,
    if_remove=False,
    type='PortfolioManagementDeepTraderTrainer',
    work_dir='work_dir/test_deeptrader')
transition = dict(type='Transition')
