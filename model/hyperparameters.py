import torch

SEED = 0
N_EPOCHS = 100
LR = 3e-6
GRADIENT_CLIPPING_VAL = 5

IN_CHANNELS = 16
OUT_CHANNELS = IN_CHANNELS
KERNEL_SIZE = 3
PADDING_TYPE = "same"
STRIDE = 1
ACTIVATION = torch.nn.ReLU()
DROPOUT_CNN = 0.25
BATCH_NORM = True

# mel spectrogram encoder
MS_ENCODER_GRU_HIDDEN_SIZE = 64
MS_MAX_LEN = 256
MS_NUM_FEATURES = 128
MS_GRU_INPUT_SIZE = 16
MS_GRU_N_LAYERS = 1

# phoneme encoder
P_ENCODER_GRU_HIDDEN_SIZE = 64
P_MAX_LEN = 256
EMBEDDING_DIM = 128
P_NUM_FEATURES = EMBEDDING_DIM

# phoneme decoder
P_DECODER_ATTN_EMBED_DIM = MS_ENCODER_GRU_HIDDEN_SIZE
P_DECODER_ATTN_N_HEADS = 8
P_DECODER_GRU_INPUT_SIZE = P_DECODER_ATTN_EMBED_DIM
P_DECODER_GRU_HIDDEN_SIZE = 64
P_DECODER_GRU_N_LAYERS = 1
P_DECODER_DROPOUT = 0.2

# word decoder
W_DECODER_ATTN_EMBED_DIM = P_DECODER_GRU_HIDDEN_SIZE
W_DECODER_GRU_INPUT_SIZE = W_DECODER_ATTN_EMBED_DIM

# PRN Classifier
PRN_CLF_IN_DIM = P_DECODER_GRU_HIDDEN_SIZE
PRN_CLF_OUT_DIM = 66

# MDN Classifier
MDN_CLF_IN_DIM = (
    P_DECODER_GRU_HIDDEN_SIZE  # word decoder & phoneme decoder have the same dimensions
)
MDN_CLF_OUT_DIM = 3
