"""修复mmcv 2.x兼容性 + Gym → Gymnasium迁移"""
import re
from pathlib import Path

print("=== 第1步: 修复mmcv → mmengine ===\n")

# 修复所有tools目录下的Config导入
for file in Path('tools').rglob('*.py'):
    content = file.read_text(encoding='utf-8')
    if 'from mmcv import Config' in content:
        content = content.replace('from mmcv import Config', 'from mmengine import Config')
        file.write_text(content, encoding='utf-8')
        print(f'✓ {file}')

# 修复utils.py
utils_file = Path('trademaster/utils/utils.py')
content = utils_file.read_text(encoding='utf-8')
content = re.sub(
    r'import mmcv\nfrom mmcv import Config\nfrom mmcv\.utils import Registry.*print_log',
    '''import mmcv
from mmengine import Config
try:
    from mmcv.utils import Registry, print_log
except ImportError:
    from mmengine import Registry
    from mmengine.logging import print_log''',
    content,
    flags=re.DOTALL
)
utils_file.write_text(content, encoding='utf-8')
print('✓ trademaster/utils/utils.py')

# 修复所有builder文件
builders = {
    'trademaster/datasets/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

DATASETS = Registry('dataset')

def build_dataset(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.data)
    dataset = build_from_cfg(cp_cfg, DATASETS, default_args)
    return dataset
''',
    'trademaster/environments/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

ENVIRONMENTS = Registry('environment')

def build_environment(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.environment)
    environment = build_from_cfg(cp_cfg, ENVIRONMENTS, default_args)
    return environment
''',
    'trademaster/agents/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

AGENTS = Registry('agent')

def build_agent(cfg, default_args = None):
    cp_cfg = copy.deepcopy(cfg.agent)
    agent = build_from_cfg(cp_cfg, AGENTS, default_args)
    return agent
''',
    'trademaster/trainers/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg

TRAINERS = Registry('trainer')

def build_trainer(cfg, default_args=None):
    cp_cfg = dict(cfg.trainer)
    trainer = build_from_cfg(cp_cfg, TRAINERS, default_args)
    return trainer
''',
    'trademaster/nets/builder.py': '''import copy
try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg

NETS = Registry('net')

def build_net(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg)
    net = build_from_cfg(cp_cfg, NETS, default_args)
    return net
''',
    'trademaster/optimizers/builder.py': '''from trademaster.utils import build_from_cfg
try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
import copy

OPTIMIZERS = Registry('optimizer')

def build_optimizer(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.optimizer)
    optimizer = build_from_cfg(cp_cfg, OPTIMIZERS, default_args)
    return optimizer
''',
    'trademaster/losses/builder.py': '''from trademaster.utils import build_from_cfg
try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
import copy

LOSSES = Registry('loss')

def build_loss(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.loss)
    loss = build_from_cfg(cp_cfg, LOSSES, default_args)
    return loss
''',
    'trademaster/transition/builder.py': '''from trademaster.utils import build_from_cfg
try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
import copy

TRANSITIONS = Registry('transition')

def build_transition(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.transition)
    transition = build_from_cfg(cp_cfg, TRANSITIONS, default_args)
    return transition
''',
    'trademaster/collector/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

COLLECTORS = Registry('collector')

def build_collector(cfg, default_args = None):
    cp_cfg = copy.deepcopy(cfg.collector)
    collector = build_from_cfg(cp_cfg, COLLECTORS, default_args)
    return collector
''',
    'trademaster/imputation/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

IMPUTATION = Registry('imputation')

def build_imputation(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.data)
    imputation_model = build_from_cfg(cp_cfg, IMPUTATION, default_args)
    return imputation_model
''',
    'trademaster/preprocessor/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

PREPROCESSOR = Registry('preprocessor')

def build_preprocessor(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.data)
    dataset = build_from_cfg(cp_cfg, PREPROCESSOR, default_args)
    return dataset
''',
    'trademaster/evaluation/market_dynamics_labeling/builder.py': '''try:
    from mmcv.utils import Registry
except ImportError:
    from mmengine import Registry
from trademaster.utils import build_from_cfg
import copy

Market_Dynamics_Model = Registry('market_dynamics_model')

def build_market_dynamics_model(cfg, default_args=None):
    cp_cfg = copy.deepcopy(cfg.market_dynamics_model)
    market_dynamics_model = build_from_cfg(cp_cfg, Market_Dynamics_Model, default_args)
    return market_dynamics_model
''',
}

for filepath, content in builders.items():
    Path(filepath).write_text(content, encoding='utf-8')
    print(f'✓ {filepath}')

print("\n=== 第2步: 将 Gym 迁移到 Gymnasium ===\n")

# 找到所有使用gym的Python文件
gym_files = [
    'trademaster/environments/portfolio_management/eiie_environment.py',
    'trademaster/environments/high_frequency_trading/environment.py',
    'trademaster/environments/order_execution/eteo_environment.py',
    'trademaster/environments/order_execution/pd_environment.py',
    'trademaster/environments/portfolio_management/deeptrader_environment.py',
    'trademaster/environments/portfolio_management/environment.py',
    'trademaster/environments/portfolio_management/inverstor_imitator_environment.py',
    'trademaster/environments/portfolio_management/sarl_environment.py',
    'trademaster/environments/algorithmic_trading/environment.py',
    'trademaster/environments/custom.py',
    'tools/earnmore/train.py',
    'pm/environment/pm_based_portfolio_return.py',
    'pm/environment/pm_based_portfolio_value.py',
    'pm/environment/wrapper.py',
    'finagent/environment/trading.py',
]

gym_updated = 0
for filepath in gym_files:
    file_path = Path(filepath)
    if not file_path.exists():
        continue

    content = file_path.read_text(encoding='utf-8')
    original = content

    # from gym import ... → from gymnasium import ...
    content = re.sub(r'^from gym import (.+)$', r'from gymnasium import \1', content, flags=re.MULTILINE)
    # import gym → import gymnasium as gym
    content = re.sub(r'^import gym$', 'import gymnasium as gym', content, flags=re.MULTILINE)

    if content != original:
        file_path.write_text(content, encoding='utf-8')
        gym_updated += 1
        print(f'✓ {filepath}')

print(f'\n✅ 所有兼容性问题已修复！')
print(f'   - mmcv → mmengine: 已更新')
print(f'   - gym → gymnasium: 更新了 {gym_updated} 个文件')
print('\n提示：运行后请卸载旧的gym: uv pip uninstall gym')
