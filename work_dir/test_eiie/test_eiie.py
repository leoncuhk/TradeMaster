act = dict(
    dims=[
        32,
    ],
    input_dim=11,
    kernel_size=3,
    output_dim=1,
    time_steps=10,
    type='EIIEConv')
agent = dict(
    gamma=0.99,
    memory_capacity=1000,
    policy_update_frequency=500,
    type='PortfolioManagementEIIE')
agent_name = 'eiie'
cri = dict(
    action_dim=29,
    hidden_size=32,
    input_dim=11,
    num_layers=1,
    output_dim=1,
    time_steps=10,
    type='EIIECritic')
data = dict(
    data_path='data/portfolio_management/dj30',
    initial_amount=100000,
    length_day=10,
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
    test_dynamic_path='data/portfolio_management/dj30/test_with_label.csv',
    test_path='data/portfolio_management/dj30/test.csv',
    train_path='data/portfolio_management/dj30/train.csv',
    transaction_cost_pct=0.001,
    type='PortfolioManagementDataset',
    valid_path='data/portfolio_management/dj30/valid.csv')
dataset_name = 'dj30'
environment = dict(type='PortfolioManagementEIIEEnvironment')
loss = dict(type='MSELoss')
loss_name = 'mse'
net_name = 'eiie'
optimizer = dict(lr=0.001, type='Adam')
optimizer_name = 'adam'
task_name = 'portfolio_management'
trainer = dict(
    epochs=1,
    if_remove=False,
    type='PortfolioManagementEIIETrainer',
    work_dir='work_dir/test_eiie')
transition = dict(type='Transition')
work_dir = 'work_dir/test_eiie'
