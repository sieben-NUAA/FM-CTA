from torchvision import datasets

# Pre-defining mean and std for the datasets to reduce computational time
CIFAR10_mean = (0.4914, 0.4822, 0.4465)
CIFAR10_std = (0.2471, 0.2435, 0.2616)
MNIST_mean = (0.1307, 0.1307, 0.1307)
MNIST_std = (0.3081, 0.3081, 0.3081)
SVHN_mean = (0.4377, 0.4438, 0.4728)
SVHN_std = (0.1980, 0.2010, 0.1970)
CIFAR = ("CIFAR-10", CIFAR10_mean, CIFAR10_std, datasets.CIFAR10, 10, "data")
MNIST = ("MNIST", MNIST_mean, MNIST_std, datasets.MNIST, 10, "data/MNIST")
SVHN = ("SVHN", SVHN_mean, SVHN_std, datasets.SVHN, 10, "data")
DATASET = CIFAR  # Replace by the proper dataset
SECOND_DATASET = ("", MNIST_mean, MNIST_std, datasets.MNIST, 10, "data/MNIST")  # Leave first
# element as "" for not to employ it
