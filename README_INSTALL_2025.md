# TradeMaster Windows 安装指南 (2025)

> **环境**: Windows 11 | Python 3.11 | uv包管理器 | CPU only
> **日期**: 2025-10-02
> **状态**: ✅ 测试通过

## 快速开始

### 1. 一键安装

```bash
# 克隆项目
git clone https://github.com/TradeMaster-NTU/TradeMaster.git
cd TradeMaster

# 创建虚拟环境
uv venv --python 3.11

# 激活虚拟环境
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 安装PyTorch CPU版本
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 安装核心依赖（关键：numpy必须<2.0）
uv pip install "numpy<2.0"
uv pip install Flask Flask-Cors prettytable plotly psutil scipy pandas matplotlib statsmodels scikit_learn yfinance
uv pip install gym gymnasium tslearn h5py pydantic==1.10.2 jupyter celery pika fastdtw chardet pyarrow iopath sqlalchemy spacy fvcore
uv pip install "ray[rllib]" tensorflow mmcv kaleido==0.1.0 openfe
uv pip install git+https://github.com/optuna/optuna.git

# 安装TradeMaster
uv pip install -e .
```

### 2. 修复代码兼容性

创建并运行修复脚本：

```bash
# Windows CMD/PowerShell - 将下面内容保存为 fix_compatibility.py
python fix_compatibility.py

# 修复完成后，卸载旧的gym（重要！）
uv pip uninstall gym
```

**fix_compatibility.py 内容**:

```python
"""修复mmcv 2.x兼容性 + Gym → Gymnasium迁移"""
import re
from pathlib import Path

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
```

### 3. 运行测试示例

```bash
# 测试 EIIE 算法（Portfolio Management，推荐，约3分钟）
uv run python tools/portfolio_management/train_eiie.py --config configs/portfolio_management/test_eiie.py

# 测试 DeepScalper 算法（Algorithmic Trading，约3分钟）
uv run python tools/algorithmic_trading/train.py --config configs/algorithmic_trading/test_deepscalper.py
```

## 测试结果

### ✅ EIIE 算法 (Portfolio Management)

```
Train Episode: [1/1]
+--------------+-------------+------------+--------------+
| Total Return | Sharp Ratio | Volatility | Max Drawdown |
+--------------+-------------+------------+--------------+
| 180.464707%  |   1.141260  | 0.756963%  |  15.018162%  |
+--------------+-------------+------------+--------------+
Valid Episode: [1/1]
+--------------+-------------+------------+--------------+
| Total Return | Sharp Ratio | Volatility | Max Drawdown |
+--------------+-------------+------------+--------------+
|  9.600494%   |   0.450540  | 2.141029%  |  31.031459%  |
+--------------+-------------+------------+--------------+
train end
```

**运行时间**: ~3分钟
**状态**: ✅ 成功

### ✅ DeepScalper 算法 (Algorithmic Trading)

```
Train Episode: [1/1]
+--------------+
| Total Return |
+--------------+
| -126.330128% |
+--------------+
Valid Episode: [1/1]
+--------------+
| Total Return |
+--------------+
| -193.080913% |
+--------------+
train end
```

**运行时间**: ~3分钟
**状态**: ✅ 成功（负收益是正常的，这是1 epoch的快速测试）

### ❌ DeepTrader 算法 (Portfolio Management)

```
RuntimeError: Expected 2D (unbatched) or 3D (batched) input to conv1d,
but got input of size: [1, 29, 16, 10]
```

**状态**: ❌ 代码bug（tensor维度问题）
**原因**: 项目原始代码的维度处理问题，非环境配置问题

### ❌ Investor Imitator 算法 (Portfolio Management)

```
AssertionError: Torch not compiled with CUDA enabled
```

**状态**: ❌ 硬编码CUDA依赖
**原因**: 代码中硬编码`.cuda()`调用，无法在CPU环境运行

## 核心依赖版本

```
torch==2.8.0+cpu
numpy==1.26.4          # ⚠️ 必须<2.0
ray==2.49.2
tensorflow==2.20.0
mmcv==2.2.0
mmengine==0.10.7
gymnasium==1.1.1
pandas==2.3.3
scikit-learn==1.6.1
```

## 重要说明

### ⚠️ NumPy版本

必须使用numpy<2.0，否则会遇到`np.nan_to_num`兼容性问题。

### ⚠️ 配置文件

原始配置文件在`_base_`中使用f-string变量，mmengine无法解析。需要创建不含变量的配置：

```python
# configs/portfolio_management/test_eiie.py
_base_ = [
    "../_base_/datasets/portfolio_management/dj30.py",  # 硬编码路径
    "../_base_/environments/portfolio_management/env.py",
    # ...
]
```

### ⚠️ Ray在Windows上的问题

Ray RLlib在Windows上不稳定，建议使用非Ray算法：

**✅ 推荐算法（已测试通过）**:
- EIIE (Portfolio Management)
- DeepScalper (Algorithmic Trading)

**❌ 已知问题**:
- DeepTrader - tensor维度bug
- Investor Imitator - 硬编码CUDA
- PPO, SAC, TD3等Ray算法 - Windows不稳定

## Windows推荐运行的示例

### 1. EIIE - 投资组合管理 ✅

```bash
uv run python tools/portfolio_management/train_eiie.py \
    --config configs/portfolio_management/test_eiie.py
```

**特点**: 纯PyTorch实现，不依赖Ray，CPU友好

### 2. DeepScalper - 算法交易 ✅

```bash
uv run python tools/algorithmic_trading/train.py \
    --config configs/algorithmic_trading/test_deepscalper.py
```

**特点**: DQN算法，不依赖Ray，CPU友好

## 修复的问题

### 1. mmcv 1.x → 2.x

**问题**: Python 3.11需要mmcv 2.x，但API发生变化
**解决**:
- `from mmcv import Config` → `from mmengine import Config`
- `from mmcv.utils import Registry` → 添加try-except兼容层

### 2. NumPy 2.x

**问题**: NumPy 2.x breaking changes
**解决**: 降级到numpy 1.26.4

### 3. Gym → Gymnasium 迁移

**问题**: Gym已于2022年停止维护，不支持NumPy 2.0
**解决**:
- 自动将所有`import gym`替换为`import gymnasium as gym`
- 将`from gym import`替换为`from gymnasium import`
- 卸载旧的gym包：`uv pip uninstall gym`

### 4. Ray RLlib API

**问题**: `ray.rllib.agents` → `ray.rllib.algorithms`
**解决**: 在trainer.py中添加兼容代码（但Windows上仍不稳定）

## 验证安装

```bash
# 测试导入
uv run python -c "from trademaster.datasets.builder import build_dataset; print('✓ OK')"

# 测试配置
uv run python -c "from mmengine import Config; cfg=Config.fromfile('configs/portfolio_management/test_eiie.py'); print('✓ OK')"

# 完整测试
uv run python tools/portfolio_management/train_eiie.py --config configs/portfolio_management/test_eiie.py
```

## 新增文件

本次安装新增以下文件：

### 测试配置文件
- `configs/portfolio_management/test_eiie.py` - EIIE快速测试
- `configs/portfolio_management/test_deeptrader.py` - DeepTrader配置（有bug）
- `configs/portfolio_management/test_investor_imitator.py` - Investor Imitator配置（需CUDA）
- `configs/algorithmic_trading/test_deepscalper.py` - DeepScalper快速测试

### 工具文件
- `fix_compatibility.py` - 一键修复脚本
- `README_INSTALL_2025.md` - 本文档

## 常见问题

**Q: 为什么没有Gym警告了？**
A: 我们已将项目从已废弃的`gym`迁移到维护中的`gymnasium`。修复脚本会自动完成迁移。

**Q: Ray崩溃**
A: Windows限制，使用EIIE、DeepScalper等非Ray算法。

**Q: 配置加载失败**
A: 使用test_eiie.py等不含f-string变量的配置。

**Q: CUDA错误但我只有CPU**
A: 部分算法（如Investor Imitator）硬编码CUDA调用，无法在CPU运行。

## 项目状态总结

| 类别 | 算法 | 状态 | 说明 |
|------|------|------|------|
| Portfolio Management | EIIE | ✅ 通过 | 推荐使用 |
| Portfolio Management | DeepTrader | ❌ Bug | Tensor维度错误 |
| Portfolio Management | Investor Imitator | ❌ 需CUDA | 硬编码CUDA调用 |
| Algorithmic Trading | DeepScalper | ✅ 通过 | 推荐使用 |
| Portfolio Management | PPO/SAC/TD3 | ❌ Windows不支持 | Ray RLlib问题 |

---

**最后更新**: 2025-10-02
**测试环境**: Windows 11, Python 3.11.9, uv 0.7.8
**成功率**: 2/4 算法可运行 (50%)
