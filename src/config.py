BAD_IMAGE_IDS = ['5adc4c_0', '7b9aaa_0', 'bb06a5_0', 'e26a04_0', '280c26_0'] + \
                ['4ae44b_0', '53e66f_0', '7c2c2f_0', '74a450_1']

BLOCK_SIZE = 28
BLOCKS_PER_CROP = 8
CROP_SIZE = BLOCK_SIZE * BLOCKS_PER_CROP
BLOCK_THR = 90
CROP_THR = 0.6
MAX_CROPS_PER_IMAGE = 20
IMAGES_PER_SAMPLE = 4
EPOCHS_NUM = 10
SCALE_FACTOR = 24
TEST_SAMPLE_DUPL_RATE = 20
TRAIN_SAMPLE_DUPL_RATE = 4
CENTER_GROUPS = [(11,), (4,), (7,), (1, 5,), (10, 3), (6, 2, 8, 9,)]