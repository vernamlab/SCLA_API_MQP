from Testing.MetricVerification import read_bin_file_traces
from WPI_SCA_LIBRARY.FileFormat import *

fixed = read_bin_file_traces("unprotected_sbox\\single\\traces\\oscilloscope_traces\\oscilloscope_traces_50k_3000_samples_fixed_positive_uint8_t.bin")
random = read_bin_file_traces("unprotected_sbox\\single\\traces\\oscilloscope_traces\\oscilloscope_traces_50k_3000_samples_random_positive_uint8_t.bin")

file = FileFormatParent("AnotherFile", existing=False)

experiment_1 = file.add_experiment(name="Experiment1")

dataset_1 = experiment_1.create_dataset(name="random", size=(50000, 3000), datatype='float32')
dataset_1.add_data(data_to_add=random)

dataset_2 = experiment_1.create_dataset(name="fixed", size=(50000, 3000), datatype='float32')
dataset_2.add_data(data_to_add=fixed)

masked_fixed = read_bin_file_traces(
    "masked_sbox1\\traces\\oscilloscope_traces\\oscilloscope_traces_50k_3000_samples_fixed_positive_uint8_t.bin")






