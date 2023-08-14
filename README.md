# ISOFIT Tutorials

Welcome to the ISOFIT tutorials repository! This repository contains a collection of Jupyter notebooks that serve as tutorials, examples, and further documentation for the ISOFIT project. These notebooks are designed to work seamlessly with the official ISOFIT Docker image, ensuring a hassle-free setup process.

ISOFIT is a powerful tool for atmospheric correction of remote sensing data, particularly hyperspectral data. These notebooks provide step-by-step guides and demonstrations on using ISOFIT for atmospheric correction, making it easier for users to understand and utilize the capabilities of the ISOFIT software.

## Getting Started

To get started with the ISOFIT Jupyter Notebooks, follow these simple steps:

1. **Pull the Official ISOFIT Docker Image**: The notebooks are designed to work with the official ISOFIT Docker image, which ensures a consistent environment. You can pull the image using the following command:

   ```bash
   docker pull jammont/isofit:latest
   ```

2. **Clone This Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/isofit/isofit-tutorials.git
   ```

3. **Run the Docker**: Create a container from the image and attach the tutorials directory:

   ```bash
   docker run --rm --shm-size=9.58gb -p 8888:8888 -v isofit-tutorials:/home/ray/isofit isofit/v2
   ```

   This command will start a Jupyter Notebook server inside the Docker container and make it accessible on your host machine.

4. **Launch Jupyter Notebooks**: Run a Docker container using the pulled image, and forward the Jupyter Notebook port (usually 8888) to your local machine:

   ```bash
   docker run -it -p 8888:8888 -v $(pwd):/workspace isofit/isofit:latest jupyter notebook --ip 0.0.0.0
   ```

   This command will start a Jupyter Notebook server inside the Docker container and make it accessible on your host machine.

5. **Access Notebooks**: Open your web browser and navigate to `http://localhost:8888`. You should see the Jupyter Notebook interface. Navigate to the notebooks directory and start exploring the ISOFIT tutorials!

## Contents

This repository contains the following tutorials:

- `NEON`: Step-by-step tutorial showcasing building a surface model, using apply_oe to generate defaults, then executing and improving ISOFIT results using NEON data

Feel free to explore, learn, and adapt the provided notebooks to your specific use cases.

## Contributing

We welcome contributions from the community! If you find any issues, have suggestions for improvements, or want to add your own tutorials/examples, please feel free to open an issue or submit a pull request.

## License

The ISOFIT Jupyter Notebooks project is licensed under the [Apache v2.0 License](https://opensource.org/license/apache-2-0/).
