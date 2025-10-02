from trademaster.utils import build_from_cfg
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
