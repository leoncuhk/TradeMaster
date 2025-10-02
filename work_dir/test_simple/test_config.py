agent_name = 'ppo'
data = dict(
    data_path='data/portfolio_management/exchange',
    initial_amount=100000,
    tech_indicator_list=[
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
    'data/portfolio_management/exchange/test_labeled_3_24_-0.05_0.05.csv',
    test_path='data/portfolio_management/exchange/test.csv',
    train_path='data/portfolio_management/exchange/train.csv',
    transaction_cost_pct=0.001,
    type='PortfolioManagementDataset',
    valid_path='data/portfolio_management/exchange/valid.csv')
dataset_name = 'exchange'
environment = dict(type='PortfolioManagementEnvironment')
loss = dict(type='MSELoss')
loss_name = 'mse'
net_name = 'ppo'
optimizer = dict(lr=0.001, type='Adam')
optimizer_name = 'adam'
task_name = 'portfolio_management'
trainer = dict(
    agent_name='ppo',
    configs=dict(framework='tf2', num_workers=0),
    epochs=2,
    if_remove=False,
    type='PortfolioManagementTrainer',
    work_dir='work_dir/test_simple')
work_dir = 'work_dir/test_simple'
