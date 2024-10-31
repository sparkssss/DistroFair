# Supplementary Package

[DistroFair](https://www.sciencedirect.com/science/article/abs/pii/S0164121224001353) is an automated test generation framework that identifies class-level fairness violations. DistroFair automatically learns the distribution of images in the dataset and generates images that are outside the distribution and finds class-level fairness violations in the generated images.

Link: [DOI](https://doi.org/10.1016/j.jss.2024.112090)

## Requirements

### Python Packages Required

* torch
* detectron2 (Note: A GPU with CUDA is highly recommended)
* numpy
* cv2
* PIL
* scipy

### Subject Specific Packages

**Note: Authentication keys for each of the individual subject programs are required to run the notebooks. You will also require a GPU and additional packages such as LaMa.**

#### Google Cloud

* from google.cloud import vision

Link: [Credentials](https://cloud.google.com/vision/docs/object-localizer#:~:text=Object%20Localization%20requests-,Set%20up%20your%20GCP%20project%20and%20authentication,-If%20you%20have)

#### MS Azure

* azure.cognitiveservices.vision.computervision

Link: [Credentials](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?pivots=programming-language-csharp&tabs=visual-studio#:~:text=the%20available%20features.-,Prerequisites,-An%20Azure%20subscription)

#### Amazon Web Services

* boto3

Link: [Credentials](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html#setting-up-iam)

### Additional Packages

We also use [LaMa](https://github.com/saic-mdal/lama) to manipulate images during the generation process.

## Usage

The code consists of 4 files.

* CLM_Submit.ipynb
* RecSubj3.ipynb
* submitFairnessErrGroupFinder.py
* submitFairnessErrCounter.py

CLM_Submit.ipynb is primarily concerned with the generation of OOD images. In particular, it seeks to find the bounds for the images in each cluster and generates images accordingly. It is able to generate images associated with insertion. It also generates the intermediate images for the deletion and rotation operations. LaMa is then used to further  manipulate the image.

RecSubj3.ipynb is primarily concerned with querying the subject programs and writing the results to a text file.

submitFairnessErrGroupFinder.py is used to identify classes that violate our fairness criteria.

submitFairnessErrCounter.py is used to find the number of erroneous images among the generated images.

## Original Images

The original images used for testing are included at the link below.

Link: [OriginalImages](https://storage.googleapis.com/jss-2023-distrofair-gen-images/DistroFairOrgImages/orgImages.zip)

## Generated Images

**Note: Generated Images are included in a separate zip file due to the large file size. It is approximately 70 GB.**

Link: [GeneratedImages](https://storage.googleapis.com/jss-2023-distrofair-gen-images/DistroFairGenImages/genImages.zip)


## Caveats

To execute these notebooks, you will need authentication keys for each of the individual subject programs. You will also require a GPU and additional packages such as LaMa.

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Citing DistroFair

```
@article{rajan2024distribution,
  title={Distribution-aware fairness test generation},
  author={Rajan, Sai Sathiesh and Soremekun, Ezekiel and Le Traon, Yves and Chattopadhyay, Sudipta},
  journal={Journal of Systems and Software},
  volume={215},
  pages={112090},
  year={2024},
  publisher={Elsevier}
}
```
