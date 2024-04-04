from Testing.MetricVerification import read_bin_file_traces
from WPI_SCA_LIBRARY.FileFormat import *


fixed = read_bin_file_traces("unprotected_sbox\\single\\traces\\oscilloscope_traces\\oscilloscope_traces_50k_3000_samples_fixed_positive_uint8_t.bin")
random = read_bin_file_traces("unprotected_sbox\\single\\traces\\oscilloscope_traces\\oscilloscope_traces_50k_3000_samples_random_positive_uint8_t.bin")

file = FileParent("AnotherFile", "C:\\Users\\samka\\PycharmProjects\\MQP\\SCLA_API_MQP\\AnotherFile", existing=False)

experiment_1 = file.add_experiment(name="Experiment1")
dataset_1 = experiment_1.add_dataset(name="random", data_to_add=random, size=(50000, 3000), datatype='float32')

experiment_2 = file.add_experiment(name="Experiment2")
dataset_2 = experiment_2.add_dataset(name="fixed", data_to_add=fixed, size=(50000, 3000), datatype='float32')
