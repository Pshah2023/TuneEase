from os import path


class Config:
    config = None

    def __init__(self) -> None:
        self.config = {
            "model": {
                "target": "tuneease.getmusic.modeling.models.dfm.DFM",
                "params": {
                    "diffusion_config": {
                        "target": "tuneease.getmusic.modeling.roformer.diffusion_roformer.DiffusionRFM",
                        "params": {
                            "diffusion_step": 100,
                            "alpha_init_type": "alpha1",
                            "auxiliary_loss_weight": 0.001,
                            "adaptive_auxiliary_loss": True,
                            "roformer_config": {
                                "target": "tuneease.getmusic.modeling.roformer.roformer_utils.DiffusionRoformerModel",
                                "params": {"vocab_size": 11880, "cond_weight": 0.5},
                            },
                        },
                    }
                },
            },
            "solver": {
                "base_lr": 3e-06,
                "adjust_lr": "none",
                "max_epochs": 50,
                "save_epochs": 10,
                "validation_epochs": 1,
                "sample_iterations": "epoch",
                "validate_iterations": 1000,
                "vocab_path": path.join(
                    path.dirname(path.dirname(path.abspath(__file__))),
                    "getmusic",
                    "utils",
                    "dict.txt",
                ),
                "print_specific_things": True,
                "ema": {"decay": 0.9, "update_interval": 100, "device": "cpu"},
                "clip_grad_norm": {
                    "target": "tuneease.getmusic.engine.clip_grad_norm.ClipGradNorm",
                    "params": {
                        "start_iteration": 0,
                        "end_iteration": 5000,
                        "max_norm": 0.5,
                    },
                },
                "optimizers_and_schedulers": [
                    {
                        "name": "none",
                        "optimizer": {
                            "target": "torch.optim.AdamW",
                            "step_iteration": 1,
                            "params": {"betas": (0.9, 0.999), "weight_decay": 0.01},
                        },
                        "scheduler": {
                            "step_iteration": 1,
                            "target": "tuneease.getmusic.engine.lr_scheduler.LinearDecayLRWithWarmup",
                            "params": {
                                "min_lr": 1e-06,
                                "warmup_lr": 0.0001,
                                "warmup": 1000,
                                "T_max": 300000,
                            },
                        },
                    }
                ],
            },
            "dataloader": {
                "batch_size": 3,
                "num_workers": 28,
                # 'train_datasets': [
                #     {
                #         'target':
                #             'tuneease.getmusic.data.bigdata.BigDataset',
                #             'params': {
                #                 'prefix': 'train',
                #                 'path': '/your-data-path',
                #                 'vocab_size': 11880
                #                 }
                #             }
                #     ], 'validation_datasets': [
                #         {
                #             'target': 'tuneease.getmusic.data.bigdata.BigDataset',
                #             'params': {
                #                 'prefix': 'valid',
                #                 'path': '/your-data-path',
                #                 'vocab_size': 11880
                #                 }
                #             }
                #         ]
            },
        }
