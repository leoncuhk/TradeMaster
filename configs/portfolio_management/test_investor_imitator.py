"""Investor Imitator快速测试配置 - 1 epoch"""

_base_ = [
    "../_base_/datasets/portfolio_management/dj30.py",
    "../_base_/environments/portfolio_management/env.py",
    "../_base_/agents/portfolio_management/investor_imitator.py",
    "../_base_/trainers/portfolio_management/investor_imitator_trainer.py",
    "../_base_/losses/mse.py",
    "../_base_/optimizers/adam.py",
    "../_base_/nets/investor_imitator.py",
]

data = dict(
    type='PortfolioManagementDataset',
    data_path='data/portfolio_management/dj30',
    train_path='data/portfolio_management/dj30/train.csv',
    valid_path='data/portfolio_management/dj30/valid.csv',
    test_path='data/portfolio_management/dj30/test.csv',
    test_dynamic_path='data/portfolio_management/dj30/test_with_label.csv',
    tech_indicator_list=[
        'high', 'low', 'open', 'close', 'adjcp', 'zopen', 'zhigh', 'zlow',
        'zadjcp', 'zclose', 'zd_5', 'zd_10', 'zd_15', 'zd_20', 'zd_25', 'zd_30'
    ],
    length_day=10,
    initial_amount=100000,
    transaction_cost_pct=0.0001,
    test_dynamic='-1')

environment = dict(type='PortfolioManagementInvestorImitatorEnvironment')

agent = dict(
    type='PortfolioManagementInvestorImitator',
    memory_capacity=1000,
    gamma=0.99,
    policy_update_frequency=500)

trainer = dict(
    type='PortfolioManagementInvestorImitatorTrainer',
    epochs=1,  # 快速测试
    work_dir='work_dir/test_investor_imitator',
    if_remove=False)

loss = dict(type='MSELoss')
optimizer = dict(type='Adam', lr=0.001)

act = dict(
    type='MLPCls',
    input_dim=None,
    dims=[128],
    output_dim=None)

task_name = "portfolio_management"
dataset_name = "dj30"
net_name = "investor_imitator"
agent_name = "investor_imitator"
optimizer_name = "adam"
loss_name = "mse"
