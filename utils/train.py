from dataloaders import create_k_fold_dataloaders
from model import Dhvani

if __name__ == "__main__":
    k_folds = 10
    random_seed = 42
    dataloaders = create_k_fold_dataloaders(k_folds=k_folds, random_seed=random_seed, test=False)
    for fold, (train_dataloader, val_dataloader, test_dataloader) in enumerate(dataloaders[2:], start=3):
        dhvani = Dhvani()
        print(f"Training on Fold {fold}/{k_folds}")
        dhvani.train_model(
            (train_dataloader, val_dataloader, None), fold_no=fold, training_mdn=False
        )
        dhvani.test_model(
            test_dataloader, fold_no=fold
        )
        break
