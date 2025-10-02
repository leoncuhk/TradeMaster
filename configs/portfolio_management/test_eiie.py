task_name = "portfolio_management"
dataset_name = "dj30"
net_name = "eiie"
agent_name = "eiie"
optimizer_name = "adam"
loss_name = "mse"
work_dir = "work_dir/test_eiie"

# 不使用变量的_base_
_base_ = [
    "../_base_/datasets/portfolio_management/dj30.py",
    "../_base_/environments/portfolio_management/env.py",
    "../_base_/agents/portfolio_management/eiie.py",
    "../_base_/trainers/portfolio_management/eiie_trainer.py",
    "../_base_/losses/mse.py",
    "../_base_/optimizers/adam.py",
    "../_base_/nets/eiie.py",
    "../_base_/transition/transition.py"
]

data = dict(
    type='PortfolioManagementDataset',
    data_path='data/portfolio_management/dj30',
    train_path='data/portfolio_management/dj30/train.csv',
    valid_path='data/portfolio_management/dj30/valid.csv',
    test_path='data/portfolio_management/dj30/test.csv',
    test_dynamic_path='data/portfolio_management/dj30/test_with_label.csv',
    tech_indicator_list=[
        'zopen', 'zhigh', 'zlow', 'zadjcp', 'zclose',
        'zd_5', 'zd_10', 'zd_15', 'zd_20', 'zd_25', 'zd_30'
    ],
    length_day=10,
    initial_amount=100000,
    transaction_cost_pct=0.001)

environment = dict(type='PortfolioManagementEIIEEnvironment')

transition = dict(type="Transition")

agent = dict(
    type='PortfolioManagementEIIE',
    memory_capacity=1000,
    gamma=0.99,
    policy_update_frequency=500)

trainer = dict(
    type='PortfolioManagementEIIETrainer',
    epochs=1,  # 减小为1以快速测试
    work_dir=work_dir,
    if_remove=False)

loss = dict(type='MSELoss')

optimizer = dict(type='Adam', lr=0.001)

act = dict(
    type="EIIEConv",
    input_dim=None,
    output_dim=1,
    time_steps=10,
    kernel_size=3,
    dims=[32]
)

cri = dict(
    type="EIIECritic",
    input_dim=None,
    action_dim=None,
    output_dim=1,
    time_steps=None,
    num_layers=1,
    hidden_size=32
)
