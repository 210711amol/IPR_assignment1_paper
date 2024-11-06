import eeglearn
import eeglearn.eeg_cnn_lib as eeglib

images = eeglib.gen_images(locs, features, nGridPoints)
eeglib.train(images, labels, train_test_fold, model_type)