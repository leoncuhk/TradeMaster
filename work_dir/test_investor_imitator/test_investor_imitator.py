act = dict(
    dims=[
        128,
    ], input_dim=638, output_dim=5, type='MLPCls')
agent = dict(
    gamma=0.99,
    memory_capacity=1000,
    policy_update_frequency=500,
    type='PortfolioManagementInvestorImitator')
agent_name = 'investor_imitator'
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
    transaction_cost_pct=0.0001,
    type='PortfolioManagementDataset',
    valid_path='data/portfolio_management/dj30/valid.csv')
dataset_name = 'dj30'
environment = dict(type='PortfolioManagementInvestorImitatorEnvironment')
loss = dict(type='MSELoss')
loss_name = 'mse'
net_name = 'investor_imitator'
optimizer = dict(lr=0.001, type='Adam')
optimizer_name = 'adam'
task_name = 'portfolio_management'
trainer = dict(
    epochs=1,
    if_remove=False,
    type='PortfolioManagementInvestorImitatorTrainer',
    work_dir='work_dir/test_investor_imitator')
